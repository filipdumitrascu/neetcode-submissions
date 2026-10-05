def best_student(scores: list[tuple[str, int]]) -> str:
    highest = float("-inf")
    student = ""

    for name, score in scores:
        if score > highest:
            highest = score
            student = name

    return student


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
