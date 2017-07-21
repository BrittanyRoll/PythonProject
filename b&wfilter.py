from PIL import Image

# RGB values for recoloring.
black = (0, 0, 0)
darkGray = (169, 169, 169)
lightGray = (211, 211, 211)
white = (255, 255, 255)

# Import image.
my_image = Image.open("beyonce.jpg") #change IMAGENAME to the path on your computer to the image you're using
image_list = my_image.getdata() #each pixel is represented in the form (red value, green value, blue value, transparency). You don't need the fourth value.
image_list = list(image_list) #Turns the sequence above into a list. The list can be iterated through in a loop.

recolored = [] #list that will hold the pixel data for the new image.

#YOUR CODE to loop through the original list of pixels and build a new list based on intensity should go here.

for pixel in image_list:
    intensity = pixel[0]+pixel[1]+pixel[2]
    if intensity < 182:
        recolored.append (black)
    if intensity >= 182 and intensity < 364:
        recolored.append (darkGray)
    if intensity >= 364 and intensity < 546:
        recolored.append (lightGray)
    if intensity >= 546:
        recolored.append (white)

# Create a new image using the recolored list. Display and save the image.
new_image = Image.new("RGB", my_image.size) #Creates a new image that will be the same size as the original image.
new_image.putdata(recolored) #Adds the data from the recolored list to the image.
new_image.show() #show the new image on the screen
new_image.save("recolored.jpg", "jpeg") #save the new image as "recolored.jpg"
#need to have updated version of python and in command prompt need to put in "pip install pillow==4.0.0"/need to download pillow
