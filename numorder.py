lis = [23, 1, 4, 2, 1000, 10, 5, 50, 51, 20, 16, 17]

def switch():
    for z in range(len(lis)):
        b = 0
        for x in range(len(lis)-1):
            print( "x:", x , "b:", b )
            if lis[x] > lis[x+1]:
                y = lis[x]
                lis[x] = lis[x+1]
                lis[x+1] = y
                b += 1
    print(lis)

li = [1, 4, 6, 8, 9, 10]
def find():
    print("Give me a number. See if it's in the list.")
    user_input = int(input())
    x = int((0 + len(li))/2)

    if user_input == li[x]:
        print("Your Number is Here!")

    elif user_input < li[x]:
        print("Not Yet")
        y = int((x + 0)/2)

        if user_input == li[y]:
            print("Your Number is Here!")

        elif user_input < li[y]:
            print("Not Yet")
            a = int((y+0)/2)

        elif user_input > li[y]:
            print("Not Yet")
            b = int((y+ len(li))/2)


    elif user_input > li[x]:
        print("Not Yet")
        z = int((x + len(li))/2)

        if user_input == li[z]:
            print("Your Number is Here!")

        elif user_input < li[z]:
            print("Not Yet")
            c = int((z+0)/2)

        elif user_input > li[z]:
            print("Not Yet")
            d = int((z + len(li))/2)





l = [1, 4, 6, 8, 9, 10]

def search():
    start = 0
    end = len(l)-1
    user_input = int(input())

    while ((end - start) >= 1):
        midpoint = int((start+end)/2)
        if user_input == l[midpoint]:
            print("Your Number is Here!")
            break
        elif user_input > l[midpoint]:
            start = midpoint
        elif user_input < l[midpoint]:
            end = midpoint

switch()
search()
