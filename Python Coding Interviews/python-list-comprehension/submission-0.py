def create_list_of_odds(n: int) -> list[int]:
    return [i for i in range(1, n + 1, 2)]


# do not modify below this line
print(create_list_of_odds(1))
print(create_list_of_odds(5))
print(create_list_of_odds(6))
print(create_list_of_odds(10))
