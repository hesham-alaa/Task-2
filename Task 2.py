#!/usr/bin/env python
# coding: utf-8

# # Question 1:
# Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.
# 
# Hints:
# 
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.

# In[37]:


d={}
i1=1
i2=2
i3=3
d[i1]=(i1**2)
d[i2]=(i2**2)
d[i3]=(i3**2)
print(d)


# # Question 2:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the values only.
# 
# Hints:
# 
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
# 

# In[23]:


d={}
for t in range(1,21) :
    d[t]=t**2
print(d)


# # Question 3:
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.
# 
# Hints:
# 
# Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.
# 

# In[6]:


d={}
for s in range(1,21):
    d[s]=s**2
    
print(d.keys()) 


# # Question 4 
# Write a Python program to check a dictionary is empty or not

# In[7]:


d={}
len(d)


# # Question 5
# 
# Write a Python program to test whether every element in s is in t and every element in t is in s.
# 
# 

# In[16]:


sets = set(["cold","hot"])
sett= set(["hot","cold"])
print("s =",sets)
print("t=",sett)
print(sets<= sett)
print(sets.issubset(sett))
print("s =",sets)
print("t=",sett)
print(sett<=sets)
print(sett.issubset(sets))


# # Question 6
# Create set 1 and set 2 then 
# Write a Python program to 1- create an intersection of sets.
# 2-  a union of sets.
# 3- create set difference.
# 4- a symmetric difference.

# In[26]:


seta={1,2,3,4,5}
setb={7,6,5,4,3}
print("intersection (a&b)  =",seta.intersection(setb))
print("union (a|b) = ",seta.union(setb))
print("difference(a-b) =",seta.difference(setb))
print("difference(b-a) =",setb.difference(seta))
print("symmetric difference (a^b) = ",seta.symmetric_difference(setb))


# # Question  7
# Write a Python program to use of frozensets.

# In[29]:


set1={1,2,3,5,7,9,0}
set1= frozenset(set1)
print("set1 =",set1)


# # Question 8
# Write a Python program to find maximum and the minimum value in a set.

# In[31]:


set1={1,2,3,5,7,9,0}
print("max of set1 =", max(set1))
print("min of set1 =", min(set1))


# # Question9 :
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line. 
# 
# Hints:
# 
# Use [n1:n2] notation to get a slice from a tuple.

# In[51]:


tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)


# # Question 10 :
# You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
# 
# Hints:
# In case of input data being supplied to the question, it should be assumed to be a console input.
# We use itemgetter to enable multiple sort keys.
# 
# Solutions:
# from operator import itemgetter, attrgetter
# 

# In[ ]:





# # Question 11:
# 
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.
# 
# 
# 
# Hints:
# Use random.sample() to generate a list of random values.

# In[61]:


l=[100,111,145,178,150,120,190,200]
print(random.sample(l,5))


# # Question 12
# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.
# 
# Hints:
# Use random.sample() to generate a list of random values.

# In[106]:


resp = random.sample(range(100,201,2),5)
print(resp)


# # Question 13
# Please write a program to randomly print a integer number between 7 and 15 inclusive.
# 
# Hints: Use random.randrange() to a random integer in a given range.
# 
# 

# In[111]:


print(random.randrange(7,15,1))


# # Question 14
# 
# Please write a program to print the running time of execution of "1+1" for 100 times.
# Hints:
# Use timeit() function to measure the running time.
# 

# In[140]:


import timeit
s='1+1'
s=str(s)
print(s*100)
print(timeit.timeit(s*100))


# # Question 15 :
# 
# Please write a program to shuffle and print the list [3,6,7,8].
# 
# Hints:
# Use shuffle() function to shuffle a list.
# 

# In[22]:


from random import shuffle
list1 = [3,6,7,8]
random.shuffle(list1)
print(list1)


# In[ ]:




