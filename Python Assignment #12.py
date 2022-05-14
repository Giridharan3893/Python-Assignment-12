#!/usr/bin/env python
# coding: utf-8

# In[3]:


## Answer 1:

def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
       
tups = [("giri", 10), ("hari", 12), ("anand", 14), 
     ("babu", 20), ("karthi", 25), ("sathish", 30)]
dictionary = {}
print (Convert(tups, dictionary))


# In[5]:


## Answer 2:

from collections import Counter
 
def makeString(str1,str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)

    result = dict1 & dict2

    return result == dict1

if __name__ == "__main__":
    str1 = 'ABHISHEKsinGH'
    str2 = 'gfhfBHkooIHnfndSHEKsiAnG'
    if (makeString(str1,str2)==True):
        print("Possible")
    else:
        print("Not Possible")


# In[7]:


## Answer 3:

from collections import Counter
  
def allSame(input):
      
    dict=Counter(input)
    same = list(set(dict.values()))
  
    if len(same)>2:
        print('No')
    elif len (same)==2 and same[1]-same[0]>1:
        print('No')
    else:
        print('Yes')
        
if __name__ == "__main__":
    input = 'xxxyyzzt'
    allSame(input)


# In[8]:


## Answer 4:

import requests
def getWords():
    url = "http://www.puzzlers.org/pub/wordlists/unixdict.txt"
    fetchData = requests.get(url)
    wordList = fetchData.content
    wordList = wordList.decode("utf-8").split()  
    return wordList
def isOrdered():
    collection = getWords()
    
    collection = collection[16:]
    word = ''
  
    for word in collection:
        result = 'Word is ordered'
        i = 0
        l = len(word) - 1
  
        if (len(word) < 3): # skips the 1 and 2 lettered strings
            continue
        while i < l:         
            if (ord(word[i]) > ord(word[i+1])):
                result = 'Word is not ordered'
                break
            else:
                i += 1
        if (result == 'Word is ordered'):
            print(word,': ',result)
            
if __name__ == '__main__':
    isOrdered()


# In[9]:


## Answer 5:

def charCount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict
  
  
def possible_words(lwords, charSet):
    for word in lwords:
        flag = 1
        chars = charCount(word)
        for key in chars:
            if key not in charSet:
                flag = 0
            else:
                if charSet.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            print(word)
  
if __name__ == "__main__":
    input = ['goo', 'bat', 'me', 'eat', 'goal', 'boy', 'run']
    charSet = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
    possible_words(input, charSet)


# In[11]:


## Answer 6:

test_dict = {'RCB' : [4, 5], 'is' : [8], 'best' : [10, 12]}

print("The original dictionary : " + str(test_dict)) 
val_list = [5, 10]
temp = {}
for key, vals in test_dict.items():
    for val in vals:
        temp[val] = key
res = [temp[ele] for ele in val_list]
print("The keys mapped to " + str(val_list) + " are : " + str(res)) 


# In[13]:


## Answer 7:

import sys

Tuple1 = ("A", 1, "B", 2, "C", 3)
Tuple2 = ("Giri", "Hari", "Giri2", "Sasi", "Giri3", "Babu")
Tuple3 = ((1, "Lion"), ( 2, "Tiger"), (3, "Fox"), (4, "Wolf"))

print("Size of Tuple1: " + str(sys.getsizeof(Tuple1)) + "bytes")
print("Size of Tuple2: " + str(sys.getsizeof(Tuple2)) + "bytes")
print("Size of Tuple3: " + str(sys.getsizeof(Tuple3)) + "bytes")


# In[14]:


## Answer 8:

test_tup = (5, 20, 3, 7, 6, 8)
print("The original tuple is : " + str(test_tup))

K = 2

res = []
test_tup = list(sorted(test_tup))
 
for idx, val in enumerate(test_tup):
    if idx < K or idx >= len(test_tup) - K:
        res.append(val)
res = tuple(res)

print("The extracted values : " + str(res))


# In[15]:


## Answer 9:

list1 = [1, 2, 5, 6]
res = [(val, pow(val, 3)) for val in list1]
print(res)


# In[16]:


## Answer 10:

test_list = [5, 6, 7]
print("The original list is : " + str(test_list))
test_tup = (9, 10)
test_list += test_tup
print("The container after addition : " + str(test_list))


# In[17]:


## Answer 11:

test_list = [(3, 4), (78, 76), (2, 3), (9, 8), (19, 23)]
print("The original list is : " + str(test_list))
tup = (17, 23)
K = 1
min_dif, res = 999999999, None
for idx, val in enumerate(test_list):
    dif = abs(tup[K - 1] - val[K - 1])
    if dif < min_dif:
        min_dif, res = dif, idx
        
print("The nearest tuple to Kth index element is : " + str(test_list[res])) 

