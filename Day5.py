fruits = ['Apple', 'Peach','Pear']
for fruit in fruits:
    print(fruit)

    import random

# letters=['a','b','c','d','e','f','l','m','n','A','B','C','D','E','F','L','M','N']
# numbers=['1','2','3','4','5','6','7','8','9','0']
# characters=['*','%','$','&','@','!','#']

# pwd=[]

# let=int(input("How many letters do you want?\n"))
# num=int(input("How many numbers do you want?\n"))
# charac=int(input("How many characters do you want?\n"))

# for i in range(let):
#     pwd.append(random.choice(letters))

# for i in range(num):
#     pwd.append(random.choice(numbers))

# for i in range(charac):
#     pwd.append(random.choice(characters))

# random.shuffle(pwd)

# pwd= ''.join(pwd)
# print(pwd)



name=str(input("Enter your name: "))
num=str(input("Enter your fav number: "))

name1=random.choice(name)
name2=random.choice(name)

print("Random letters are :", name1,name2)

num=random.choice(num)

pwd=print("Your random thing is : ", name1+name2+num)
random.shuffle(pwd)
print(pwd)
