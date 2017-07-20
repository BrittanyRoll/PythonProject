start = '''


print(start)
''' You are a traveler. A person in a trenchcoat walks up to you with his face hidden and offers you two plane tickets. You stare at him, confused. "Pick one!" he growls. Which ticket do you take: ticket A or ticket B? '''

print("Type 'ticket A' or 'ticket B'.)
user_input = input()
if user_input == "ticket A":
    print("You decide to pick ticket A and your destination is... the Galapagos Islands!")
    print("After you board the plane, you sleep through a long flight on a tiny plane. When you arrive--although you have your backpacking supplies--the sudden realization that you have nowhere to stay hits you.")
    print("You exit the airport after converting most of your money to the local currency. You realize that you can either spend all of your money on a hotel, or camp out in the wilderness somewhere. What do you do?")
    print ("Type 'hotel' or 'wilderness' to choose.")
    user_input = input()
    if user_input == "hotel":
        print("You walk into a shabby hotel and pay for the only room available: room number 13. As you look around the room, you gulp: paint is peeling off the walls, the bed is hastily made, and the floor is covered with a thick layer of dust.")
        print("A shady-looking concierge comes up to you with a cheesy smile, and holds out a brochure to you. 'Would you like to go on an all-day expedition? It would be perfect for the likes of you--a worldwide traveler, I see!' Do you take the expedition or do you reject it?")
        print("Type 'accept' to accept the expedition-- with the little money you have left-- or type 'reject' to reject it.")
        user_input = input ()
        if user_input == "accept":
            print("The next day, you arrive at the location... but then your heart sinks. You were scammed. You knew it! There is nothing around except for dense rainforest all around a clearing, and you decide you're done with traveling for a while. Anyway, you think, I don't have any money left.")
            print("END GAME")
        elif user_input == "reject":
            print("You reject the offer; something about this concierge seems a little off to you. As soon as you get back to your room and connect to the slow (but free) wifi, you realize that was a smart choice, as the expedition agency has terrible reviews.")
            print("When you get up the next morning, bright and early, you decide to spend the whole day out hiking and walking everywhere. As it nears noon, you decide to go snorkeling in the beautiful coral reefs with the equipment you carry. You see all kinds of multicolored fish... but you don't see the huge shark behind you...")
            print("END GAME")
        else:
            print("Sorry, that isn't an option!")
    elif user_input == "wilderness":
        print("Aside from a few houses and the airport, everything else is completely isolated. You walk around-- but there is only the natural beauty of the island around you. Tall, rugged peaks are raised to your right, while a sliver of turquoise ocean stretches out in the far distance. As you walk around, your legs start to ache terribly and your throat feels dryer than a desert. You realize that you either have to start looking for food/ water, or start looking for shelter. What do you choose?")
        print("Type 'food/water' or 'shelter' to decide.")
        if user_input == "food/water":
            print("Parched, you decide to go look for a river nearby so you can get water at the very least, as you've emptied out your canteen since exiting the airport.")
            print("After an hour of searching in the blazing sun, you spot a tiny stream. Your heart leaps. Water, at last! You run as fast to the cool, clear water as you can... but in your hurry, you slip on the muddy banks and fall facefirst into the stream, and hit your head on a rock in the gushing water, and lose consciousness...")
            print("END GAME")
        elif user_input == "shelter":
            print("You're thirstier than you've ever been in your life, but you know that you need to find a sheltered place to rest before your legs collapse. Finally, you find a cool, dark cave under a thick grove of palm trees. You walk in, not knowing that the cave is the home of a bear...")
        else:
            print("Sorry, that isn't an option!")
    else:
         print("Sorry, that isn't an option!")
elif user_input == "ticket B":
    print("This part of the story coming soon!")
else:
    print("Sorry, that isn't an option!")

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
        print("Try again")
