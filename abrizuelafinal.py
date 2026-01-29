#final question 1

print("Hello!")

print("option 1")
print("option 2")
print("option 3")

option = int(input("pick one of these options"))

if option == 1:
    name = str(input("what's your name?"))
    print("Never gonna give you up, never gonna let you down, never gonna turn around and desert you", name)
elif option == 2:
    for i in range(20):
        print("pizza")
elif option == 3: 
    number = 0 
    guess = int(input("Guess a number between 0-10"))

    while guess != number:
        if guess <0 or guess> 10:
            print("your guess is out of range")
        else:
            print ("no, sorry,try again")
        guess = int(input("Guess again, between 0 - 10"))
    print("you won! thats the number")
