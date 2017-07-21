import random
def nameGen():
    name1 = ["Chris' ", "Brittany's ", "Brandon's ", "Maddi's ", "Jen's ", "Matt's ", "Anna's ", "Courtney's ", "Hannah's ", "Falou's " ]
    adj = ["awesome ", "amazing ", "crazy ", "luxurious ", "wild "]
    place = ["restaurant", "office", "bistro", "cafe", "spot"]

    print(random.choice(name1) + random.choice(adj) + random.choice(place))
    
    def nameGen():
    adj = ["awesome ", "amazing ", "crazy ", "luxurious ", "wild "]
    place = ["restaurant", "office", "bistro", "cafe", "spot"]

    print("What's your name?")
    name = input()
    print(name + "'s " + random.choice(adj) + random.choice(place))

nameGen()

nameGen()
