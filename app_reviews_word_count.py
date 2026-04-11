"""Count words in each fabricated app review and print summary stats."""

# 50 made-up app reviews (varied length and tone)
APP_REVIEWS = [
    "Love this app. Simple and fast.",
    "Crashes every time I open the camera. Unusable.",
    "Great for tracking habits. Wish there was a dark mode.",
    "Five stars. Customer support actually replied within an hour.",
    "Too many ads. Deleted after one day.",
    "The onboarding was confusing but once I figured it out it is fine.",
    "Battery drain is real. Lost twenty percent in an hour.",
    "Perfect for my commute. Offline mode works well.",
    "I use this daily for work. Export to PDF would be nice.",
    "Meh. Does what it says but nothing special.",
    "Subscription price feels high for what you get.",
    "Beautiful design. My friends asked what app this is.",
    "Login broke after the last update. Please fix.",
    "Good concept, execution is half baked.",
    "I have been using it for six months. Still my favorite.",
    "Search is slow when you have a lot of entries.",
    "Notifications are helpful and not spammy.",
    "Would not recommend. Lost my data twice.",
    "Solid app. Occasional lag on older phones.",
    "The tutorial skipped steps. I had to Google everything.",
    "Sync across devices works flawlessly for me.",
    "Needs widgets. Come on, it is twenty twenty six.",
    "Fun for kids. Parental controls are easy to find.",
    "Privacy policy is clear. I appreciate that transparency.",
    "Crashed during checkout. Lost my cart. Frustrating.",
    "Minimal and focused. Exactly what I wanted.",
    "Voice commands are hit or miss in noisy places.",
    "Great free tier. Paid features are worth it for power users.",
    "UI refresh looks modern. Took a day to get used to it.",
    "Cannot change the default font size. Accessibility fail.",
    "Reliable for budgeting. Bank connection was painless.",
    "Too bloated. Used to be faster two years ago.",
    "I recommend this to anyone learning a language.",
    "Map accuracy is off in rural areas.",
    "Checkout flow is smooth. Saved my payment info securely.",
    "Community features are toxic. Moderation needed.",
    "Works offline. That alone makes it a keeper.",
    "The trial ended without warning. Felt sneaky.",
    "Clean charts. I finally understand my spending.",
    "Multiplayer keeps disconnecting. Servers seem unstable.",
    "Easy to share lists with family. Real time updates rock.",
    "No dark mode in twenty twenty six is wild.",
    "Help docs are outdated. Screenshots do not match the app.",
    "Fast, lightweight, no nonsense.",
    "I paid for premium and still see ads. False advertising?",
    "Reminders helped me build a morning routine.",
    "Crop tool is awkward. Otherwise great photo editor.",
    "Support sent a generic reply. My bug is still there.",
    "Best meditation app I have tried. Guided sessions are calming.",
    "Location permission feels aggressive for a note app.",
]


def count_words(text: str) -> int:
    return len(text.split())


def main() -> None:
    word_counts = [count_words(review) for review in APP_REVIEWS]

    print(f"{'#':<4} {'Words':<6} Review (first 55 chars)")
    print("-" * 72)
    for i, (review, n) in enumerate(zip(APP_REVIEWS, word_counts), start=1):
        preview = (review[:55] + "...") if len(review) > 55 else review
        print(f"{i:<4} {n:<6} {preview}")

    total = len(word_counts)
    shortest = min(word_counts)
    longest = max(word_counts)
    average = sum(word_counts) / total

    print()
    print("── Summary ─────────────────────────────")
    print(f"  Reviews counted : {total}")
    print(f"  Shortest        : {shortest} words")
    print(f"  Longest         : {longest} words")
    print(f"  Average         : {average:.1f} words")


if __name__ == "__main__":
    main()
