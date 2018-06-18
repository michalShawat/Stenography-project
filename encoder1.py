from PIL import Image
import numpy as np


'''
create a bin string of the code and
encode in the image in the 3-th layer
here we encode in each pixel so the between
encoded bit to bit there is 1 byte distance 
'''
def encode_image(img, malicious):
    length = len(malicious)
    binstring=getNByte(length)
    for c in malicious:
        binstring+=getByte(ord(c))
    encoded = img.copy()
    w, h = img.size
    leftover = len(binstring) % 3 #if the bits rep is not a multiple of 3
    index = 0
    for row in range(h):
        for col in range(w):
            r, g, b = img.getpixel((col, row))
            if index <len(binstring)-leftover:
                tr=list(getByte(r))
                tr[-3]=binstring[index]
                asc_r = int("".join(tr),2)
                index+=1
                tr = list(getByte(g))
                tr[-3] = binstring[index]
                asc_g = int("".join(tr), 2)
                index+= 1
                tr = list(getByte(b))
                tr[-3] = binstring[index]
                asc_b = int("".join(tr), 2)
                index += 1
            elif len(binstring)-leftover<=index<len(binstring):
                if leftover==1:
                    tr = list(getByte(r))
                    tr[-3] = binstring[index]
                    asc_r = int("".join(tr), 2)
                    index += 3
                    asc_b = b
                    asc_g = g
                else:
                    tr = list(getByte(r))
                    tr[-3] = binstring[index]
                    asc_r = int("".join(tr), 2)
                    index += 1
                    tr = list(getByte(g))
                    tr[-3] = binstring[index]
                    asc_g = int("".join(tr), 2)
                    index += 1
                    asc_b = b
            else: #the bits rep of the code ended
                asc_r = r
                asc_b=b
                asc_g=g
            encoded.putpixel((col, row), (asc_r, asc_g , asc_b))
    return encoded


'''
to allow code bigger then 255 we encode the
len on 9 bits instead of 8 bits 
'''
def getNByte(num):
    str=bin(num).replace("0b", "")
    if len(str) != 9:
        for i in range(0,9-len(str)):
            str = '0'+str
    return str


'''
get bits representation of number
pad with 0's for a uniform len
'''
def getByte(num):
    str=bin(num).replace("0b", "")
    if len(str) != 8:
        for i in range(0,8-len(str)):
            str = '0'+str
    return str


'''
deocde the code in the image
(for sanity check)
'''
def decode_image(img):
    w, h = img.size
    malicious = ""
    index = 0
    res=""
    lens=0
    rr=""
    lenstr=""
    num=0
    leftover=0
    for row in range(h):
        for col in range(w):
            r, g, b = img.getpixel((col, row))
            if num<6:
                lenstr += getByte(r)[-3]
                lenstr += getByte(g)[-3]
                lenstr += getByte(b)[-3]
                num += 3
            elif 5<num<9:
                lenstr += getByte(r)[-3]
                lenstr += getByte(g)[-3]
                lenstr += getByte(b)[-3]
                num=9
                lens=int("".join(lenstr), 2)
                leftover=lens%3
            elif index <= 8*(lens)-leftover:
                res+=getByte(r)[-3]
                res += getByte(g)[-3]
                res += getByte(b)[-3]
                index +=3
    for i in range(0,lens):
        rr+=chr(int(res[:8],2))
        res=res[8:]
    return rr


'''
encode the code's bits in a byte jump
the code is taken from the exp dictionary 
'''
def encode1():
    # 191 - 382
    exp = [
        # 193
        "alert(\"A high-pass filter (HPF) is an electronic filter that passes signals with a frequency higher than a certain cutoff frequency and attenuates signals with frequencies lower than the sea\");",
        # 198
        "function changeBackground(color) {document.body.style.background = green;alert(\"Lorem ipsum dolor sit amet, consectetur adipiscing elit.Etiam vitae ante pulvinar, consectetur est et nullam para.\");}",
        # 200
        "function checkCookies() {var text = "";if (navigator.cookieEnabled == true) {text = \"Cookies are enabled.\";} else {text = \"Cookies are not enabled.\";}document.getElementById(\"demo\").innerHTML = text;}",
        # 213
        "function time() {var d = new Date();document.getElementById(\"demo\").innerHTML = d.getTime();alert(\"Abaev was born in the village of Kobi, Georgia, Russian Empire. He studied at the Gymnasium of Tiflis in 1910-\");}",
        # 259
        "window.location.replace('https://www.google.com/search?safe=strict&client=ubuntu&hs=W4H&channel=fs&ei=UcAWW5roCYWPsgHXtr6gCQ&q=hacking+tutorial&oq=hacking&gs_l=psy-ab.1.0.0i71k1l8.0.0.0.56000.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.6Dj8xTfNkeA')",
        # 272
        "alert(\"This ain't for the best\nMy reputation's never been worse, so""\nYou must like me for me.\nWe can't make\nAny promises now, can we,babe?""\nBut you can make me a drink\nDive bar on the East Side, where you at?\n""Phone lights up my nightstand in the black\nC\");",
        # 292
        "function myFunction() {setTimeout(function(){ alert(\"Tanner Joe Meyer (born May 10, 1962 in Honolulu, Hawaii) is a former Major League Baseball player. He played two seasons in the majors, 1988 and 1989, for the Milwaukee Brewers. He also played one season in Japan for their.\"); }, 3000);}",
        # 306
        "function Redirect() {window.location=\"https://www.google.com/search?safe=strict&client=ubuntu&hs=W4H&channel=fs&ei=UcAWW5roCYWPsgHXtr6gCQ&q=hacking+tutorial&oq=hacking&gs_l=psy-ab.1.0.0i71k1l8.0.0.0.56000.0.0.0.0.0.0.0.0..0.0....0...1c..64.psy-ab..0.0.0....0.6Dj8xTfNkeA\";}setTimeout('Redirect()', 10000);",
        # 341
        "document.addEventListener(\"DOMContentLoaded\", function(event) {var e = document.getElementById(\"go\"); e.addEventListener(\"click\", function() {var url = document.getElementById(\"url\").value;window.open(url,\"popUpWindow",
        "height=500, width=400, left=100, top=100, toolbar=yes, menubar=no,location=no, directories=no, status=yes\");}, false);});",
        # 382
        "alert(\"Olfactory receptors interact with odorant molecules in the nose, to initiate a neuronal response that triggers the perception of a smell. The olfactory receptor proteins are members of a large family of G-protein-coupled receptors (GPCR) arising from single coding-exon genes. Olfactory receptors share a 7-transmembrane domain structure with many neurotransmitter and..\");"
    ]

    for i in range(0,10000):
        MyImage = "batch2/image"+str(i)+".png"
        img = Image.open(MyImage)
        #print(img, img.mode)
        encodedImage = "encoded1/enc_image"+str(i)+".png"
        maliciousToHide = np.random.choice(exp)
        newImg = encode_image(img, maliciousToHide)
        if newImg:
            newImg.save(encodedImage)
            print("{} saved!".format(encodedImage))


