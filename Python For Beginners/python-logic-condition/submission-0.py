def discount_applies(age: int) -> bool:
    return age < 18 or age >= 65

# don't modify this code below this line
print(discount_applies(17))
print(discount_applies(18))
print(discount_applies(40))
print(discount_applies(65))
print(discount_applies(70))
