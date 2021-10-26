#log all the pairs from the boxes
boxes = [1,2,3,4,5]

def log_pairs(arr):

  for i in range(len(arr)):

     for j in range(len(arr)):

      print(arr[i] , arr[j])


log_pairs(boxes) 



#big O ----> O(n*n) ----O(n*2)


