import random
play = True
study = str(random.randint(10,20))
print("guess a number unti you get it right from 10 to 20")
while play:
    n = input("guess the number")
    if  n == study:
        print("number is correct")        
        break
    else:
        print("that is not the number guess aggain") 
        break
   
     