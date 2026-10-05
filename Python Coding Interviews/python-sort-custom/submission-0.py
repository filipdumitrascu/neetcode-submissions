def get_word_length(word: str) -> int:
    return len(word)

def get_abs_value(number: int) -> int:
    return abs(number)

def sort_words(words: list[str]) -> list[str]:
    words.sort(key=get_word_length, reverse=True)
    return words

def sort_numbers(numbers: list[int]) -> list[int]:
    numbers.sort(key=get_abs_value, reverse=False)
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
