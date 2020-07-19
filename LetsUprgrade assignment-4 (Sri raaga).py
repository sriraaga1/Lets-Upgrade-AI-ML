#!/usr/bin/env python
# coding: utf-8

# 1)Assuming that we have some email addresses in the "username@companyname.com" format, please write program
# to print the company name of a given email address. Both user names and company names are composed of letters
# only.
# 
# Input Format:
# The first line of the input contains an email address.
# Output Format:
# Print the company name in single line.
# Example;
# Input:
# john@google.com
# Output:
# google

# In[4]:


a="username@sriraaga.com"
print(a[9:17])


# 2)Write a program that accepts a comma-separated sequence of words as input and prints the words in a comma
# separated sequence after sorting them alphabetically.
# 
# Input Format:
# The first line of input contains words separated by the comma.
# Output Format:
# Print the sorted words separated by the comma.
# Example:
# Input:
# without,hello,bag,world
# Output:
# bag,hello,without,world

# In[15]:


a=["zebra","strawberry", "air", "bugs"]
a.sort()
print(a)


# 3)Create your own Jupyter Notebook for Sets

# In[16]:


thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)


# In[17]:


thisset = {"apple", "banana", "cherry"}

thisset.update(["orange", "mango", "grapes"])

print(thisset)


# In[18]:


thisset = {"apple", "banana", "cherry"}

print(len(thisset))


# In[19]:


thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


# In[21]:


thisset = {"apple", "strawberry", "mango"}

thisset.discard("apple")

print(thisset)


# In[22]:


thisset = {"fasion", "skincare", "makeup"}

x = thisset.pop()

print(x)

print(thisset)


# In[23]:


thisset = {"blogging", "cooking", "travelling"}

thisset.clear()

print(thisset)


# In[24]:


thisset = {"dance", "music", "art"}

del thisset

print(thisset)
#The del keyword will delete the set completely


# In[25]:


set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


# In[27]:


set1 = {"x", "y" , "z"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


# 4)Given a list of n-1 numbers ranging from 1 to n, your task is to find the missing number. There are no duplicates.
# Input Format:
# 
# The first line contains n-1 numbers with each number separated by a space.
# Output Format:
# Print the missing number
# Example:
# Input:1 2 4 6 3 7 8
# Output:5
# Explanation:
# In the above list of numbers 5 is missing and hence 5 is the input
# 

# In[41]:



mylist = [1,2,3,4,6,7,8,9]
for x in range(1, len(mylist)):
    if x not in mylist:
        print(x, "is missing")
        break       


# 5)With a given list L, write a program to print this list L after removing all duplicate values with original order reserved. Example:
# 
# If the input list is 
# 12 24 35 24 88 120 155 88 120 155 
# 
# Then the output should be 
# 12 24 35 88 120 155
# 
# 
# Explanation: Third, seventh and ninth element of the list L has been removed because it was already present.
# Input Format:
# 
# In one line take the elements of the list L with each element separated by a space. 
# Output Format:
# 
# Print the elements of the modified list in one line with each element separated by a space.
# Example: 
# 
# Input: 12 24 35 24 Output: 12 24 35
# 
# 

# In[49]:


list1 = [10, 20, 10, 20, 30, 40, 30, 50]
list2 = []
for n in list1:
    if n not in list2:
        list2.append(n)

print ("List after removing duplicate elements")
print( "list2: ", list2)

