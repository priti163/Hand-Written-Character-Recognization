import tkinter as tkinter
mydict = {'george':16,'amber':19}
a = list(mydict.keys())[list(mydict.values()).index(16)]
print(a)
window = tkinter.Tk()
window.title("Digit Recongnition")
window.geometry("350x300")
window.configure(background = "#ffffff")

#Defines GUI Elements
lbl = tkinter.Label(window, text="Digit Recognition", fg="#383a39", bg="#ffffff", font=("Helvetica", 23))
lbl3 = tkinter.Label(window, text="")
lbl2 = tkinter.Label(window, text="Enter an image's filename and click 'Upload Image'")
ent = tkinter.Entry(window)
btn = tkinter.Button(window, text="Upload Image")
lbl4 = tkinter.Label(window, text="The prediction as: ")
lbl5 = tkinter.Label(window,text="")
lbl6 = tkinter.Label(window,text="If answer is wrong, help machine learn. Enter correct answer: ")
ent1 = tkinter.Entry(window)
entbtn = tkinter.Button(window,text="Enter Value")

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