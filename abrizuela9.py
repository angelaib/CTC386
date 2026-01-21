
#Angela Brizuela
#lab 8 copied to lab 9
#GitHub test comment

#functinos go here

def TempConv(f):
    C = (f - 32) * (5/9)
    return C


name = str(input("What's your name?"))

print("Hi,", name,"choose an option below")

print("Menu")
print("*_*_*_*_*_")
print("option 1: joke")
print("option 2: username")
print("option 3: quote")
print("option 4: Guess a number")
print("option 5: F to C conversion")
print("_________")

option = int(input("choose an option"))
if option == 1:
    print("A man walks into a bar... OUCH")
elif option == 2:
    name = input("enter your  name:")
    for i in range (15):
        print(name)
elif option == 3:
    x = int(input("enter a number:"))
    for i in range(x):
        print("Just do it")
elif option == 4:
    number = 3

    guess = int(input("Guess a number between 0 -100 "))
    
    while guess != number:

        if guess < 0 or guess > 100:
            print("your guess is out of range guess again")
        elif guess < number:
            print("your guess is too low, try again")
        else:
            print("your guess is too high, try again")

        guess = int(input("guess a number between 0 - 100"))

    print("you won! correct!")

elif option == 5:

    print("lets calculate the current farenheight temperature into celcius")
    f = int(input("tell me the current temperature in degrees farenheight"))

    output = TempConv (f)

print("the current temp is, ", output)

