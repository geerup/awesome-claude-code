#!/usr/bin/env python3
"""Read-only Meta Ads MCP server for the Maharat marketing engine.

A thin, stdlib-only MCP server over stdio that exposes READ-ONLY Meta Marketing
API (Graph API v25.0) calls for planning and reporting on streams 5, 8, and 9.
It authenticates with META_ADS_ACCESS_TOKEN from the environment and makes only
HTTP GET requests. It has no create, update, upload, or spend tool, so it cannot
send or spend by construction. Building paused campaigns and any spend stay
human-gate actions under runtime/send-safeguards.md and CLAUDE.md principle 4.

Why a wrapper: the off-the-shelf Meta Ads MCP servers authenticate by Meta
Business OAuth (a browser callback), which a headless remote session cannot
complete. This wrapper consumes the static token that the read-only test on
2026-06-24 proved valid, so it works headless and stays read-only.

Protocol: JSON-RPC 2.0 over stdio, newline-delimited, per the MCP stdio
transport. Methods: initialize, tools/list, tools/call, ping, and empty
resources/prompts listings for client compatibility. Notifications get no reply.
Only JSON-RPC messages go to stdout; diagnostics go to stderr.

House rule: no em dashes, no tatweel, Western numerals, plain ASCII.
"""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

API_VERSION = "v25.0"
BASE = "https://graph.facebook.com/" + API_VERSION
TOKEN_ENV = "META_ADS_ACCESS_TOKEN"
SERVER_NAME = "meta-ads-readonly"
SERVER_VERSION = "0.1.0"
DEFAULT_PROTOCOL = "2025-06-18"


def log(msg):
    sys.stderr.write("[" + SERVER_NAME + "] " + msg + "\n")
    sys.stderr.flush()


def graph_get(path, params=None):
    """Read-only GET against the Graph API. Returns parsed JSON or raises."""
    token = os.environ.get(TOKEN_ENV, "")
    if not token:
        raise RuntimeError(TOKEN_ENV + " is not set in the environment.")
    params = dict(params or {})
    url = BASE + "/" + path.lstrip("/")
    if params:
        url += "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, method="GET")
    req.add_header("Authorization", "Bearer " + token)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        try:
            err = json.loads(body).get("error", {})
        except Exception:  # noqa: BLE001
            err = {"message": body[:300]}
        raise RuntimeError("Graph API " + str(e.code) + ": "
                           + str(err.get("message", body[:200])))
    except urllib.error.URLError as e:
        raise RuntimeError("network error reaching Graph API: " + str(e.reason))


def norm_account(account_id):
    s = str(account_id).strip()
    return s if s.startswith("act_") else "act_" + s


TOOLS = [
    {
        "name": "list_ad_accounts",
        "description": "List the Meta ad accounts the token can access. Read-only. "
                       "amount_spent is in the account currency minor unit.",
        "inputSchema": {"type": "object", "properties": {}, "additionalProperties": False},
    },
    {
        "name": "get_campaigns",
        "description": "List campaigns in an ad account. Read-only.",
        "inputSchema": {"type": "object", "properties": {
            "account_id": {"type": "string", "description": "Ad account id, with or without the act_ prefix."},
            "limit": {"type": "integer", "description": "Max rows, default 25."},
            "effective_status": {"type": "array", "items": {"type": "string"},
                                 "description": "Optional filter, e.g. [\"ACTIVE\", \"PAUSED\"]."},
        }, "required": ["account_id"]},
    },
    {
        "name": "get_adsets",
        "description": "List ad sets under an ad account (pass act_...) or a campaign id. Read-only.",
        "inputSchema": {"type": "object", "properties": {
            "parent_id": {"type": "string", "description": "An ad account id (act_...) or a campaign id."},
            "limit": {"type": "integer", "description": "Max rows, default 25."},
        }, "required": ["parent_id"]},
    },
    {
        "name": "get_ads",
        "description": "List ads under an ad account (pass act_...), campaign, or ad set id. Read-only.",
        "inputSchema": {"type": "object", "properties": {
            "parent_id": {"type": "string", "description": "An ad account id (act_...), campaign id, or ad set id."},
            "limit": {"type": "integer", "description": "Max rows, default 25."},
        }, "required": ["parent_id"]},
    },
    {
        "name": "get_insights",
        "description": "Performance insights for an account (act_...), campaign, ad set, or ad. "
                       "Read-only. spend is in the account currency.",
        "inputSchema": {"type": "object", "properties": {
            "object_id": {"type": "string", "description": "act_... account id, or a campaign/adset/ad id."},
            "date_preset": {"type": "string", "description": "today, yesterday, last_7d, last_30d, this_month, "
                                                            "maximum, etc. Default last_30d."},
            "level": {"type": "string", "description": "account, campaign, adset, or ad. Default account."},
            "fields": {"type": "string", "description": "Comma list. Default impressions,clicks,spend,reach,cpc,cpm,ctr,frequency."},
        }, "required": ["object_id"]},
    },
    {
        "name": "search_interests",
        "description": "Search Meta targeting interests for audience planning. Read-only.",
        "inputSchema": {"type": "object", "properties": {
            "query": {"type": "string"},
            "limit": {"type": "integer", "description": "Max rows, default 20."},
        }, "required": ["query"]},
    },
]


def call_tool(name, args):
    if name == "list_ad_accounts":
        return graph_get("me/adaccounts", {
            "fields": "account_id,name,account_status,currency,timezone_name,amount_spent",
            "limit": 100})
    if name == "get_campaigns":
        params = {"fields": "id,name,status,effective_status,objective,daily_budget,lifetime_budget,start_time,stop_time",
                  "limit": int(args.get("limit", 25))}
        if args.get("effective_status"):
            params["effective_status"] = json.dumps(args["effective_status"])
        return graph_get(norm_account(args["account_id"]) + "/campaigns", params)
    if name == "get_adsets":
        return graph_get(str(args["parent_id"]).strip() + "/adsets", {
            "fields": "id,name,status,effective_status,daily_budget,lifetime_budget,optimization_goal,billing_event",
            "limit": int(args.get("limit", 25))})
    if name == "get_ads":
        return graph_get(str(args["parent_id"]).strip() + "/ads", {
            "fields": "id,name,status,effective_status,creative",
            "limit": int(args.get("limit", 25))})
    if name == "get_insights":
        return graph_get(str(args["object_id"]).strip() + "/insights", {
            "date_preset": args.get("date_preset", "last_30d"),
            "level": args.get("level", "account"),
            "fields": args.get("fields", "impressions,clicks,spend,reach,cpc,cpm,ctr,frequency"),
            "limit": int(args.get("limit", 50))})
    if name == "search_interests":
        return graph_get("search", {"type": "adinterest", "q": args["query"],
                                    "limit": int(args.get("limit", 20))})
    raise RuntimeError("unknown tool: " + str(name))


def respond(id_, result=None, error=None):
    msg = {"jsonrpc": "2.0", "id": id_}
    if error is not None:
        msg["error"] = error
    else:
        msg["result"] = result
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()


def handle(req):
    method = req.get("method")
    id_ = req.get("id")
    has_id = "id" in req and req.get("id") is not None
    if method == "initialize":
        proto = (req.get("params") or {}).get("protocolVersion") or DEFAULT_PROTOCOL
        respond(id_, {
            "protocolVersion": proto,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        })
        return
    if method in ("notifications/initialized", "initialized", "notifications/cancelled"):
        return  # notifications get no reply
    if method == "ping":
        respond(id_, {})
        return
    if method == "tools/list":
        respond(id_, {"tools": TOOLS})
        return
    if method == "resources/list":
        respond(id_, {"resources": []})
        return
    if method == "resources/templates/list":
        respond(id_, {"resourceTemplates": []})
        return
    if method == "prompts/list":
        respond(id_, {"prompts": []})
        return
    if method == "tools/call":
        params = req.get("params") or {}
        name = params.get("name")
        args = params.get("arguments") or {}
        try:
            data = call_tool(name, args)
            text = json.dumps(data, ensure_ascii=False, indent=2)
            respond(id_, {"content": [{"type": "text", "text": text}], "isError": False})
        except Exception as e:  # noqa: BLE001
            respond(id_, {"content": [{"type": "text", "text": "ERROR: " + str(e)}], "isError": True})
        return
    if has_id:
        respond(id_, error={"code": -32601, "message": "method not found: " + str(method)})


def main():
    if not os.environ.get(TOKEN_ENV):
        log("warning: " + TOKEN_ENV + " not set; tool calls will error until it is.")
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(req, list):
            for r in req:
                handle(r)
        else:
            handle(req)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
