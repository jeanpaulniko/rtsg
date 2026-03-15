---
title: "TMP Cheatsheet"
---

# TMP Cheatsheet

## Quick Reference

| Input | Claude does |
|---|---|
| `^` | Continue building |
| `HU` | End session cleanly |
| Single word | Minimal response |
| Full sentence | Match length proportionally |
| `?` after claim | Explain/justify |
| `!` after claim | Emphasize/expand |

## Response Format

```
`[summary_line]`

[content]
```

## Update Protocol

At end of each session Claude produces `session_update.tar.gz`. Run:
```bash
./niko-update.sh session_update.tar.gz
```
Wiki rebuilds automatically. No manual file management.
