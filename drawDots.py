
from PIL import Image,ImageOps, ImageFilter, ImageEnhance
import turtle
import numpy, requests
import blend_modes
import urllib
from io import BytesIO
import webcolors


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name


print("1. URL Location of Image")
print("2. Local file location of image")
c_u= int(input("Do you want to enter url or local file location."))    

print("enter the path of the img in this sample format : " + "C://Users/ABC/20.jpg or like https://baobab-poseannotation-appfile.s3.amazonaws.com/media/project_5/images/images01/01418849d54b3005.o.1.jpg")

if c_u==1:
    
    url = input("Enter url of pic with extension")
    file = requests.get(url)
    img = Image.open(BytesIO(file.content))
if c_u==2:
    file= str(input("enter the path picture: "))
    img=Image.open("{}".format(file),"r")


def resiz(img):
    wi= int(input("enter width to be resize"))
    ht= int(input("enter height to be resized to "))
    img= img.thumbnail((wi,ht))

def mirror(img):
    img = img.transpose(Image.FLIP_LEFT_RIGHT)
    #img = img.transpose(Image.FLIP_LEFT_RIGHT)

def grayscale(image):
    image= image.convert('L')
    img_invert= ImageOps.invert(image)
    img_invert= img_invert.filter(ImageFilter.GaussianBlur(radius = 1))
    return image , img_invert
'''
#image brightness enhancer
enhancer = ImageEnhance.Contrast(im)

factor = 1 #gives original image
im_output = enhancer.enhance(factor)
im_output.save('original-image.png')

factor = 0.5 #decrease constrast
im_output = enhancer.enhance(factor)
im_output.save('less-contrast-image.png')

factor = 1.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('more-contrast-image.png')

'''

def enhan(factor,image):
    enhancer= ImageEnhance.Contrast(img)
    img_en= enhancer.enhance(factor)
    return img_en

#The Mathematical Equation used in the Blend() method:
#out = image1*(1.0 - alpha) + image2*alpha
# If the value of alpha is ‘0.0’ then first input image is returned,
#if its value is ‘1.0’ then second input image is
#returned and if its value is between ‘0.0’ and ‘1.0’ then mixture or
#blend of two images would be returned depending upon the inclination of alpha value.
def blen(img1, img2,alpha):
    #blended_img_float = blend_modes.dodge(background_img_float, foreground_img_float, opacity)
    img1=img1.convert('RGBA')
    img2=img2.convert('RGBA')
    # Import background image
    
    background_img = numpy.array(img1)  # Inputs to blend_modes need to be numpy arrays.
    background_img_float = background_img.astype(float)  # Inputs to blend_modes need to be floats.

    # Import foreground image

    foreground_img = numpy.array(img2)  # Inputs to blend_modes need to be numpy arrays.
    foreground_img_float = foreground_img.astype(float)  # Inputs to blend_modes need to be floats.

    # Blend images
    opacity = alpha  
    blended_img_float = blend_modes.dodge(background_img_float, foreground_img_float, opacity)
    blended_img_float = blend_modes.hard_light(background_img_float, foreground_img_float, opacity)
    #blended_img_float = blend_modes.dodge(background_img_float, foreground_img_float, opacity)
    # Convert blended image back into PIL image
    blended_img = numpy.uint8(blended_img_float)  # Image needs to be converted back to uint8 type for PIL handling.
    blended_img_raw = Image.fromarray(blended_img)  # Note that alpha channels are displayed in black by PIL by default.
                                                # This behavior is difficult to change (although possible).

    return blended_img_raw

def rgb_to_binary(image):
    #image = image.convert('L')
    image = image.convert('1')
    return image


choice_draw=input("Do you want to make a grayscale pic(Y/N) : ")
if choice_draw=="Y" or choice_draw=='y':
    img, img_i = grayscale(img)
    
    alpha= float(input("enter value of alpha(alpha is opacity in b/w 0 to 1 only-- type zero for no change)"))
    img= blen(img,img_i,alpha)
    img.show()
    e=1
    while e==1:
        f= float(input("enter factor(grater than 1 increases contrast and less than 1 decreases-- 1 for no change): "))
        img= enhan(f,img)
        img.show()
        e= int(input ("do you still want to enhance? Enter 1 to continue."))

'''
choice_binary= input("Do you want to make a binary pic(Y/N): ")
if choice_binary =='Y' or choice_binary=='y':
    img = rgb_to_binary(img)
'''


resiz(img)
img= img.rotate(180)
img = img.transpose(Image.FLIP_LEFT_RIGHT)
img.show()
img.convert('RGB')
print (img.size)

type(img)
w,h=img.size

s= turtle.Screen()
s.setworldcoordinates(0,0,int(w),int(h))
s.bgcolor("black")
t = turtle.Turtle()
t.hideturtle()
dotsize= int(input("enter dot size"))

ck= int(input("do you want to change background - enter 1 to continue"))
while ck==1:
    bg_col= input("enter background color : ")
    s.bgcolor(bg_col)
    ck= int(input("Enter 1 to change background color again"))


def changepos(turtle,x,y,c):
    
       
        turtle.speed(5000)
        turtle.color(c)
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.dot(dotsize)

   

# use getpallete
'''im2 = img.getpalette()
print(im2)'''


pic= img
x=0
y=0

for x in range (0,int(w),1):
    for y in range(0,int(h),1):
            
            
            current_color = img.getpixel( (x,y) )
            print (current_color)
            if img.mode == 'RGBA' or img.mode =='L':
                r,g,b,a = img.getpixel( (x,y ))
            if img.mode == 'RGB':
                r,g,b = img.getpixel( (x,y ))
            
            
            acol,col= get_colour_name((r,g,b))
            # print("Red: {0}, Green: {1}, Blue: {2} at {3},{4} pixel in colour as {5}".format(r,g,b,x,y,col))
            t.speed(5000)
            changepos(t,x,y,col)


ck= int(input("do you want to change background - enter 1 to continue"))
while ck==1:
    bg_col= input("enter background color : ")
    s.bgcolor(bg_col)
    ck= int(input("Enter 1 to change background color again"))

turtle.done()
