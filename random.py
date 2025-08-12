import random

IsHappy = random.choice([True, False]) #random happiness
print("happy? ", IsHappy)
if IsHappy:
    print("You are happy!")
else:
    print("You are not happy!")
    
age = random.randint(16,25) #random age
print("age? ", age)

if age>17:
    print("unc")
else:
        print("yung")
        
name = random.choice(["scooby", "dave", "gabe"]) #random name
print("name? ", name)

if name == "scooby":
    print("you're scooby!")
else:
        print("you're not scooby!")
        
float = random.random() #random float
print("how much? ", float)

if float<0.5:
    print("lil float")
else:
        print("big float")