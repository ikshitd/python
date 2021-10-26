nemo = [
    "dorry", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt",
    "darla", "hank"
]

more_nemo = ["nemo"] * 100000

#just look at the result on how slow it is n

import time


def find_nemo(arr):

    start_time = time.time()

    for i in range(len(arr)):

        if arr[i] == "nemo":

            print("Found Nemo")

    end_time = time.time()

    print("The time took to find Nemo was {}".format(end_time - start_time))


find_nemo(more_nemo)
