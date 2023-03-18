#!/usr/bin/env python
# coding: utf-8

# ### 1. What are the characteristics of the tuples? Is tuple immutable?

# Ans:
# 1. Tuples are immutable
# 2. Tuples can contain elements of different data types
# 3. Tuples are indexed
# 4. Tuples are faster than lists

# ### 2. What are the two tuple methods in python? Give an example of each method. Give a reason why tuples have only two in-built methods as compared to Lists. 

# Ans: 
# 
# Tuple have 2 in-built methods:
#         1. count() method
#         2. index() method
# 
# count() method example:

# In[5]:


t = (1, 2, 3, 4, 2, 5, 2)
count_2 = t.count(2)
count_2


# index() method example:

# In[7]:


t = (1, 2, 3, 4, 2, 5, 2)
index_2 = t.index(2)
index_2


# Reason because tuples have only two in-built methods as compared to lists is that tuples are immutable, whereas lists are mutable.

# ### 3. Which collection datatypes in python do not allow duplicate items? Write a code using a set to remove duplicates from the given list.
# #### List = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]

# Ans:
#     
# 1. Set and Collection does not allow duplicate items

# In[2]:


original_list = [1, 1, 1, 2, 1, 3, 1, 4, 2, 1, 2, 2, 2, 3, 2, 4, 3, 1, 3, 2, 3, 3, 3, 4, 4, 1, 4, 2, 4, 3, 4, 4]
unique_set = set(original_list)
new_list = list(unique_set)
print(new_list)


# ### 4. Explain the difference between the union() and update() methods for a set. Give an example of each method.

# union() method returns a new set that contains all the unique elements of the original sets.
# update() method adds all the unique elements of one set to another set.

# In[9]:


# Example of union() method
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3) 

# Example of update() method
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set1.update(set2)
print(set1) 


# ### 5. What is a dictionary? Give an example. Also, state whether a dictionary is ordered or unordered.

# 1. Dictionary is a collection data type that stores key-value pairs.

# In[13]:


my_dict = {"apple": 1, "banana": 2, "orange": 3}
my_dict


# ### 6. Can we create a nested dictionary? If so, please give an example by creating a simple one-level nested dictionary.

# - Yes, we can create a nested dictionary in Python

# In[15]:


person = {
    'name': 'John',
    'age': 30,
    'address': {
        'street': '123 Main St',
        'city': 'Anytown',
        'state': 'CA',
        'zip': '12345'
    }
}

print(person['address']['city'])


# ### 7. Using setdefault() method, create key named topics in the given dictionary and also add the value of the key as this list ['Python', 'Machine Learning’, 'Deep Learning']

# In[17]:


dict1 = {'language' : 'Python', 'course': 'Data Science Masters'}
dict1.setdefault('topics', ['Python', 'Machine Learning', 'Deep Learning'])
dict1


# ### 8. What are the three view objects in dictionaries? Use the three in-built methods in python to display these three view objects for the given dictionary.
# #### dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

# ANS:
# 
# Python, there are three types of view objects that can be created from a dictionary:
# 1. dict_keys
# 2. dict_values
# 3. dict_items 

# In[21]:


dict1 = {'Sport': 'Cricket' , 'Teams': ['India', 'Australia', 'England', 'South Africa', 'Sri Lanka', 'New Zealand']}

print("dict_keys view object:", dict1.keys())
print("dict_values view object:", dict1.values())
print("dict_items view object:", dict1.items())


# In[ ]:




