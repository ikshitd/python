nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

import math


def func(arr):

    print(arr[0])

    middle_index = math.floor(len(arr) / 2)

    index = 0

    while index < (middle_index):

        print(arr[index])

        index += 1

    for i in range(101):

        print("hi")


print(func(nums))

#rule-2 : drop the constants

#big O will be o(1) + o(n/2) + o(101) --> o(n + 1) ---> o(n)
