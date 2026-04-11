# Project context: HCDE 530 Week 2 — CSV word counts

This file is the **main explanation** for this folder. Use it when you want to remember *why* the code exists and *which parts matter* for processing research-style data.

---

## 1. Purpose and audience

**Purpose:** Show how to **process a data file effectively** (read a CSV, turn rows into something you can loop over, compute a simple metric, print readable output). The script is a teaching example, not production analytics.

**Primary audience:** You, as a **UX research–leaning practitioner** learning Python. Examples and framing assume interview-style text and roles (researcher, designer, PM, etc.).

**Tone:** Beginner-friendly. Technical terms appear when they help (e.g. *dictionary*, *encoding*) and are explained in plain language.

---

## 2. Dataset overview

**File:** `demo_responses.csv`

**Columns (header row):**

| Column            | Meaning |
|-------------------|--------|
| `participant_id` | ID like `P01`, `P02` |
| `role`            | Job role (e.g. UX Researcher, UX Designer) |
| `response`        | Free-text answer (may contain commas; those fields are quoted in CSV) |

**Assumptions the script relies on:**

- The first row is the header with **exact** names: `participant_id`, `role`, `response`.
- Each data row has those three fields. If a column is renamed in the CSV, the keys in Python must match (`row["participant_id"]`, etc.).

**UX angle:** This mirrors a small export from interviews or a survey: one row per person, one text field per open-ended answer.

---

## 3. How the script works (by block)

### Imports and setup

```python
import csv

filename = "demo_responses.csv"
responses = []
```

- **`csv`** is Python’s built-in module for reading comma-separated files (no extra install).
- **`filename`** is a string path. The script looks for the file **in the folder you run the command from** (see §5).
- **`responses`** starts empty; you will fill it with one dictionary per row.

### Open file and load rows

```python
with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        responses.append(row)
```

- **`with open(...)`** opens the file and closes it automatically when the block ends (good habit so files don’t stay open by mistake).
- **`newline=""`** is recommended for CSV on Python 3 so line endings are handled correctly.
- **`encoding="utf-8"`** tells Python how to read characters (accents, smart quotes, etc.).
- **`csv.DictReader(f)`** reads the file so **each row is a dictionary**: keys come from the header row (`participant_id`, `role`, `response`). That’s easier than remembering “column 0, column 1…” for research data.
- The **`for`** loop appends each row dict to **`responses`**, so you end up with a **list of dictionaries**.

### Word-count helper

```python
def count_words(response):
    """Count the number of words in a response string.

    Takes a string, splits it on whitespace, and returns the word count.
    Used to measure response length across all participants.
    """
    return len(response.split())
```

- **`response.split()`** splits the string on whitespace into a list of “words” (rough measure: good for demos; not linguistic tokenization).
- **`len(...)`** counts how many pieces you got.
- Putting this in a **function** keeps the main loop readable and lets you reuse or test the idea later.

### Table header and loop

```python
print(f"{'ID':<6} {'Role':<22} {'Words':<6} {'Response (first 60 chars)'}")
print("-" * 75)

word_counts = []

for row in responses:
    participant = row["participant_id"]
    role = row["role"]
    response = row["response"]
    # ...
```

- First two **`print`** lines are a **fixed header** and a separator line (visual table in the terminal).
- **`word_counts`** collects every per-row count so you can compute min/max/average after the loop.
- **`row["..."]`** pulls fields by name — the payoff of `DictReader`.

### Inside the loop: count, preview, print

```python
    count = count_words(response)
    word_counts.append(count)

    if len(response) > 60:
        preview = response[:60] + "..."
    else:
        preview = response

    print(f"{participant:<6} {role:<22} {count:<6} {preview}")
```

- **`response[:60]`** is the first 60 characters (a **slice**). Long answers get `...` so the terminal stays readable.
- **`f"{...:<6}"`** is an f-string with **alignment**: `<` left-aligns in a field width (columns line up).

### Summary statistics

```python
print()
print("── Summary ─────────────────────────────────")
print(f"  Total responses : {len(word_counts)}")
print(f"  Shortest        : {min(word_counts)} words")
print(f"  Longest         : {max(word_counts)} words")
print(f"  Average         : {sum(word_counts) / len(word_counts):.1f} words")
```

- **`min` / `max` / `sum`** work on the list of integers you built.
- **`:.1f`** formats the average to one decimal place.

---

## 4. Which parts matter most (and why)

| Area | Why it matters for “processing a file effectively” |
|------|-----------------------------------------------------|
| `open` + `encoding` + `with` | Correct, safe file handling — first step of any CSV workflow. |
| `csv.DictReader` | Maps columns to **names** instead of positions; matches how you think about survey fields. |
| List + `append` in a loop | Standard pattern: **accumulate** all rows, then analyze. |
| `count_words` (or any small function) | Separates “what is a word count?” from “what do we do with each row?” |
| Collecting `word_counts` then summarizing | Two-phase pattern: **per-row metrics**, then **aggregate** stats — same idea as spreadsheets pivot/summary. |

**Design tie-in (occasional):** Word count is a blunt metric; in real work you’d pair length with themes, quotes, or tags — but the **data pipeline** (load → iterate → compute → report) is the same shape.

---

## 5. How to run and what to expect

**From Terminal, `cd` into this project folder** — the folder that contains `demo_word_count.py` and `demo_responses.csv`. If the path has spaces, wrap it in quotes.

```bash
cd "/path/to/hcde 530 week 2 project"
python3 demo_word_count.py
```

Replace `/path/to/...` with your real path (e.g. drag the folder into Terminal after `cd ` to paste the path).

**Expected output:**

1. A header row and a line of dashes.
2. One printed line per participant: ID, role, word count, first ~60 characters of the response.
3. A blank line and a **Summary** block: total responses, shortest/longest word count, average word count.

If you run from the **parent** folder without changing directory, Python may say it can’t find `demo_word_count.py` or the CSV — see §7.

---

## 6. Adapting to a new CSV

1. **Put the CSV** in the same folder as the script (or change `filename` to the new path/name).
2. **Match the header names** in the file to what the code expects, **or** change the code:
   - Update `row["participant_id"]`, `row["role"]`, `row["response"]` to your actual column names.
3. If you add columns (e.g. `study_id`, `segment`), you can still use `DictReader`; add variables like `study = row["study_id"]` and use them in `print` or in new metrics.
4. For **multiple text fields**, call `count_words` (or another function) on each field inside the loop.

---

## 7. Common errors and fixes

| Symptom | Likely cause | Fix |
|--------|----------------|-----|
| `can't open file '...demo_word_count.py'` | Wrong folder or typo in filename (`demon_` vs `demo_`) | `cd` into the project folder; run `python3 demo_word_count.py` |
| `FileNotFoundError` for the CSV | Script run from a directory where `demo_responses.csv` isn’t present | `cd` to the folder that contains both `.py` and `.csv` |
| `KeyError: 'participant_id'` | Header renamed or extra spaces in column names | Open CSV; align names with `row["..."]` keys |
| Garbled characters | Wrong encoding | Keep `encoding="utf-8"` if the file is UTF-8; otherwise re-export CSV as UTF-8 from your tool |

---

## 8. Next improvements (if you extend the project)

- **Export** results to a new CSV (e.g. add a `word_count` column) for Excel or Notion.
- **Filter** by `role` before printing or summarizing (research vs design vs PM).
- **Keyword or theme counts** (still beginner-friendly with a simple word list or manual tags).
- **Dashboard:** `dashboard.html` already summarizes the same kind of data in the browser; keep CSV and script aligned if you change columns.

---

## Related files

- **`.cursorrules`** — Short rules for AI assistants working in this folder; points here for full context.
- **`dashboard.html`** — Optional visual companion to the same dataset.

When you add or rename files, update the directory tree in `.cursorrules` in the same change.
