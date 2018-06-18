from PIL import Image
import numpy as np


'''
create a bin string of the code and
encode in the image in the 3-th layer
here we encode in ered pixel only
'''
def encode_image(img, malicious):
    length = len(malicious)
    binstring=getByte(length)
    for c in malicious:
        binstring+=getByte(ord(c))
    encoded = img.copy()
    w, h = img.size
    index = 0
    for row in range(h):
        for col in range(w):
            r, g, b = img.getpixel((col, row))
            if index <len(binstring):
                tr=list(getByte(r))
                tr[-3]=binstring[index]
                asc_r = int("".join(tr),2)
                index+=1
                asc_b = b
                asc_g = g
            else:
                asc_r = r
                asc_b=b
                asc_g=g
            encoded.putpixel((col, row), (asc_r, asc_g , asc_b))
    return encoded


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
    num=1
    for row in range(h):
        for col in range(w):
            r, g, b = img.getpixel((col, row))
            if num<8:
                lenstr += getByte(r)[-3]
                num += 1
            elif num==8:
                lenstr += getByte(r)[-3]
                num=9
                lens=int("".join(lenstr), 2)
            elif index <= 8*(lens):
                res+=getByte(r)[-3]
                index +=1
    for i in range(0,lens):
        rr+=chr(int(res[:8],2))
        res=res[8:]
    return rr

'''
encode the code's bits in 3 bytes jump (a full pixel)
the code is taken from the exp dictionary 
'''
def encode3():
    # 95-127
    exp = [
        # 126
        "alert(\"A high-pass filter (HPF) is an electronic filter that passes signals with a frequency higher than a automobile had\");",
        # 111
        "alert(\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas aliquam sed elit a sagittis. Maec\");",
        # 103
        "alert(\"A tolerance interval is a statistical interval within which, with some confidence level, a \");",
        # 96
        "window.location.replace('https://docs.google.com/spreadsheets/d/1rs17-AgvwYvk1u7C3K2vZWxaz-0\');",
        # 108
        "function Redirect() {window.location=\"https://www.youtube.com/results?sea\";}setTimeout('Redirect()', 10000);",
        # 95
        "function myFunction() {setTimeout(function(){ alert(\"log-transformed lead\"); }, 3000);}",
        # 117
        "window.location.replace('https://www.google.com/search?safe=strict&client=ubuntu&hs=W4H&channel=fs&ei=UcAWW5roCYWP');",
        # 106
        "function checkCookies(){var text="";if (navigator.cookieEnabled == true){text = \"enacled\";}else{text = \"enabled.\";}document.getElementById(\"demo\").innerHTML = text;}",
        # 121
        "function time() {var d = new Date();document.getElementById(\"demo\").innerHTML = d.getTime();alert(\"nose, to initiate.\");}",
        # 118
        "function changeBackground(color) {document.body.style.background = green;alert(\"Boogie-woogie is a musical genre t\");}"
    ]

    for i in range(0, 10000):
        MyImage = "batch2/image" + str(i) + ".png"
        img = Image.open(MyImage)
        encodedImage = "encoded3/enc_image" + str(i) + ".png"
        maliciousToHide = np.random.choice(exp)
        newImg = encode_image(img, maliciousToHide)
        if newImg:
            newImg.save(encodedImage)
            print("{} saved!".format(encodedImage))
