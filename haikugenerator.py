import random
def haikuGen():
    short = ["An old silent pond", "splash! Silence again.", "Autumn's nice moonlight", "into the chestnut", "In the twilight rain", "A lovely sunset"]
    long1 = ["A frog jumps into the pond", "a worm digs silently", "these brilliant-hued hibiscus", "Moves west, flowers' shadows", "the color and scent of the wisteria"]

    print(random.choice(short))
    print(random.choice(long1))
    print(random.choice(short))

haikuGen()
