#!/usr/bin/env python
# coding: utf-8

# 1)Write a Python program to find the first 20 non-even prime natural numbers.
# 

# In[11]:


for i in range (1,20,3):
    if(i%2!=0):
        print(i)


# 2)Write a Python program to implement 15 functions of string.

# In[16]:


txt="50800"
x=txt.isdigit()
print(x)


# 3)Write a Python program to check if the given string is a Palindrome or Anagram or None of them.
# Display the message accordingly to the user.

# In[21]:


s1= "mom"
s2= "code"
s3= "sriraaga"
s4=  reversed(s1)
if list(s1)==list(s4):
    print("the string is palindrome ")
elif (sorted(s2)==sorted(s3)):
    print("the strings are anagram")
else:
    print("none of them")


# 4)Write a Python's user defined function that removes all the additional characters from the string
# and converts it finally to lower case using built-in lower(). eg: If the string is "Dr. Darshan Ingle
# @AI-ML Trainer", then the output be "drdarshaningleaimltrainer".

# In[22]:


text='SRIRAAGA'
print(text)
print(text.lower())


# In[23]:


def replace_character(y):
    special_char=["@",".","-"]
    for c in special_char :
        y=y.replace(c," ")
        y=y.lower()
        print("resultant string",y)
string1="Dr.Darshan ..."
replace_character(string1)


# Given a string, convert the characters of the string into opposite case,i.e. if a character is lower case than convert it into upper case and vice-versa.
# 
# ASCII values  of alphabets: A – Z = 65 to 90, a – z = 97 to 122
# 
# Steps:
# 1.Take one string of any length and calculate its length.
# 2.Scan string character by character and keep checking  the index .
# 3.If character in a index is in lower case, then subtract 32 to convert it in upper case, else add 32 to convert it in lower case
# 4.Print the final string.
# 
