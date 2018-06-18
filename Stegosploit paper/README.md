# Stegosploit
This part deals with  Saumil Shah's paper "Exploit Delivery via Steganography and Polyglots".
<br /> Stegosploit Toolkit is the toolkit of the paper ,there you can find a readme.txt explaining on the folders.
<br />encoded images - the images we created using the toolkit .
<br />additional files -created additional files ,by us, in order to create the polyglots.

## Recommendation
Read Saumil Shah's paper "Exploit Delivery via Steganography and Polyglots" can be found in [here](http://stegosploit.info/)

## Deployment
1. go to Stegosploit Toolkit/stego and open iterative_encoding
2. fiil the image path in "input file" field and press load
3. chose bit layer and fill the exploits in necessary fields and press "process"
4. when it's done the encoded image will downloaded 
5. copy the result image to imajs file 
6. run the appropriate perl file in the commend line. 
  e.g., 
     <br /> ```peal ./html_in_png.pl decoder.html encoded_image.png polyglot_name```
  decoder can be found in "exploits" folder (the author) of in "additional files" folder 
7. the created polyglot can be use as resouse to web server, one can be found in "additional files" folder.

## Authors

* **Galit Vaknin** - [Galit1321](https://github.com/Galit1321)

* **Ifat Neumann** - [neumani1](https://github.com/neumani1)

* **Michal Shawat** - [michalShawat](https://github.com/michalShawat)

## Acknowledgments

* Saumil Shah 
* The BIU Center for Research in Applied Cryptography and Cyber Security in Bar-Ilan University

