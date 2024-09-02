#1 Creat a Tuple of five elements
T1=(1,2,56,87,3)
print (T1)
#2 acces the first elemint of a tuple
print(T1[0])
#3 concatination two tuples
T2=(1,23,5,6,8)
print(T1+T2)
#4 repeat a Tuple 4 times
print(T1*4)
#5 creat a tuple with single element
T3=(1,)
print(T3)
#6 convert a list to a tuple
l1=[3,6,8,45,90]
T4=tuple(l1)
print(T4)
#7 convert a tuple in a list
L2=list(T3)
print(L2)
#8 Get the lenth of a tuple
print(len(T4))
#9 acces the last element of the tuple
print(T4[-1])
#10 itrete over a tuple and print each element
for element in T4:
    print(element)
#11 print first & last element
print(T4[0],T4[-1])
#12 itreate over a tuple & print each element with its index
for i,element in enumerate(T4):
    print(i,element)
#13 print sum of the elements in tuple
print(sum(T4))
#14 reverse tuple 
print(T4[::-1])
#15 Maximum and minimum value of a tuple
print(max(T4))
print(min(T4))
#16 sorted version( accendind order)
print(sorted(T4))
#17 disending order
print(sorted(T4[::-1]))