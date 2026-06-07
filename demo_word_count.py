# Demo: measure open-ended response length from a CSV export (typical UX interview/survey format)
import csv

# Keep the filename in one place so a rename in the folder only needs one edit
filename = "demo_responses.csv"
responses = []
# DictReader keys each row by column name — if the CSV column order changes, the script still works
with open(filename, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        responses.append(row)


def count_words(response):
    """Count the number of words in a response string.

    Takes a string, splits it on whitespace, and returns the word count.
    Isolated in a function so every row uses the same length rule — change once, apply everywhere.
    """
    return len(response.split())


# Print column headers first so output scans like a table (ID, role, length) before the text preview
print(f"{'ID':<6} {'Role':<22} {'Words':<6} {'Response (first 60 chars)'}")
print("-" * 75)
# Store counts while looping — summary stats (min, max, average) need the full list, not just printed rows
word_counts = []

# Loop/iterative structure so that we don't have to repeat code for each row
for row in responses:
    participant = row["participant_id"]
    role = row["role"]
    response = row["response"]

    count = count_words(response)
    word_counts.append(count)

    # Truncate preview so long responses don't push ID and word count off the terminal line
    if len(response) > 60:
        preview = response[:60] + "..."
    else:
        preview = response

    print(f"{participant:<6} {role:<22} {count:<6} {preview}")

# Summary block answers a different question than the table: overall spread, not one row at a time
print()
print("── Summary ─────────────────────────────────")
print(f"  Total responses : {len(word_counts)}")
print(f"  Shortest        : {min(word_counts)} words")
print(f"  Longest         : {max(word_counts)} words")
print(f"  Average         : {sum(word_counts) / len(word_counts):.1f} words")
