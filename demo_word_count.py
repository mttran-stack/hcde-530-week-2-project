import csv

#Keeps filename in one place so a rename in the folder only needs one edit
filename = "demo_responses.csv"
responses = []
#DictReader keys each row by column name
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


#Prints column headers so output scans like a table (ID, role, length)
print(f"{'ID':<6} {'Role':<22} {'Words':<6} {'Response (first 60 chars)'}")
print("-" * 75)
#Stores counts while looping
word_counts = []

#Loop/iterative structure so that code does not have to be repeated for each row
for row in responses:
    participant = row["participant_id"]
    role = row["role"]
    response = row["response"]

    count = count_words(response)
    word_counts.append(count)

    #Doesn't show full preview so that long responses don't push ID and word count off the terminal line
    if len(response) > 60:
        preview = response[:60] + "..."
    else:
        preview = response

    print(f"{participant:<6} {role:<22} {count:<6} {preview}")

#Summary block shows overall word count statistics for total responses, shortest, longest, and average.
print()
print("── Summary ─────────────────────────────────")
print(f"  Total responses : {len(word_counts)}")
print(f"  Shortest        : {min(word_counts)} words")
print(f"  Longest         : {max(word_counts)} words")
print(f"  Average         : {sum(word_counts) / len(word_counts):.1f} words")
