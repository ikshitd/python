list = [1,2,3,4,5]

def func(nums):

  print("The numbers are : ")

  for num in nums : 
    
    print(num)

  print("the sum of the numbers are : ")  
    
  for i in nums:

    for j in nums:

      print(i+j)   


func(list)  


#big O ----> O(n + n**2)
#rule_4 -----> remove the non dominant terms
#big O ---> O(n**2)