# Image Processing
# This projects takes a photo and detects the edges
# Author: Kavan Lam
# Date: April 25,2020

#HW
#1) Edit the code so that we flip the picture left to right instead of reversing it 
#2) Try to mix up the RGB values and see the result of the picture

"""
Helpful Functions and notes
1) createImage(200,200,RGB) -- Create blank color image
2) loadImage("file.jpg")
3) image(img, locx, locy, sizex, sizey)
4) tint(brightness, alpha) or tint(R, G, B, alpha)
5) loadPixels() -- loads the pixels from the object to the pixels array
6) updatePixels() -- update the object with the pixels inside the pixels array
7) The pixels array in 1D (so 2D projected onto 1D)
8) Because of 7, location = x + (y * width). Width is left to right
9) color(greyscale value 0-255) or color(R, G, B)
10) use red(), green(), blue() to extract components from color
"""


def setup():
    global img
    size(533, 529)
    img = loadImage("flower.JPG")
    
def draw():
    global img
    img_new = createImage(img.width,img.height,RGB)
    img_new.loadPixels()
    img.loadPixels()
    for y in range(img.height):  # y = row_num
        for x in range(img.width): # x = col_num
            loc = (x + (y * img.width))

            r = red(img.pixels[loc])
            g = green(img.pixels[loc])
            b = blue(img.pixels[loc])
      
            # Set the display pixel to the image pixel
            #loc = ((img.width-(x+1)) + (y * img.width))
            img_new.pixels[loc] =  color(r,g,b)  
    img_new.pixels = img_new.pixels[::-1]       
    img_new.updatePixels()   
    background(img_new) 
