def group_names_and_scores(names: list[str], scores: list[int]) -> dict[str, int]:
    name_to_score = {}
    for name, score in zip(names, scores):
        name_to_score[name] = score

    return name_to_score

# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))
