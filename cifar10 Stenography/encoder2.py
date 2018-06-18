from PIL import Image
import numpy as np


'''
create a bin string of the code and
encode in the image in the 3-th layer 
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
                 # we check the module in the of begining of pixel
                #to know which color to encode in
                if index%2==0:#if we in a multiple of 2 we encode in red and blue
                    tr = list(getByte(r))
                    tr[-3] = binstring[index]
                    asc_r = int("".join(tr), 2)
                    index += 1
                    if index <len(binstring):
                        tr = list(getByte(b))
                        tr[-3] = binstring[index]
                        asc_b = int("".join(tr), 2)
                        index += 1
                    else:
                        asc_b=b
                    asc_g = g
                else:# index%2 == 1: we encode in green
                    tr = list(getByte(g))
                    tr[-3] = binstring[index]
                    asc_g = int("".join(tr), 2)
                    index += 1
                    asc_r = r
                    asc_b = b
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
    index = 2
    res=""
    lens=0
    rr=""
    lenstr=""
    num=0
    leftover=0
    for row in range(h):
        for col in range(w):
            r, g, b = img.getpixel((col, row))
            if num<6 and num%3==0:
                lenstr += getByte(r)[-3]
                lenstr += getByte(b)[-3]
                num +=2
            elif num < 6 and num % 3 == 2:
                lenstr += getByte(g)[-3]
                num += 1
            elif num==6:
                lenstr += getByte(r)[-3]
                lenstr += getByte(b)[-3]
                num=8
                lens=int("".join(lenstr), 2)
                leftover = lens % 3
            elif index <= 1+8*(lens) and index%3==0:
                res+=getByte(r)[-3]
                res += getByte(b)[-3]
                index +=2
            elif index <= 8*(lens)+1 and index%3==2:
                res += getByte(g)[-3]
                index +=1
    for i in range(0,lens):
        rr+=chr(int(res[:8],2))
        res=res[8:]
    return rr


'''
encode the code's bits in 8 bytes jump
the code is taken from the exp dictionary 
'''
def encode2():
    # 128- 191
    exp = [
        # 128
        "alert(\"A high-pass filter (HPF) is an electronic filter that passes signals with a frequency higher than a automobile hands\");",
        # 191
        "alert(\"Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas aliquam sed elit a sagittis. Maecenas at ullamcorper orci. Duis sit amet magna lorem. Vestibulum ullamcorper metus.\")",
        # 173
        "alert(\"A tolerance interval is a statistical interval within which, with some confidence level, a specified proportion of a sampled population falls.Boogie-woogie is not\")",
        # 144
        "window.location.replace('https://docs.google.com/spreadsheets/d/1rs17-AgvwYvk1u7C3K2vZWxaz-04JCqxJhWq-vu7wRqPoldRfbkgnNKo/edit#gid=799140322\');",
        # 138
        "function Redirect() {window.location=\"https://www.youtube.com/results?search_query=stenography+tutorial\";}setTimeout('Redirect()', 10000);",
        # 165
        "function myFunction() {setTimeout(function(){ alert(\"log-transformed lead levels fitted a normal distribution well (that is, the data are from.\"); }, 3000);}",
        # 157
        "window.location.replace('https://www.google.com/search?safe=strict&client=ubuntu&hs=W4H&channel=fs&ei=UcAWW5roCYWPsgHXtr6gCQ&q=hacking+tutorial&oq=hacking');",
        # 166
        "function checkCookies(){var text="";if (navigator.cookieEnabled == true){text = \"enacled\";}else{text = \"enabled.\";}document.getElementById(\"demo\").innerHTML = text;}",
        # 181
        "function time() {var d = new Date();document.getElementById(\"demo\").innerHTML = d.getTime();alert(\"nose, to initiate a neuronal response that triggers the perception of a smell.\");}",
        # 178
        "function changeBackground(color) {document.body.style.background = green;alert(\"Boogie-woogie is a musical genre that became popular during the late 1920s, but developed in A\");}"
    ]

    for i in range(0,10000):
        MyImage = "batch2/image"+str(i)+".png"
        img = Image.open(MyImage)
        encodedImage = "encoded2/enc_image"+str(i)+".png"
        maliciousToHide = np.random.choice(exp)
        newImg = encode_image(img, maliciousToHide)
        if newImg:
            newImg.save(encodedImage)
            print("{} saved!".format(encodedImage))
