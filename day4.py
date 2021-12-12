
# # # # simple palendrone
# # # # first_name = "Sai kumar kadiveti"
# # # # print(first_name[::-1])

# # # # # List unpacking
# # # # numbers = [1, 2, 3, 4]
# # # # first, second, *other = numbers
# # # # print(first)
# # # # print(other)

# # # # looping over list

# # # # for index, letter in enumerate(numbers):
# # # #     print(index, letter)

# # # # for letter in enumerate(numbers):
# # # #     print(letter[0], letter[1])

# # # letters = ["a", "b", "c", "b", "d", "b", "f", "b", "e"]

# # # # adding in the list

# # # letters.append("b")
# # # letters.insert(1, "w")


# # # # Remove from the list

# # # # letters.pop()

# # # for i in range(5):
# # #     print(i)
# # #     letters.remove("b")

# # # print(letters)

# # # numbers = [1, 2, 3, 4, 5, 6, 87, 67, 5, 43, 2]
# # # numbers.sort()
# # # print(numbers)
# # # print(numbers)

# # # items = [
# # #     ("product1", 10),
# # #     ("product2", 9),
# # #     ("product3", 1000)
# # # ]


# # # def sort_item(item):
# # #     return item[1]


# # # items.sort(key=sort_item)
# # # print(items)

# # items = [
# #     ("product1", 10),
# #     ("product2", 9),
# #     ("product3", 1000)
# # ]

# # items.sort(key=lambda item: item[1])
# # print(items)

# # prices = list(map(lambda item: item[1], items))
# # print(prices)

# # PricesGretaer = filter(lambda item: item[1] > 9, items)
# # print(list(PricesGretaer))

# # price = [item[1] for item in items]
# # print(price)

# # priceGreater = [item for item in items if item[1] > 9]
# # print(priceGreater)

# # list1 = [1, 2, 3]
# # list2 = [100, 200, 300]

# # print(list(zip("abc", list1, list2)))

# # string = "saikumar"

# # list1 = (1, 2, 3, 4)


# # from collections import deque

# # queue = deque([])
# # queue.append(1)
# # queue.append(2)
# # queue.append(3)

# # queue.popleft()

# # print(list(queue))
# # first = [1, 1, 3, 4, 6, 5]
# # unique = set(first)

# # second = {1, 7}


# # print(unique & second)
# # print(unique | second)
# # print(unique - second)
# # print(unique ^ second)

# sentence = "I tried this program for twenty minutes didn't get the same way my instructor suggested so i tried my own solution to built my app"

# sentence1 = [*sentence]

# sentence2 = set(sentence1)

# char_frequency = {}

# for x in sentence2:
#     char_frequency[x] = sentence1.count(x)


# char_frequency_sorted = sorted(
#     char_frequency.items(), key=lambda kv: kv[1], reverse=True)

# print(char_frequency_sorted)
