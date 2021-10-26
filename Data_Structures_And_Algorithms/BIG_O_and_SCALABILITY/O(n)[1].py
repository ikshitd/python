nemo = [
    "dorry", "bruce", "marlin", "nemo", "gill", "bloat", "nigel", "squirt",
    "darla", "hank"
]

more_nemo = ["nemo"] * 100000

#what is someone asks about the big O scalabilty by just looking at the code 

def find_nemo(arr):

    for i in range(len(arr)):

        if arr[i] == "nemo":

            print("Found Nemo")

#o(n) ---> liner 

print(find_nemo(more_nemo))