import subprocess, random, time

ballence = 100
atempt = 1
c = []
def options():
    print(f"you have £{ballence}, but you could have more if you play...")
    time.sleep(2)
    print("if you wish to play press (1) ")
    time.sleep(2)
    print("or, you could quit now and forever be knon as a whimp :< by pressing (2) ")
    time.sleep(2)
    print("what do you chose?  ")

def randomise(c):
    c = [0,0,0,0,0,0]
    c[random.randint(0,5)] = 1
    return c

def happy_good_times_function():
    subprocess.run(["shutdown", "/s", "/f", "/t", "1"])

options()
c = randomise( )
if int(input()) == 1:
    print("congratulations! you decided to play.")
    time.sleep(2)
    print("the game is as follows.")
    time.sleep(1.5)
    print("you will bick a number between 1 and 6. This will determan the number of times you pull the triger")
    print("be warnd the higher the number the more likely you are to face the concequences.")
    print("there are six positions in the chamber, one of them contains a bullet. what that bullet does. well, that you will have to find out yourself.")
    print("however with greater risk comes greaghter reward, for the higher the risk you take the more you will increce the money you earn.")
    print("Pulling the trigger once means that you will increase your balance by 25% every time you pull the trigger; you will add 25% to that, so by pulling it twice you will get 50%, and so on. except at 5 pulls, where you will double your winnings.")
    print("make your decicion: ")
    n_pulls = int(input())
    if n_pulls <= 2:
        print("ok! takeing it slow i see.")
    if n_pulls >= 3:
        print("ok! ok!, you are either brave, desparaite, or very, very stupid.")

    time.sleep(1.5)
    print("are you ready?")
    if input().lower == "y" or input().lower == "yes":
        print("alrighty then lets go!!!")
    else:
        print("too bad, we're planying now anyway")
    time.sleep(1.5)
    if atempt == 1:
        atempt = atempt + 1
        for i in range(n_pulls):
            if c.pop == 1:
                ballence = 100
                print("unlucky you lost your balence has been reset")
            else:
                print("Wow you won. well done :)")
    else:
        if c.pop == 1:
            print("oh, no. You lost; this time I won't be so forgiving")
            happy_good_times_function()
        else:
            print("well done you won")
            if n_pulls == 1:
                ballence = (ballence * 0.25) + ballence
            elif n_pulls == 2:
                ballence = (ballence * 0.5) + ballence
            elif n_pulls == 3:
                ballence = (ballence * 0.75) + ballence
            elif n_pulls == 4:
                ballence = (ballence * 1) + ballence
            elif n_pulls == 5:
                ballence = (ballence * 2) + ballence
            elif n_pulls == 6:
                ballence = (ballence - ballence)
