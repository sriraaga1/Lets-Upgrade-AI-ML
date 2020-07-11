#!/usr/bin/env python
# coding: utf-8

# 1)Write a program to subtract two complex numbers in Python

# In[1]:


a=2+4j
b=1+2j
print("subtraction is:",(a-b))


# 2)Write a program to find the fourth root of a number

# In[2]:


a=4
p=pow(a,(0.25))
print(p)


# 3) Write a program to swap two numbers in Python with the help of a temporary variable

# In[3]:


x = 5
y = 10

temp = x
x = y
y = temp

print("The value of x after swapping: ",x)
print("The value of y after swapping: ",y)


# 4) Write a program to swap two numbers in Python without using a temporary variable

# In[4]:


x = 5
y = 7  
print ("Before swapping: ") 
print("Value of x : ", x, " and y : ", y)  
x, y = y, x 
print ("After swapping: ") 
print("Value of x : ", x, " and y : ", y) 


# 5) Write a program to convert fahrenheit to kelvin and celsius both

# In[6]:


def Fahrenheit_to_Kelvin(F): 
   return 273.5 + ((F - 32.0) * (5.0/9.0)) 
  
F = 100
print("Temperature in Kelvin ( K ) = {:.3f}" 
           .format(Fahrenheit_to_Kelvin( F ))) 
   


# 6) Write a program to demonstrate all the available data types in Python. Hint: Use type() function.
# 

# In[5]:


a= 5
print(a, "is of type", type(a))

b= 2.0
print(b, "is of type", type(b))

c = 1+2j
print(c, "is of type", type(c))


# 7) Create a Markdown cell in jupyter and list the steps discussed in the session by Dr. Darshan Ingle sir to create Github profile and upload Githubs Assignment link.

# __Markdown is a lightweight and popular Markup language which is a writing standard for data scientists and analysts.it is ofent converted into the corrosponding HTML which by the Markdown processor which allowsit to be easily shared between different devices and people__.
# 
# Markdown cell syntaxehich is supported by Jupyter Notebook are:
# 
# #1) Headings
# 
# The heading starts with "#," i.e., hash symbol followed by the space, and there are six Headings with largest heading only using one hash symbol and the smallesttitiles using six hash symbols.
# 
# # (Header 1 ,title)
# ## (Header 2, major headings)
# ### (Header 3, subheadings)
# #### (Header 4)
# ##### (Header 5)
# ###### (Header 6)
# 
# # 2)Bold and italic Text
# You can use tags, '**' i.e 'double asterisk' or '__' i.e.
# 
# **hi
# 
# 
# 
# 
# 

# __HOW TO CREATE THE GITHUB PROFILE AND UPLOAD GITHUB'S ASSIGNMENTS LINK__
# __STEP:1 Open Github in the browser and sign up to the github and create an account.
# __STEP:2 After creating the account now we should create a repository.
# __STEP :3 Create the repositopry and files,we should upload the files by drag and drop method.
# 
