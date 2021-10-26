list = [1,2,3,4,5]

def func(arr):

  for i in range(len(arr)):

    print("boooo !")


func(list)

#for the space complexity we don't care about the input instead of the for loop we are adding aything to the memory , hence the space complexity will be ---->  O(1)
def hi(n):

  hi_arr = []

  for i in range(n+1):

    hi_arr.append("hi")

  return(hi_arr)  

print(hi(6)) 

#big O ----> O(n)
