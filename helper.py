from PIL import Image
import os

def getImageSrc():
    FOLDER = './src/'
    catchFile = []
    for file in os.walk(FOLDER):
        for fileName in file[2]:
            if fileName.endswith('.jpg') or fileName.endswith('.png'):
                catchFile.append(fileName)
    return FOLDER+catchFile[0],FOLDER+catchFile[1]
    
def min(a,b):
    if a<b:
        return a
    else:
        return b
def getSize(hl,wl,hr,wr):
    return min(hl,hr),min(wl,wr)

def hasTransparency(img):
    if img.mode == "P":
        transparent = img.info.get("transparency", -1)
        for _, index in img.getcolors():
            if index == transparent:
                return True
    elif img.mode == "RGBA":
        extrema = img.getextrema()
        if extrema[3][0] < 255:
            return True
    return False

def pasteImage(destImg,w,h,Img):
    if hasTransparency(Img):
        destImg.paste(Img,(w,h),Img)
    else:
        destImg.paste(Img,(w,h))

def main():
    left_src,right_src = getImageSrc()
    right = Image.open(right_src)
    left = Image.open(left_src)
    right = right.transpose(method=Image.FLIP_LEFT_RIGHT)
    wl,hl= left.size
    wr,hr= right.size
    h,w = getSize(hl,wl,hr,wr)
    left_img = left.resize((w,h))
    right_img = right.resize((w,h))
    doubleHorny = Image.new('RGB',(w*2,h),(255,255,255))
    pasteImage(doubleHorny,0,0,left_img)
    pasteImage(doubleHorny,w,0,right_img)
    doubleHorny.save("doubleHrony.jpg")
    anotherDoubleHorny = doubleHorny.transpose(method=Image.FLIP_LEFT_RIGHT)
    anotherDoubleHorny.save("anotherDoubleHorny.jpg")
    doubleHorny.show()
    anotherDoubleHorny.show()
    left.close()
    right.close()