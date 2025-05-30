def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for t in text.lower():
        counts[t] = counts.get(t, 0) + 1
    return counts
