#dsa example 

def contains(arr_1 , arr_2):

    for i in range(len(arr_1)):

        for j in range(len(arr_2)):

            if arr_1[i] == arr_2[j] :

                return True

    return False

    #BIG O ----> O(a*b)                        

#So this is a more radical approach of solving the problem , since the big o for the following can be given as :

def func(arr_1 , arr_2):

    for i in range(len(arr_1)):
        
        if arr_1[i] in arr_2:

            return True 

    return False 


#BIG O ----> O(n)


list_1 = ["a" , "b" , "c" , "d"]
list_2 = ["x" , "y" , "a"]


print(func(list_1 , list_2))