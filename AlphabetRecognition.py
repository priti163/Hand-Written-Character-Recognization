import tkinter as tkinter
import os
from PIL import Image,ImageFilter
from matplotlib import pyplot as plt
import pandas as panda
from sklearn.tree import DecisionTreeClassifier

data = panda.read_csv("datasets/alphabet.csv").as_matrix()
clf = DecisionTreeClassifier()

#training dataset
xtrain = data[0:,1:]
train_label = data[0:,0]
clf.fit(xtrain,train_label)

alphabets = {'A':65,'B':66,'C':67,'D':68,'E':69,'F':70,'G':71,'H':72,'I':73,'J':74,'K':75,'L':76,'M':77,'N':78,'O':79,'P':80,'Q':81,'R':82,'S':83,'T':84,'U':85,'V':86,'W':87,'X':88,'Y':89,'Z':90}

def imageprepare(argv):
    """
    This function returns the pixel values.
    The imput is a png file location.
    """
    im = Image.open(argv).convert('L')
    width = float(im.size[0])
    height = float(im.size[1])
    newImage = Image.new('L', (28, 28), (255))  # creates white canvas of 28x28 pixels

    if width > height:  # check which dimension is bigger
        # Width is bigger. Width becomes 20 pixels.
        nheight = int(round((20.0 / width * height), 0))  # resize height according to ratio width
        if (nheight == 0):  # rare case but minimum is 1 pixel
            nheight = 1
            # resize and sharpen
        img = im.resize((20, nheight), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wtop = int(round(((28 - nheight) / 2), 0))  # calculate horizontal position
        newImage.paste(img, (4, wtop))  # paste resized image on white canvas
    else:
        # Height is bigger. Heigth becomes 20 pixels.
        nwidth = int(round((20.0 / height * width), 0))  # resize width according to ratio height
        if (nwidth == 0):  # rare case but minimum is 1 pixel
            nwidth = 1
            # resize and sharpen
        img = im.resize((nwidth, 20), Image.ANTIALIAS).filter(ImageFilter.SHARPEN)
        wleft = int(round(((28 - nwidth) / 2), 0))  # caculate vertical pozition
        newImage.paste(img, (wleft, 4))  # paste resized image on white canvas

    # newImage.save("sample.png

    tv = list(newImage.getdata())  # get pixel values

    # normalize pixels to 0 and 1. 0 is pure white, 1 is pure black.
    tva = [(255 - x) * 1.0 / 255.0 for x in tv]
    print(tva)
    return tva



def btnclick():
    if ent.get() == "":
        btn.configure(text="No Filename")
    else:
        btn.configure(text="Uploading")
        filename = ent.get()

        # The name of the image file
        file_name = os.path.join(
            os.path.dirname(__file__), filename)

        x = [imageprepare(filename)]  # file path here
        print(len(x))  # mnist IMAGES are 28x28=784 pixels
        print(x[0])
        # Now we convert 784 sized 1d array to 24x24 sized 2d array so that we can visualize it
        newArr = [[0 for d in range(28)] for y in range(28)]
        k = 0
        for i in range(28):
            for j in range(28):
                newArr[i][j] = x[0][k]*1000
                k = k + 1

        for i in range(28):
            for j in range(28):
                print(newArr[i][j])
                # print(' , ')
            print('\n')

        mat = sum(newArr,[])
        print(clf.predict([mat]))
        l = list(alphabets.keys())[list(alphabets.values()).index(clf.predict([mat]))]
        lbl5.config(text=l)

        plt.imshow(newArr, cmap="gray")
        plt.savefig('MNIST_IMAGE.png')  # save MNIST image
        plt.show()  # Show / plot that image

def enterval():
    filename = ent.get()
    label = ent1.get()
    x = [imageprepare(filename)]  # file path here
    print(len(x))  # mnist IMAGES are 28x28=784 pixels
    print(x[0])
    # Now we convert 784 sized 1d array to 24x24 sized 2d array so that we can visualize it
    newArr = [[0 for d in range(28)] for y in range(28)]
    k = 0
    for i in range(28):
        for j in range(28):
            newArr[i][j] = x[0][k] * 1000
            k = k + 1

    for i in range(28):
        for j in range(28):
            print(newArr[i][j])
            # print(' , ')
        print('\n')

    mat = sum(newArr, [])
    mat = [label] + mat
    df = panda.DataFrame(mat)
    dft = df.T
    dft.to_csv("datasets/alphabet.csv",header=False,mode="a",index=False)

# Instantiate a new GUI Window
window = tkinter.Tk()
window.title("Digit Recongnition")
window.geometry("350x300")
window.configure(background = "#ffffff")

#Defines GUI Elements
lbl = tkinter.Label(window, text="Digit Recognition", fg="#383a39", bg="#ffffff", font=("Helvetica", 23))
lbl3 = tkinter.Label(window, text="")
lbl2 = tkinter.Label(window, text="Enter an image's filename and click 'Upload Image'")
ent = tkinter.Entry(window)
btn = tkinter.Button(window, text="Upload Image", command = btnclick)
lbl4 = tkinter.Label(window, text="The prediction as: ")
lbl5 = tkinter.Label(window,text="")
lbl6 = tkinter.Label(window,text="If answer is wrong, help machine learn. Enter correct answer: ")
ent1 = tkinter.Entry(window)
entbtn = tkinter.Button(window,text="Enter Value",command=enterval)

#Packs GUI Elements into window
lbl.pack()
lbl3.pack()
lbl2.pack()
ent.pack()
btn.pack()
lbl4.pack()
lbl5.pack()
lbl6.pack()
ent1.pack()
entbtn.pack()
window.mainloop()