start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''


print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You decide to go left and...") # finished the story by writing what happens
#my code starts here
elif user_input == "ticket B":
    print("You choose ticket B. Your destination is...Egypt!")

    print("You've just landed in Europe after a grueling 10 hours and you're really tired. Do you want to go with the person holding a sign with your name or hail a cab? (type 'person' or 'cab' to choose)")
    user_input = input()
    if user_input == "person":
        print("You choose to go with the mysterious driver! You get into the car and the person asks where you want to got. Do you go to a hotel or do you go to the pyramids? (type 'hotel' or 'pyramids' to choose)")
        user_input = input()
        if user_input == "hotel":
            print("You choose hotel! You go to lay down in the hotel and take a nap in a really nice suite. When you wake up, all of your stuff is gone, including your phone and you wallet.")
            print("Game Over!")

        elif user_input == "pyramids":
            print("You choose pyramids! You arrive by the pyramids and you see a food stand. You haven't eaten since you left your house. Do you go to get food or go to take pictures by the monument? (type 'food' or 'pictures')")
            user_input = input()
            if user_input == "food":
                print("You go to get food, but when you reach into your pocket, you realize that all of your money is gone. Oh No! You can't get home!")
                print("Game Over!")
                #Game Over
            elif user_input == "pictures":
                print("You put your stuff on the ground and ask some one to take a picture. You got to pose and when you turn around, the person and all of your stuff is gone! You can't get home!")
                print("Game Over!")
            else:
                if user_input != "food" or "pictures":
                    print("Try again!")

        else:
            if user_input != "hotel" or "pyramids":
                print("Try again")


    elif user_input == "cab":
        print("The cab driver seems angry as you open the door and gruffly asks where you want to go. Do you say you want to go to the nearest hotel or a random destination? (type 'hotel' or 'random destination' to choose)")
        user_input = input()
        if user_input == "hotel":
            print("You arrive at a rundown hotel and are able to book a room. You are really tired, so you take a nap. When you wake up, all of your stuff is gone and you are now stuck in Egypt. What will you do now?")
            print("Game Over!")
        elif user_input == "random destination":
            print("You are driven to the Nile and are told to get on a raft. You get on and end up stuck in the middle of the river. You try to swim to land, but you drown.")
            print("Game Over!")
        else:
            if user_input != "hotel" or "random destination":
                print("Try again")

    else:
        if user_input != "person" or "cab":
            print("Try again")

else:
    if user_input != "left" or "ticket B":
        print("Try again")
