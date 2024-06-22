import random

user_name=input("Enter your name:")
print(f"hello {user_name}")
random="5"
vowel="aeiouAEIOU"
if(user_name[0] in vowel):
   print("Aha...your name begins with vowel")
   Number=input("Select a random number between 1 and 10:") 
   if(Number==random):
     print("YOU WON!!!")
   else:
     print("YOU LOST!!") 
else:
    print("ohhhh...your name begins with consonanat")
    #random_number = random.randint(0, 10)
    Number=input("Select a random number between 1 and 10:") 
    if(Number==random):
     print("YOU WON!!!")
    else:
     print("YOU LOST!!") 


    
 

