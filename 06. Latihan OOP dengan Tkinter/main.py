import tkinter

root = tkinter.Tk()
label1 = tkinter.Label(root,text="label1")
label2 = tkinter.Label(root,text="label2")

quit = tkinter.Button(root,text="quit",command=root.destroy)

# method positioning
label1.pack()
label2.pack()
quit.pack()

root.mainloop()
