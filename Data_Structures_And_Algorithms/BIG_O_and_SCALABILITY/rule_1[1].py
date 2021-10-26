# rule-1 : always think of the worst case 

nemo = [
    "dorry", "bruce", "marlin", "hank", "gill", "bloat", "nigel", "squirt",
    "darla", "nemo"
    ]

def find_nemo(arr):

    for i in range(len(arr)):

        print("running")

        if arr[i] == "nemo":

            print("Found Nemo")

            break 


#o(n) ---> liner

print(find_nemo(nemo))

#If we run this code this is not the best code because we have already got the word "nemo" at the 4th posn , so we will use a "break" statement 


#rule 1 : alwaysn  think about the worst case , likein this case that the "nemo is at the end of the list" ; whilw the best case can be that the "nemo" is the beginning of the list , so then  the BIG O n in that case would have  been o(1): representing a very nice and effecient code .