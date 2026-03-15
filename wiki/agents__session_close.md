---
title: "Session Close Protocol"
---

# Session Close Protocol

**Give this command to any AI agent at the end of every session.**

Every novel idea, derivation, correction, or insight from the session gets integrated into RTSG and the wiki. This is how the network learns.

---

## The Command

Copy and paste this verbatim at session end:

```
SESSION CLOSE PROTOCOL — execute now:

1. IDENTIFY every novel idea, claim, derivation, correction, conjecture, 
   or insight generated during this session that is not already in the wiki.

2. CATEGORIZE each item by destination:
   - New RTSG axiom/theorem/claim     → docs/rtsg/master.md or docs/rtsg/axioms.md
   - New equation or derivation       → docs/rtsg/equations.md or docs/math/
   - Companion paper update           → docs/papers/companions/{discipline}.md
   - Cosmological conjecture          → docs/papers/grf/cosmological_vision.md
   - Solved or advanced problem       → docs/problems/solved.md
   - Problem confidence update        → docs/problems/open.md
   - Engine result                    → docs/engine/live_results.md
   - Anything else                    → docs/meta/session_log.md

3. WRITE the complete updated content for every file that changed.
   Include the full file — not just the diff.

4. UPDATE docs/meta/session_log.md with a dated entry:
   ## YYYY-MM-DD — Session summary
   - What was built/discussed
   - Novel claims generated (list them)
   - Files changed (list them)
   - Open tasks carried forward

5. UPDATE NIKO_BRIEFING.md — replace the "Current State" section with
   today's date, what changed, and what is next.

6. OUTPUT all changed files in this format:

=== FILE: docs/path/to/file.md ===
[complete file content]
=== END FILE ===

One block per file. No truncation. Ready for extraction.
```

---

## After the AI Responds

Paste the output into a new Claude session with this command:

```
Extract these files into the wiki and produce session_update.tar.gz:

[paste the AI's === FILE: === blocks here]
```

Claude packages the tarball. On the VPS:

```bash
tar -xzf session_update.tar.gz && cd wiki && mkdocs build
```

Done. All session knowledge is now in the shared wiki, readable by every agent at the next session start.

---

## What Gets Integrated

| Type | Destination | Notes |
|---|---|---|
| New RTSG claim | `rtsg/master.md` | Label with date and agent ID |
| New axiom/theorem | `rtsg/axioms.md` or `rtsg/theorems.md` | Formal statement + proof sketch |
| New equation | `rtsg/equations.md` | With derivation notes |
| Cosmological conjecture | `papers/grf/cosmological_vision.md` | Niko's original contributions |
| Companion paper advance | `papers/companions/{field}.md` | Append to v2 integration section |
| Problem solved | `problems/solved.md` | Full solution summary |
| Confidence update | `problems/open.md` | Update % and reasoning |
| Engine result | `engine/live_results.md` | With timestamp |
| Session summary | `meta/session_log.md` | Always — every session |
| Current state | `NIKO_BRIEFING.md` | Always — for next session's AI |

---

## TMP Version

For TMP-fluent agents:

```
`HU·session → close_protocol·execute | output=FILE_blocks`
```
