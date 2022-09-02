a=int(input("무슨 그림을 그릴겁니까? \n1. 삼각형 \n2. 사각형 \n"))
b=int(input("크기는? 1~10까지 \n"))
i=1

if a == 1:
    for i in range (b):
        print("* "*(i+1)+"  "*(b-i-1))

    


if a == 2:
    for i in range (b):
        print("* "*b)

        


