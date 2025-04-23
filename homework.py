import random

#so i imported random but dont worry about that now.
#what you wanna look at is the fruit array. 
#so basically you could make that variable anything.
#the only reason its an array is because we added [] to it.
#you will pick up quick and dont worry to much on understanding everything cuz i gotchu
#ima give you some homework to practice.

#fruit = ["apple", "pear", "orange"]

#arrays start with 0 as the first number so pear is  gonna be 1 and apple is 0.
#the numbers dont mean anything but thats so you know what is what.
#print(fruit[1])


#so def is used to define a function.
#the computer is both retarded and never wrong.
#that means you have to explian every single thing to the computer in order to get anything to work.
#for this function we are gonna call it salad, we are gonna make a loop, and print some vegetables we wanna add to the salad.
#then we will make another salad and let the computer decide what is added with the "import random" we added.

def salad():
    i = 0
    dinner = ["carrots", "lettuce", "onions","ranch dressing"]
    #so pay attention how this is written. 
    # we added a function with "def"
    # we named it "salad"
    #theres a thing called parameters which im to dumb to spell correctly but those go in the ();
    #we do need any because those are usually used with numbers, not always but usually.
    #thats just something to note bro. 
    #anyway we also have an array called dinner.
    #we added "strings", we know they are strings because they have qoutes like "carrots".
    #now we are gonna make a loop.
    for i in range(4):
    #so this is called a for loop.
    #for now dont worry about the "i".
    #what you need to pay attention to is why we used a for loop.
    #its because we know we have 4 elements. 
    #the elements are the vegetables we added in our array.
    #anything in your list or array is your element.
    #we only use for loops when we know we have a handful of numbers that we can keep up with.
        print(dinner[i])
        i = i + 1
#salad()
#okay so this may or may not be confusing but ima break it down.
#so "i" stands for incrimate. just a fancy way of saying we want to count up like 0 1 2 3.
#when we say i = i +1 we are saying i = 0 + 1, i = 1 + 1, i = 2 + 1,etc.
#so in order the for loop says okay so "i" is 0 so ill print dinner[i] which 0 in the list is carrots.
#because an array starts at 0,1,2,3,4. so because it starts at 0 , carrots is 0.
#so we print carrots at 0, lettuce at 1, onions at 2, and ranch at 3, in total thats 4 elements but its only weird cuz in all programming the array always starts at 0 first.
#if you look at the end. we called the function by writing salad(). now if we had parameters we would have to add those as well but thats another lesson bro.



#okay we are gone make a while loop for fun an then ima give you something to try on you own and ill help you with that as well if you need it.
#first you are gonna learn to use a while loop.
def relaxBro():
    chill = random.randint(1,10)
#all we are doing is making a new function called relaxBro.
#then we added a new varible called chill.
#you are getting a super lesson today cuz you are learn to use a method called random.
#a method is a built in function.
#remember they last function we had to make called salad()?
#we python has some for us that we can use and that saves alot of time not having to code those functions.
#anyway, to use them you just have to look them up and then import them by simply typing in "import"
#so random is the built in "function" and the "method" is the ".randint()"
#so the numbers we added are those things called parameters i was talking about.
#this specific one is easy to grasp even though it kinda weird at first, probly really weird but thats why i labeled it chill cuz youll get it fast.
#all the parameters are doing is saying we want a number between 1 and 10, but the catch is we want a random number, not just a number.
#so ima add another variable called smooth and all i wanna do is see which random number wins.
#so ima compare them.
    smooth = random.randint(1,10)
    while chill <= 10:
        print("tig ol bitties")
        if smooth >= chill:
            print("i like to listen to music while coding")
        if smooth == chill:
            print("idk im just making stuff up lol just imagine something")


#relaxBro()
#this code hypothetically could run for hours lol.
#this function uses a while loop, comparison operators, if statements, and methods.
#thats alot if you havent done it before.
#so thats means if you havent then you a re about to level up bro.
#if you complete the next lesson i have a small project for you the next time we talk.

def rocky():
    punch = "punch"
    kick = "kick"
    block = "block"
    ai = [punch,kick,block]
    aiMoves = random.choice(ai)
    player = input("pick punch kick or block: ")
    if aiMoves == player:
        print("same move loser")
    if aiMoves == punch and player == block:
        print("good stuff bro, kick his ass")
    if aiMoves == kick and player == block:
        print("good stuff bro, kick his ass")
    #add more code here to complete the game, idc how it works, make it your own game.
    #make it "cool" or fun. its whatever
    #remove the "else and all the stuff below except the function call"
    else:
        print("finish this game bro, this is your homework")
        print("if you wanna code, alot of it is gonna be working on code people have already built")
        print("you got it bro, add stuff like a score keeper and add a loop for the game")
        print("i know you arent ready for this and thats why i gave you a more difficult task on purpose")
        print("if you need help with this i gotchu but i wanna see you try and i think you will surprise yourself")
        #the rocky() is the function call.
        #you need that for it to work.
        #make a round counter
        #use a while loop for it.
        #use the hash tag on the other code so its commented out and doesnt run.
#rocky()




#lets make rock paper scissors with recursion.
#theres alot of ways to make this game so try making it different if you can.
#im not gonna treat you like a rookie anymore so pay close attention.
#you need to study this hard because the card game we make will be very tricky.

def game():

    def rounds(gameRounds):
        
        if gameRounds == 4:
            print("game end")
            return
        else:
            print(f"Round {gameRounds}")
            gameLogic(gameRounds + 1)
            gameRounds = gameRounds + 1

    def playerChoice():
        player = input("rock paper scissor:    ").lower()
        if player not in ["rock", "paper", "scissors"]:
            print("gotta make a valid choice dude")
            return playerChoice()
        return player
    

    def aiChoice():
        print("thinking...")
        ai = ["rock", "paper", "scissors"]
        fate = random.choice(ai)
        print(f"AI chose: {fate}")
        return fate
            
            
    def gameLogic(currentRounds):
        player = playerChoice()
        ai = aiChoice()

        if player == ai:
            print("its a tie")
            

        elif player == "rock" and ai == "scissors" or player == "paper" and ai == "rock" or player == "scissors" and ai == "paper":
            print("player wins that round\n")
            
        else:
            print("ai wins that round\n")
            

        rounds(currentRounds)
        



    rounds(1)

game()


#