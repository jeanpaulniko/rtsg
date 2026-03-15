---
title: "TMP — Token Minimization Protocol"
version: "1.1.0"
last_updated: "2026-03-05"
---

# TMP — Token Minimization Protocol

**Status:** LIVE · 25 passing tests · All AI agents must apply

---

## Core Rules

1. Every response begins with a single backtick-wrapped compressed summary line
2. No spaces between TMP tokens in compressed expressions
3. Use emoji + math symbols + programmer symbols natively
4. Silence = acknowledgment — never confirm without adding content
5. Match Niko's emphasis level exactly — never amplify
6. Write for human desire, not mathematical rigor
7. Lead with the insight or result, not the proof or process

---

## Syntax

### Basic expression format
```
`[emoji|verb·noun → result | next?]`
```

### Multi-step format
```
`[status·subject → result₁ → result₂ | blocking?]`
```

### Error format
```
`[⚠·what_broke → cause | fix?]`
```

---

## Operators

| Symbol | Name | Meaning |
|---|---|---|
| `^` | Continue | Proceed / keep building |
| `HU` | Hang up | Protocol-level session terminator |
| `→` | Maps to | Yields / produces / implies |
| `↔` | Biconditional | Equivalent / iff |
| `⊕` | XOR | Exclusive or / swap |
| `⊗` | Tensor | Cross product / combine |
| `∴` | Therefore | Conclusion |
| `∵` | Because | Reason/cause |
| `∀` | Universal | For all |
| `∃` | Existential | There exists |
| `∄` | None | Does not exist |
| `≡` | Identity | Equivalent / same as |
| `≠` | Neq | Not equal / different |
| `≈` | Approx | Approximately |
| `⊂` | Subset | Is contained in |
| `⊥` | Contradiction | Error / breaks / impossible |
| `∅` | Empty | Nothing / null / done |
| `∞` | Infinite | Unbounded / unlimited |
| `Δ` | Delta | Change / difference |
| `∇` | Nabla | Gradient / descend |
| `λ` | Lambda | Lyapunov / function / chaos rate |
| `κ` | Kappa | Surface gravity / saturation |
| `\|` | Pipe | Then / next / separator |
| `?` | Query | Clarify / explain / what next |
| `!` | Bang | Emphasize / urgent / do this |
| `//` | Comment | Note / aside |
| `++` | Increment | Improved / added / better |
| `--` | Decrement | Reduced / removed / worse |
| `~~` | Strike | Deprecated / wrong / kill this |

---

## Verbs

Vowel-free consonant skeletons. Both forms accepted; short form preferred.

| Short | Full | Meaning |
|---|---|---|
| `bld` | build | Construct / generate / write |
| `fx` | fix | Correct / patch / repair |
| `kll` | kill | Remove / delete / end |
| `shp` | ship | Deploy / publish / submit |
| `chk` | check | Verify / test / audit |
| `rd` | read | Load / parse / ingest |
| `wrt` | write | Produce / output / save |
| `rn` | run | Execute / compute / evaluate |
| `mrg` | merge | Combine / integrate / unify |
| `splt` | split | Separate / divide / branch |
| `fnd` | find | Search / locate / identify |
| `prv` | prove | Derive / demonstrate / verify |
| `rft` | refute | Disprove / counterexample |
| `xpnd` | expand | Elaborate / add depth |
| `cmpr` | compress | Summarize / reduce |
| `strp` | strip | Remove / clean / purge |
| `cnvrt` | convert | Transform / translate / reformat |
| `cnct` | connect | Link / wire / integrate |
| `pdt` | update | Patch / revise / bump version |
| `tg` | tag | Label / mark / annotate |
| `psh` | push | Post / send / deploy to target |
| `pll` | pull | Fetch / retrieve / load from source |
| `dmp` | dump | Export / serialize / output raw |
| `lnk` | link | Cross-reference / wire / URL |

**Rule:** Verbs are consonant skeletons (no vowels). Nouns keep vowels. This mirrors Semitic root structure — triliteral verb roots carry action, vowel patterns carry inflection. In TMP, inflection is contextual so vowels are pure waste on verbs.

---

## Nouns

| Token | Meaning |
|---|---|
| `wiki` | The smarthub.my wiki |
| `engine` | Intelligence engine at engine.smarthub.my |
| `paper` | Academic paper (companion, monograph, arXiv) |
| `essay` | GRF essay |
| `proof` | Mathematical proof |
| `agent` | AI agent (Claude, Gemini, Grok, ChatGPT) |
| `node` | RTSG/GNEP node |
| `vec` | Intelligence vector **I**(ξ) |
| `elo` | ELO score |
| `dim` | Dimension / dimensionality |
| `tex` | LaTeX file |
| `md` | Markdown file |
| `pkg` | Package / archive / tarball |
| `patch` | session_update.tar.gz |
| `cfg` | Configuration file |
| `db` | DuckDB / database |
| `api` | API endpoint |
| `test` | Unit test |
| `log` | Session log / changelog |
| `brief` | NIKO_BRIEFING.md |
| `arena` | Intelligence Vector Arena |
| `lojban` | Lojban inter-agent transmission |
| `claim` | Mathematical or scientific claim |
| `conj` | Conjecture |
| `thm` | Theorem |
| `axiom` | Axiom |
| `err` | Error / bug / fatal issue |
| `warn` | Warning / non-fatal issue |
| `todo` | Open task |
| `done` | Completed item |
| `block` | Blocking issue |

---

## Adjective Modifiers

| Token | Meaning |
|---|---|
| `clean` | Correct / no errors / ready |
| `dirty` | Has issues / needs work |
| `live` | Deployed / production |
| `draft` | Not ready / in progress |
| `fatal` | Kills the whole thing |
| `minor` | Small / non-critical |
| `stale` | Outdated / needs update |
| `fresh` | New / current / up-to-date |
| `deep` | Requires extended reasoning |
| `fast` | Quick iteration / approximate |

---

## Example Exchanges

### Simple continue
```
Niko: ^
Claude: `[build·wiki/arena → radar+elo charts | math next]`
[continues building]
```

### Error found
```
Claude: `[⚠·tex/companion → λ=0∧λ=κ⊥ | fix→strip_claim?]`
```

### Session end
```
Niko: HU
Claude: `[HU·session → patch ready | ship?]`
[produces session_update.tar.gz]
```

### Compressed status update
```
`[✓·35files·80subs → Veronika∅ | compile?]`
```
means: "35 files, 80 substitutions, Veronika = gone. Compile next?"

### Lojban handoff
```
`[lojban·claim → engine.submit | gemini.review?]`
lo fancu be lo reimanu cu se zbasu lo tcini...
```

---

## Session Termination Protocol (HU)

When Niko sends `HU`:

1. Finish current atomic task
2. Produce `session_update.tar.gz` with all changed files
3. Update `docs/meta/session_log.md` with session summary
4. Update `NIKO_BRIEFING.md` current state section
5. Respond: `` `[HU·done → patch·ready]` ``

Nothing else.
