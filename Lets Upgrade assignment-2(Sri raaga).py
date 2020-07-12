#!/usr/bin/env python
# coding: utf-8

# 1) Research on whether addition, subtraction, multiplication, division, floor division and modulo
# operations be performed on complex numbers. Based on your study, implement a Python
# program to demonstrate these operations

# In[13]:


a=2+4j
b=1+2j
print("addition is:",(a+b))
print("subtraction is:",(a-b))
print("multiplicaltion is:",(a*b))
print("divison is:",(a/b))
#print(" floor divison is:",(a/b)) in the  Python 3 you can't compute floor division of complex numbers 
#print(" modulo operation is:",(a%b))  in the Python 3 you can't support modulo division of complex numbers 


# 2) Research on range() functions and its parameters. Create a markdown cell and write in your own
# words (no copy-paste from google please) what you understand about it. Implement a small
# program of your choice on the same.

# # Range() Function:
# 
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# 
# # Syntax
# range(start, stop, step)
# 
# 
# 
# # Parameter	Description
# start:Optional. An integer number specifying at which position to start. Default is 0
# stop:Required. An integer number specifying at which position to stop (not included).
# step:Optional. An integer number specifying the incrementation. Default is 1

# In[17]:


#Create a sequence of numbers from 0 to 10, and print each item in the sequence:

x = range(10)
for n in x:
  print(n)


# In[19]:


#Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:

x = range(3, 20, 2)
for n in x:
  print(n)


# In[20]:


# Create a sequence of numbers from 3 to 5, and print each item in the sequence:

x = range(3, 6)
for n in x:
  print(n)


# Markdown Cells:
# 
# Markdown cells can be selected in Jupyter Notebook by using the drop-down or also by the keyboard shortcut 'm/M' immediately after inserting a new cell.
# 
# 

# 3)  Consider two numbers. Perform their subtraction and if the result of subtraction is greater than
# 25, print their multiplication result else print their division result.

# In[18]:


a=100
b=39
c=a-b
if c>25:
 print(a*b)
else:
    print(a/b)


# 4)Consider a list of 10 elements of integer values. If the number in the list is divisible by 2, print the
# result as "square of that number minus 2".

# In[23]:


for i in range(10):
   if(i/2):
    print((i*i)-2)


# 5)Consider a list of 10 elements. Print all the elements in the list which are greater than 7 when that
# number is divided 2.

# In[24]:


l=[1,2,3,4,5,6,7,8,9,100]
for i in l:
    if((i/2)>7):
        print(i)
    

