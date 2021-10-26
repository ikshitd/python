#let's look at an example
import time


def compress_first_boxes(arr):

  start_time = time.time()

  print(arr[0])

  end_time = time.time()

  print("The time taken is {}".format(end_time-start_time))


  #now this is an example of a constant big(0) , because no matter how much is the length of the arr , simply we will be looping through it one time just to grab that one char . so the time to run this code will be same . 

print((compress_first_boxes(["hello", "world" , "joker"]*100000)))

#o(1) -----> constant time