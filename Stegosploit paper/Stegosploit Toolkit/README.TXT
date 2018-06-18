                                  .       .
                                 / .   .' \
                         .---.  <    > <    >  .---.
                         |    \  \ - ~ ~ - /  /    |
                          ~-..-~             ~-..-~
                      \~~~\.'   stegosploit 0.2   ./~~~/
                       \__/                        \__/
                         /  .    -.                  \
                  \~~~\/   {       \       .-~ ~-.    -._ _._
                   \__/    :        }     {       \     ~{  p'-._
    .     .   |~~. .'       \       }      \       )      \  ~--'}
    \\   //   -..'       _ -\      |      _\      )__.-~~'='''''
 -._\\_//__..-'      .-~    |\.    }~~--~~  \=   / \
  ~---.._ _ _ . - ~        ) /=  /         /+  /   }
                            /_/   /         {   } |  |
                              ~---o.       ~___o.---'

by Saumil Shah
@therealsaumil

Stegosploit comprises of tools that let a user analyse images, steganographically encode exploit data onto JPG and PNG files, and turn the encoded images into polyglot files that can be rendered as HTML or executed as Javascript.

The current version of Stegosploit is 0.2

- README.TXT
- copying.txt - WTFPL
- stego/
  - image_layer_analysis.html - Analyse an image's bit layers
  - iterative_encoding.html - Encode an exploit onto a JPG or PNG image
  - imagedecoder.html - Decode a steganographically encoded image
  - imagedecode.js
  - histogram.js
  - md5.js
  - base64.js
  - stegosploit_logo_small.jpg
- exploits/
  - exploits.js - Canned exploit code
  - decoder_cve_2014_0282.html - Decoder code + CVE-2014-0282 HTML elements
- imajs/
  - html_in_jpg_ie.pl - Generate JPG+HTML polyglot for IE
  - html_in_jpg_ff.pl - Generate JPG+HTML polyglot for Firefox
  - html_in_png.pl - Generate a PNG+HTML polyglot (for any browser)
  - pngenum.pl - Enumerate a PNG file's FourCC chunks
  - jpegdump.c - Enumerate a JPG file's segments
  - CRC32.pm
  - PNGDATA.pm

jpegdump.c is written by Ralph Giles and downloaded from https://svn.xiph.org/experimental/giles/jpegdump.c

Stegosploit 0.1 was first presented at SyScan 2015, Singapore.
Stegosploit 0.2 was presented at Hack In The Box 2015, Amsterdam.

Slides from my HITB2015AMS presentation can be viewed at:

http://www.slideshare.net/saumilshah/stegosploit-hacking-with-pictures

The stego tools (image_layer_analysis.html, imagedecoder.html, iterative_encoding.html) are implemented in HTML5 CANVAS and Javascript. To use them, serve the web pages from a web server, or use python's SimpleHTTPServer:

python -m SimpleHTTPServer

