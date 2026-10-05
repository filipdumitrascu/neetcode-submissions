def count_characters(word: str) -> Dict[str, int]:
    freq = {}
    for ch in word:
        freq[ch] = 1 + freq.get(ch, 0)
    return freq


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
