from PIL import Image, ImageFont, ImageDraw 
import random 

def addText(text, fontsize, imagewidth, margin, linegap):
  my_image = Image.open("D:\CS50\content\\blank.webp")
  font = ImageFont.truetype('D:\CS50\\5c982c9f1d5fe.ttf', fontsize)
  draw = ImageDraw.Draw(my_image)
  text 
  space = margin
  line = margin
  for char in text:
    if imagewidth - margin < margin + space:
      space = margin
      line += fontsize + linegap
    ran = random.randint(-linegap/2, linegap/2)
    #draw.text((space, line + ran), char, (0, 0, 0), font=font)
    draw.text((margin + space, margin + line), char, (0, 0, 0), font=font)
    #draw.line((space, line+ran+fontsize/2+linegap, space+fontsize, line+fontsize/2+linegap), fill=0)
    space += fontsize
  my_image.save("result2.jpg")

from flask import Flask, render_template, send_file
from threading import Thread
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
  if flask.request.method == 'POST':
    addText(flask.request.values.get('text'))
    return render_template("index.html", show=True)
  else:
    return render_template("index.html")
