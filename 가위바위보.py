import random
com = random.randint(1,3)
user = int(input('가위=1,바위=2,보=3'))
print("com({}):user({})".format(com,user))

if com == user:
    print("draw")
    
elif(com==1 and user==3):
    print("win")

elif(com==1 and user==2)
    
else:
    print("incorrect")
