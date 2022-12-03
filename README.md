# Λc^2
This repo contains two programs and some suggestions on how one can circumvent WeChat's (or in theory other Chinese social media's) censorship.  

## Background
It is well-known that social media in China are heavily censored. Violators could find their messages deleted, accounts suspended, or even jailed. In light of recent events, the need for a quick way around internet censorship is even more pressing, as China cracks down on dissidents of its zero-covid policy, Russia blocks Facebook and Instagram over anti-war messages, and the Mahsa Amini protest still rages in Iran. This repo aims to address a small part of that problem - not being able to send what you want to send over Chinese social media apps. 

## Text censorship
WeChat automatically scans messages and images for sensitive words. The consequences can range from message deleted, account suspended, permanently banned to even jailed. However, previous research (Knockel et al 2018) has shown that this filter is rather rudimentary - it can be easily defeated by separating the characters, which is why both programs function by inserting random characters between every two characters. They also set the random text and the original text to two different colors by default, so the generated text is easily readable by humans. 
Nonetheless, it is safe to assume that WeChat will eventually improve its filter, which is why main.py in /offline uses a more sophisticated method of drawing random lines and randomly varying each character's position. The basic idea here is to prevent the filter from recongising the characters in the first place. Tests with several online Chinese OCD software have shown that this reduces the recognition rate significantly. 
One can reduce the recognition rate even further by overlapping the characters. However, we do not recommend this method as it also significantly reduces its readability for humans, although you can easily add this functionality by replacing the two "space += fontsize" in main.py with "space += fontsize *0.6". 

## Image censorship
WeChat compares images to a list of blocked images and blocks those that are too similar. In anticipation that the basic texts on a blank paper format might be blocked, we added an option to add a stock image background.   
This repo cannot help you send sensitive images. For that, we recommend covering your image with a lot of markups, or if you want to be extra fancy, run a [neural style transfer model](https://www.tensorflow.org/hub/tutorials/tf2_arbitrary_image_stylization)
### initial study on the effectiveness of style transfer
We combined the style of Les Demoiselles D'avignon with 4 politically sensitive images (1 [the Tank Men](https://upload.wikimedia.org/wikipedia/en/d/dd/Tank_Man_%28Tiananmen_Square_protester%29.jpg); 2 a [poster](https://cdn.cnn.com/cnnnext/dam/assets/190801115339-protest-art-hong-kong-22-super-169.jpg) from the Hong Kong protests; 3 a [meme](https://ichef.bbci.co.uk/news/976/cpsprodpb/5074/production/_96969502_78b75efc-37fe-449f-944e-0fa30805a597.jpg) comparing Xi to Winnie the Pooh; 4 an [image](https://d1i4t8bqe7zgj6.cloudfront.net/thumbnails/634957c08b967e521393f146/2022-10-14T121813Z_1_OV228914102022RP1_RTRMADC_0_CHINA-CONGRESS-PROTESTS-ROUGH-CUT.jpg) of the Sitong Bridge Protest) using the model linked above. We then uploaded them and their originals onto Google Image Search. All 4 originals returned different instances of the image itself. For the modified images only no.2 returned relevant results, and these disappeared after we cropped out the slogan on the poster. no.1 and no.4 returned artworks with a similar style, and no.3 returned images of Winnie the Pooh without any political context.

## Limitations 
1. It is inevitable that once a message or image gains enough popularity, it will be subjected to manual review, which cannot be countered. Therefore, this repo is only suitable for small, personal acts of rebellion, not organising large movements. There are much better tools for that like TOR. 
2. The same program can be used to circumvent other social media filters on conspiracy theories and hate speeches, which we strongly discourage. However, we believe that the benefits of free speech under oppressive regimes significantly outweigh these harms. 

## Disclaimer
We cannot guarantee that these tools will always work, nor be held liable for any damages that ensue or for the content posted using these tools. This project is self-funded and has no conflict of interest. 

## Acknowledgement 
This repo is dedicated to the Sitong Bridge protestor, the White Paper protestors, and freedom fighters everywhere. We would also like to thank the staff of Harvard's CS50 course, as this project originally started as a submission for its final project. 
