from PIL import Image, ImageFont, ImageDraw 
import random 
import os

#settings
fontsize = 20 # font size of the text
imagewidth = 1080 # width of the background image used
margin = 100 # margin of the page
linegap = 50 # space between the two lines
addLines = False # draw 2 lines across every character if True to reduce recognition
twoColors = True # write content and noise in two distinct colours if True to improve readability

dir_path = os.path.dirname(os.path.realpath(__file__))
my_image = Image.open(dir_path+"\\blank.webp") # load the background image used
font = ImageFont.truetype(dir_path+'\\font.ttf', fontsize) # load the font library
draw = ImageDraw.Draw(my_image)
text = input("请输入您的内容：") 
space = margin
line = margin

for char in text: # iterate through each character 
    if imagewidth - margin < margin + space: # start a new line
        space = margin
        line += fontsize + linegap
        
    ran = random.randint(int(-linegap/4), int(linegap/4)) # varies the y coordinate of the characters 
    draw.text((space, line + ran), char, (0, 0, 0), font=font)
    
    if addLines: # cross through the character with two lines
        draw.line((space+random.randint(0, fontsize), line+ran+fontsize*0.35, space+random.randint(0, fontsize), line+ran+fontsize*1.35), fill=0)
        draw.line((space, line+ran+random.randint(fontsize*0.35, fontsize*1.35), space+fontsize, line+ran+random.randint(fontsize*0.35, fontsize*1.35)), fill=0)
    space += fontsize # move pen to the next character's x-coordinate
    
    #generate a random character
    if twoColors:
        draw.text((space, line + ran), chr(random.randint(22500, 27500)), (50, 50, 150), font=font)
    else:
        draw.text((space, line + ran), chr(random.randint(22500, 27500)), (0, 0, 0), font=font)
    space += fontsize # move pen to the next character's x-coordinate

my_image.save(dir_path+"\\result.jpg") # output to offline/result.jpg
