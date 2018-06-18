from PIL import Image
import numpy as np

'''
create a bin string of the code and
encode in the image in the 3-th layer
'''
def encode_image(img, malicious):
    length = len(malicious)
    binstring = getByte(length)
    for c in malicious:
        binstring += getByte(ord(c))
    encoded = img.copy()
    w, h = img.size
    index = 0
    checker = 0
    for row in range(h):
        for col in range(w):
            r, g, b = img.getpixel((col, row))
            asc_b = b
            asc_g = g
            asc_r = r
            if index < len(binstring):
                # we check the module in the of begining of pixel
                #to know which color to encode in 
                if checker % 4 == 0:  #if we in a multiple of 4 we encode in red
                    tr = list(getByte(r))
                    tr[-3] = binstring[index]
                    asc_r = int("".join(tr), 2)
                    index += 1
                elif checker % 4 == 3: #if we have 1 spaces for next encode bit -green
                    tr = list(getByte(g))
                    tr[-3] = binstring[index]
                    asc_g = int("".join(tr), 2)
                    index += 1
                elif checker % 4 == 2:#if we have 2 spaces for next encode bit -blue
                    tr = list(getByte(b))
                    tr[-3] = binstring[index]
                    asc_b = int("".join(tr), 2)
                    index += 1
            checker += 3
            encoded.putpixel((col, row), (asc_r, asc_g, asc_b))
    return encoded

'''
get bits representation of number
pad with 0's for a uniform len
'''
def getByte(num):
    str = bin(num).replace("0b", "")
    if len(str) != 8:
        for i in range(0, 8 - len(str)):
            str = '0' + str
    return str

'''
deocde the code in the image
(for sanity check)
'''
def decode_image(img):
    w, h = img.size
    malicious = ""
    index = 0
    res = ""
    lens = 0
    rr = ""
    lenstr = ""
    num = 0
    leftover = 0
    for row in range(h):
        for col in range(w):
            r, g, b = img.getpixel((col, row))
            if num < 7:
                if leftover % 4 == 0:
                    lenstr += getByte(r)[-3]
                    num += 1
                elif leftover % 4 == 3:
                    lenstr += getByte(g)[-3]
                    num += 1
                elif leftover % 4 == 2:
                    lenstr += getByte(b)[-3]
                    num += 1
            elif num == 7:
                lenstr += getByte(g)[-3]
                lens = int("".join(lenstr), 2)
                num += 7
            elif index <= 8 * (lens):
                if leftover % 4 == 0:
                    res += getByte(r)[-3]
                    index += 1
                elif leftover % 4 == 3:
                    res += getByte(g)[-3]
                    index += 1
                elif leftover % 4 == 2:
                    res += getByte(b)[-3]
                    index += 1
            leftover += 3
    for i in range(0, lens):
        rr += chr(int(res[:8], 2))
        res = res[8:]
    return rr


'''
encode the code's bits in a byte jump
the code is taken from the exp dictionary 
'''
def encode4():
    #dictionary of the code (payload) in the len possiable in 4 bytes jumps
    exp = [
        # 48
        "alert(\"LAtH2KfslaEaOQ3eFjCv16X2Z2PV4AwTuFahhR\");",
        # 54
        "xhttp.open(\"GET\", \"ajax_info.txt\", true);xhttp.send();",
        # 56
        "\"use strict\";var obj ={get x(){return 0} };obj.x = 3.14;",
        # 63
        "var person = prompt(\"Please enter your name:\", \"Harry Potter\");",
        # 74
        "document.cookie =\"username=;expires=Thu,01 Jan 1970 00:00:00 UTC;path=/;\";",
        # 76
        "alert(\"Stegosploit creates a new way to encode \"drive-by\" browser exploits);",
        # 78
        "window.location.replace(\"https://www.youtube.com/watch?v=6lYUtIZHlJA&t=889s\");",
        # 82
        "try{document.getElementById(\"frm\").submit();catch(err){alert(\"\"+document.cookie;)}",
        # 89
        "function openWin(){myWindow = window.open(\"\", \"\", \"width=400 ,height=200\");}var myWindow;",
        # 95
        "var x= document.getElementById(\"main\").innerHTML =\"cookiesEnabled is \"+navigator.cookieEnabled;"
    ]

    for i in range(0, 10000):
        MyImage = "batch2/image" + str(i) + ".png"
        img = Image.open(MyImage)
        encodedImage = "encoded4/enc_image" + str(i) + ".png"
        maliciousToHide = np.random.choice(exp) #chose a random code to code
        newImg = encode_image(img, maliciousToHide)
        if newImg:
            newImg.save(encodedImage)
            print("{} saved!".format(encodedImage))
