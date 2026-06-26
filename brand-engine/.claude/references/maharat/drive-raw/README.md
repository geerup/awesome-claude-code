# drive-raw: local source files for instructor mining (Route B)

When the Google Drive MCP is not available, instructor source Docs are exported and
placed here, one folder per slug, then mined into a pack per the batch protocol.

Layout:
  references/drive-raw/<slug>/  <exported .md, .txt, .pdf, or .docx from the instructor Doc>

Slugs are in context/instructors/_CATALOG.md. mona-ataya is already mined (pilot A).
Record the export date in references/drive-extraction-log.md when a folder is added.
This directory holds raw source only; it is rewritten to house style on extraction,
never copied through.
