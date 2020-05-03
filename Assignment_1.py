#!/usr/bin/env python
# coding: utf-8

# # TASK 1

# # 1 Write a program which will find all such numbers which are divisible by 7 but are not a multipleof 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

# In[1]:


list=[i for i in range(2000,3201) if i%7==0 and i %5!=0]


# In[2]:


print(list)


# # 2 Write a Python program to accept the user's first and last name and then getting them printed in the the reverse order with a space between first name and last name.

# In[3]:


n1=input("Enter a first name:")
n2=input("Enter a last name:")
a=n1[::-1]
b=n2[::-1]
print(a+ ' ' +b)


# # 3  Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r3

# In[4]:


import math
pi=3.141
d=int(input("enter a value of diameter:"))
r=float(d/2)
print("volume of sphere is V:",4/3*(pi)*(r)**3)


# # TASK 2 

# #  1 Write a program which accepts a sequence of comma-separated numbers from console and generate a list.

# In[13]:


a=input("insert values:")
list=a.split(",")
print("List:",list)


# # 2 Create the below pattern using nested for loop in Python.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# 

# In[18]:


num=5
for i in range(num):
    for j in range(i):
        print ('* ', end="")
    print('')
for i in range(num,0,-1):
    for j in range(i):
        print('* ', end="")
    print('')


# #  3 Write a Python program to reverse a word after accepting the input from the user.
# 

# In[10]:


name=input("Enter a name:")
a=name[::-1]
print(a)


# #  4 Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens
# 

# In[12]:


print("WE, THE PEOPLE OF INDIA,\n\thaving solemnly resolved to constitute India into a SOVEREIGN,! \n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\tand to secure to all its citizens") 


# In[ ]:




