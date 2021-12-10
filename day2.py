
# # simple palendrone
# # first_name = "Sai kumar kadiveti"
# # print(first_name[::-1])

# # # List unpacking
# # numbers = [1, 2, 3, 4]
# # first, second, *other = numbers
# # print(first)
# # print(other)

# # looping over list

# # for index, letter in enumerate(numbers):
# #     print(index, letter)

# # for letter in enumerate(numbers):
# #     print(letter[0], letter[1])

# letters = ["a", "b", "c", "b", "d", "b", "f", "b", "e"]

# # adding in the list

# letters.append("b")
# letters.insert(1, "w")


# # Remove from the list

# # letters.pop()

# for i in range(5):
#     print(i)
#     letters.remove("b")

# print(letters)

# numbers = [1, 2, 3, 4, 5, 6, 87, 67, 5, 43, 2]
# numbers.sort()
# print(numbers)
# print(numbers)

# items = [
#     ("product1", 10),
#     ("product2", 9),
#     ("product3", 1000)
# ]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 1000)
]

items.sort(key=lambda item: item[1])
print(items)
