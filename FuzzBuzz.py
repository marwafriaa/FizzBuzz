#!/usr/bin/env python
# coding: utf-8

# In[13]:


def fizzbuzz(nb):
    for i in range(nb):
        if verify_mult(i,3) and verify_mult(i,5):
            print("fizzbuzz")
            continue
        elif verify_mult(i,3) :
            print("fizz")
            continue
        elif verify_mult(i,5):
            print("buzz")
            continue
        
        print(i)
    
        
def verify_mult(a,b):
     if a % b == 0:
        return True
     else:
        return False

    

    


# In[14]:

def main():
    fizzbuzz(100)


# In[6]:





# In[ ]:




