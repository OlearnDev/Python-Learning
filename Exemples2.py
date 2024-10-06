

# age=15

# if age>= 19:
# 	print("Vous etes adulte !")
# elif 14<age< 19:
# 	print("Vous etes adolescent !")
# elif 5<age< 14:
# 	print("Vous etes encore enfant !")
# else:
# 	print("Vous etes un bébé !")
 
# for i in range(10):
#     print((i+1)**2)
    
l=["Ted", 34, True, range(15)]

print(l)
# print(l[0])

for i in l:
    if type(i) == str:
        print(i.upper())
    elif type(i) == int:
        print(i**2)
    else:
        print(i)