# Week 2 — Competency 2: Code literacy & documentation

Reflections for HCDE 530 — Competency 2: **code literacy** and **documentation**.

---

## What “code literacy” means to me (in this class)

To me, code literacy means being able to **design a request** (ask for what I need clearly) and **detect issues** (notice when something is wrong—paths, errors, typos—and figure out what to fix).

---

## What “documentation” means to me (in this class)

Documentation is a **best practice** to **track your progress** and **understand why you made certain decisions at the time** (not just what the code does, but the reasoning behind it).

---

## What I did this week (concrete)

- CSV script (`demo_word_count.py` + `demo_responses.csv`)
- App reviews script (`app_reviews_word_count.py`)
- `dashboard.html`
- `context.md` (project walkthrough / documentation)
- Git / GitHub (repo, commits, push)
- Terminal / `cd` (running scripts from the right folder)
- `.cursorrules` (project conventions for tooling)

---

## Bridging code literacy and comments in `demo_word_count.py`

My first pass at inline comments mostly **narrated syntax** — “load the CSV,” “call our function,” “print summary statistics.” That tells future-me *what line is there*, not *why I structured the script that way*. That gap showed up when I tried to read the file a week later: I could follow the steps, but I could not quickly reconstruct the decisions.

**Designing a clear request** shows up in comments that record intent. For example, I print column headers before the data rows because I wanted output that **scans like a research table** — ID, role, word count, then a short text preview — not a wall of numbers. The comment on the loop — *“so that we don't have to repeat code for each row”* — is the kind I am aiming for: it explains **why iteration exists**, not that a `for` loop is a loop.

**Detecting when something went wrong** shows up in comments that flag assumptions. I noted that `DictReader` keys rows by **column name** so the script still works if column order changes in the CSV — that is the kind of bug I hit in practice when a export column shifts. I also noted that `word_counts` is a separate list because **summary statistics need the full set of counts**; without that comment, it is easy to “fix” the script by removing the list and then wonder why min/max/average break.

| Comment style | Example (weaker) | Example (stronger — what I revised toward) |
|---------------|------------------|--------------------------------------------|
| Narrates syntax | `# Call our function to count words in this response` | *(removed — the function name already says this)* |
| Explains a decision | `# Load the CSV file` | `# DictReader keys each row by column name — if the CSV column order changes, the script still works` |
| Explains user/research need | `# Print summary statistics` | `# Summary block answers a different question than the table: overall spread, not one row at a time` |

The docstring on `count_words()` follows the same rule: it says what the function takes and returns, and **why it is isolated** — one place to change length logic if I add filtering later.

This is the bridge I was missing in my first submission: **code literacy** is not only asking Cursor for help or reading tracebacks; it is leaving comments that tie lines back to **research workflow** (scan by role, compare response length, survive a messy export) so documentation and the script reinforce each other.

---

## Observations about Competency 2

- **Paths and the terminal:** Setting up the path and figuring out what the issue was took real attention (wrong folder, typos in filenames, quoting paths with spaces).
- **Cursor and GitHub:** Working through when Cursor/GitHub felt “not connecting” was confusing at first; sorting that out was part of building literacy.
- **Comment revision:** Re-reading professor feedback, I updated `demo_word_count.py` to drop comments that only restated the code and kept ones that explain **structure choices** (loop, list, preview truncation, summary block). `context.md` still holds the longer walkthrough; inline comments now point to *why*, not *what*.

---

## How this connects to UX research / design practice

This ties to **UX research** because code can help **organize data**—whether **quant data** or working through **transcripts**—so analysis is **less time-consuming** and more repeatable than doing everything by hand. Comments that explain *why* I truncated previews or separated row output from summary stats mirror how I would note **decisions in a research log** — not just what I did, but what question each step was meant to answer.

---

## Artifacts / evidence

- **Repository:** [github.com/mttran-stack/hcde-530-week-2-project](https://github.com/mttran-stack/hcde-530-week-2-project)
- **Code:** `demo_word_count.py`, `app_reviews_word_count.py`, `demo_responses.csv`
- **Documentation:** `context.md`, `week2.md`, `.cursorrules`
- **Visualization:** `dashboard.html`

---

## One thing I want to get better at next

**Writing “why” comments on the first draft** instead of adding them only after feedback — closing the gap between intent (what I need the computer to do) and comments that would let future-me or a collaborator follow the reasoning without re-deriving it from the syntax.
