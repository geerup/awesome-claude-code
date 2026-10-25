import copy
import json
import sys
from pathlib import Path

import pytest

ENGINE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ENGINE / "scripts"))
DRAFT_PATH = ENGINE / "outputs" / "gated" / "application-001" / "draft.json"


@pytest.fixture
def draft():
    return copy.deepcopy(json.loads(DRAFT_PATH.read_text()))


def find_line(draft, line_id):
    for section in draft["sections"]:
        for line in [section.get("subtitle"), *section["lines"]]:
            if line and line["line_id"] == line_id:
                return line
    raise KeyError(line_id)
