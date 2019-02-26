#!/usr/bin/env python
# coding: utf-8

# In[13]:

# Fizzbuzz verifications and prints , the parameter nb is the number of iterations we want to get
def fizzbuzz(nb):
    for i in range(nb):
        # To verify if i is a maltiple of 3 and 5
        if verify_mult(i,3) and verify_mult(i,5):
            print("fizzbuzz")
            continue
         # To verify if i is a maltiple of 3 
        elif verify_mult(i,3) :
            print("fizz")
            continue
         # To verify if i is a maltiple of 5
        elif verify_mult(i,5):
            print("buzz")
            continue
        # Else we print i
        print(i)
    
 # Verify if the a is a multiple of b        
def verify_mult(a,b):
     if a % b == 0:
        return True
     else:
        return False

    

    


# In[14]:
# main function to run to test
def main():
    fizzbuzz(100)


# In[6]:





# In[ ]:




