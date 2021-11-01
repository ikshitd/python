list = ["a" , "b" , "c" , "d"]

list.append("e")

print(list)
#/// O(1)  since we are appending only one time at the end , the index position of the char remains the same.....

list.pop()

print(list)

#//// O(1) we are not looping and removing one char from the end ,,, index pos remains the same .... 

list.insert(0,"x")

print(list) #/////// O(n) THIS IS VERY INTERESTING !!!


"""
initial   :    ["a" , "b" , "c" , ""d]
index pos :      0     1     2      3 

finally when we add a char to the list what happens :

final     :    ["x" , "a" , "b" , "c" , "d"]
index_pos :      0     1     2     3     4 

we can clearly see that the whole index position shifted that means we are kinda iterating !!!!
so the BIG O can be given as ------>  O(n)
"""

list.insert(2,"alien")

print(list) # ------>  O(n)

"""
**** STATIC AND DYNAMIC ARRAY ***

"""

#in javascript and python the arrays that are usually dyanmic , so one thing to keep in mind is that sometimes the "append" method can be O(n) as well , and this is because of how the meory allocation takes place so what happens  is that when we use "append" method , it copies the array and increases it's memory so that new char could be added to it, so kinda "iterating" ....
#But , that's kinda deep !!!!
