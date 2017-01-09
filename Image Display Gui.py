from PIL import Image, ImageTk
import os, os.path
import Tkinter as tk
import ttk

imgs = []
imgNumbers = {}
treeItems = []
path_name = "/Users/danielchan/Pictures"
valid_images = [".jpg",".gif",".png",".tga"]

i = 0

window = tk.Tk()
window.title(path_name)
window.geometry("570x590")
window.configure(background='grey')

textBox = tk.Entry(window)
textBox.insert(0, "/Users/danielchan/Pictures")


size_500 = (500, 300)

def on_tree_select(event):
    global tree, panel, imgs, imgNumbers, i
    for item in tree.selection():
        item_text = tree.item(item, "text")
        panel.config(image = imgs[imgNumbers[item_text]])
        i = imgNumbers[item_text]

tree = ttk.Treeview(window)
tree.heading("#0", text='File Name', anchor='w')
tree.column("#0", anchor="w", width = 300)
tree.bind("<<TreeviewSelect>>", on_tree_select)

def initialize():
    global i, treeItems, tree, imgs, imgNumbers, path_name
    path_name = textBox.get()

    for entry in tree.get_children():
        #print (entry)
        tree.delete(entry)

    treeItems[:] = []
    imgNumbers.clear()
    imgs[:] = []
    i = 0

    for f in os.listdir(path_name):

        #if str(f) != ".DS_Store" and str(f) != ".localized":
        if str(f)[-4:].lower() in valid_images:
            treeItems.append(tree.insert('', 'end', text=str(f)))
            imgNumbers[f] = i
            i += 1
        ext = os.path.splitext(f)[1]
        if ext.lower() not in valid_images:
            continue

        img = Image.open(os.path.join(path_name, f))
        #img.show()
        img.thumbnail(size_500)
        imgs.append(ImageTk.PhotoImage(img))
    i = 0
    if len(treeItems) != 0:
        tree.selection_set(treeItems[i])
        tree.focus_set()
        tree.focus(treeItems[i])

    window.title(path_name)

initialize()


def right():
    global i, panel, tree, treeItems
    i += 1
    if i == len(imgs):
        i = 0
    panel.config(image = imgs[i])
    tree.selection_set(treeItems[i])
    tree.focus_set()
    tree.focus(treeItems[i])

def left():
    global i, panel
    i -= 1
    if i == -1:
        i = len(imgs) - 1
    panel.config(image = imgs[i])
    tree.selection_set(treeItems[i])
    tree.focus_set()
    tree.focus(treeItems[i])
"""
def key(event):
    if repr(event.char) == "u'\uf703'":
        right()
    elif repr(event.char) == "u'\uf702'":
        left()

window.bind("<Key>", key)"""

panel = tk.Label(window, image = imgs[i])
rightButton = tk.Button(text = " > ", command = right)
leftButton = tk.Button(text = " < ", command = left)
enterButton = tk.Button(text = "Go", command = initialize)

textBox.pack(side = "top")
enterButton.pack(side = "top")
leftButton.pack(side = "left")
rightButton.pack(side = "right")
panel.pack()
tree.pack(side = "bottom")
#textBox.grid(row = 0, column = 3, columnspan = 2)
#enterButton.grid(row = 0, column = 5, sticky = "W")
#leftButton.grid(row = 1, column = 1, sticky = "E")
#rightButton.grid(row = 1, column = 6, stick = "W")
#panel.grid(row = 1, column = 2, columnspan = 4)
#tree.grid(row = 3, column = 4)


window.mainloop()
