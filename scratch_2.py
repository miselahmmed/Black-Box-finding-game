print("Welcome to black box finding game")

q1= input("Left or right?").lower()
if q1 == "left":
    q2 = input("swim or wait?").lower()
    if q2== "wait":
        q3 = input("red,blue, yellow?").lower()
        if q3 == "blue":
            print("you win the game, you have the box")
        else:
            print("game over")
    else:
        print("game over")
else:
    print("game over")