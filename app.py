from PIL import Image, ImageFont, ImageDraw 
import random 

def addText(text, fontsize, imagewidth, margin, linegap, addLines, twoColors):
  my_image = Image.open("D:\CS50\content\\blank.webp")
  font = ImageFont.truetype('D:\CS50\\5c982c9f1d5fe.ttf', fontsize)
  draw = ImageDraw.Draw(my_image)
  space = margin
  line = margin
  for char in text:
    if imagewidth - margin < margin + space:
      space = margin
      line += fontsize + linegap
    ran = random.randint(int(-linegap/4), int(linegap/4))
    draw.text((space, line + ran), char, (0, 0, 0), font=font)
    #draw.text((margin + space, margin + line), char, (100, 100, 200), font=font)
    if addLines:
      draw.line((space+random.randint(0, fontsize), line+ran+fontsize*0.35, space+random.randint(0, fontsize), line+ran+fontsize*1.35), fill=0)
      draw.line((space, line+ran+random.randint(fontsize*0.35, fontsize*1.35), space+fontsize, line+ran+random.randint(fontsize*0.35, fontsize*1.35)), fill=0)
    space += fontsize
    if twoColors:
      draw.text((space, line + ran), chr(random.randint(22500, 27500)), (50, 50, 150), font=font)
    else:
      draw.text((space, line + ran), chr(random.randint(22500, 27500)), (0, 0, 0), font=font)
    space += fontsize
  my_image.save("result3.jpg")

from flask import Flask, render_template, send_file, request
from threading import Thread
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    addText(request.values.get('text'))
    return render_template("index.html", show=True)
  else:
    return render_template("index.html", show=False)
