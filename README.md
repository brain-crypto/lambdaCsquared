# Λc^2
This repo contains two programs and some suggestions on how one can circumvent WeChat's (or in theory other Chinese social media's) censorship.  

## Background
It is well-known that social media in China are heavily censored. Violators could find their messages deleted, accounts suspended, or even jailed. In light of recent events, the need for a quick way around internet censorship is even more pressing, as China cracks down on dissidents of its zero-covid policy, Russia blocks Facebook and Instagram over anti-war messages, and the Mahsa Amini protest still rages in Iran. This repo aims to address a small part of that problem - not being able to send what you want to send over Chinese social media apps. 

## Text censorship
WeChat automatically scans messages and images for sensitive words. The consequences can range from message deleted, account suspended, permanently banned to even jailed. However, previous research (Knockel et al 2018) has shown that this filter is rather rudimentary - it can be easily defeated by separating the characters, which is why both programs function by inserting random characters between every two characters. They also set the random text and the original text to two different colors by default, so the generated text is easily readable by humans. 
Nonetheless, it is safe to assume that WeChat will eventually improve its filter, which is why main.py in /offline uses a more sophisticated method of drawing random lines and randomly varying each character's position. The basic idea here is to prevent the filter from recongising the characters in the first place. Tests with several online Chinese OCD software have shown that this reduces the recognition rate significantly. 
One can reduce the recognition rate even further by overlapping the characters. However, I do not recommend this method as it also significantly reduces its readability for humans, although you can easily add this functionality by replacing the two "space += fontsize" in main.py with "space += fontsize *0.6". 

## Image censorship
WeChat compares images to a list of blocked images and blocks those that are too similar. In anticipation that the basic texts on a blank paper format might be blocked, I added an option to add a stock image background.   
This repo cannot help you send sensitive images. For that, I recommend covering your image with a lot of markups, or if you want to be extra fancy, run a [style transfer model](https://www.tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization)
### Test results 

## Limitations 
It is inevitable that once a message or image gains enough popularity, it will be subjected to manual review, which cannot be countered. This 
The same program can be used to circumvent other social media filters on conspiracy theories and hate speeches, which we strongly discourage.  

## Disclaimer
I cannot guarantee that these tools will always work, nor be held liable for any damages that ensue or for the content posted using these tools. This project is self-funded and has no conflict of interest. 

## Acknowledgement 
This repo is dedicated to the Sitong Bridge protestor, the White Paper protestors, and freedom fighters everywhere. I would also like to thank the staff of Harvard's CS50 course, as this project originally started as my submission for its final project. 
