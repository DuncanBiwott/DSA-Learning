import re


def solution(S: str) -> int:
    result = 0
    operation = "+"  # Start with addition
    mylist = S.split()

    for word in S.split(r"\w+"):
        print(word.split())
        if word in ("one", "two"):
            value = 1 if word == "one" else 2
            result = result + value if operation == "+" else result - value
        else:
            operation = word  # Update operation for the next value

    return result


solution("one+two-two+one")

# Solution ONE
word = "ABCabcAefG"
small = {}
capital = {}
count = 0

for x, letter in enumerate(word):
    if letter.islower():
        small[letter] = x
    else:
        if capital.get(letter):
            capital[letter].append(x)
        else:
            capital[letter] = [x]

for item in small.items():
    capital_indexes = capital.get(item[0].upper())
    if capital_indexes and all(x > item[1] for x in capital_indexes):
        count += 1

print(count)

# Solution TWO
word = "ABCabcAefG"


# "abCABc"
# "xyzXYZabcABC"
def matched_letters_count(word: str = "aCbcABCA") -> int:
    small = {}
    capital = {}
    count = 0

    for x, letter in enumerate(word):
        if letter.islower():
            small[letter] = x
        else:
            if capital.get(letter):
                capital[letter].append(x)
            else:
                capital[letter] = [x]

    for item in small.items():
        capital_indexes = capital.get(item[0].upper())
        if capital_indexes and all(x > item[1] for x in capital_indexes):
            count += 1

    return count


print(matched_letters_count())

# small = {}
# capital = {}
# count = 0
#
# for x, letter in enumerate(word):
#     if letter.islower():
#         small[letter] = x
#     else:
#         if capital.get(letter) is not None:
#             pass
#         else:
#             capital[letter] = x
#
# for item in small.items():
#     if capital.get(item[0].upper()) is not None and item[1] < capital.get(item[0].upper()):
#         count += 1
#
# print(count)
