import sys
import tkinter
import traceback
import cv2
from PIL import ImageTk, Image
import numpy as np

lineOutputFile = None

if len(sys.argv) == 2:
    _, IMG_FILENAME = sys.argv
else:
    _, IMG_FILENAME, lineOutputFile = sys.argv

IMG_FILENAME = '' + IMG_FILENAME 
if lineOutputFile is None:
    lineOutputFile = 'buildingLines'

else:
    lineOutputFile = lineOutputFile + '.npy'

master = tkinter.Tk()
img_cv2 = cv2.imread(IMG_FILENAME)
IMG = ImageTk.PhotoImage(Image.open(IMG_FILENAME))
IMG_WIDTH, IMG_HEIGHT = IMG.width(), IMG.height()

canvas = tkinter.Canvas(master, width=IMG_WIDTH, height=IMG_HEIGHT)
canvas.pack()

TOP_LEFT = None
BOTTOM_RIGHT = None

lines = []


def on_click(event):

    global TOP_LEFT, BOTTOM_RIGHT

    if not TOP_LEFT:
        TOP_LEFT = event.x, event.y
    else:
        BOTTOM_RIGHT = event.x, event.y
        try:
            canvas.create_line(TOP_LEFT, BOTTOM_RIGHT, fill = "blue")

        except:
            BOTTOM_RIGHT = None
            traceback.print_exc()
        
        lines.append([TOP_LEFT, BOTTOM_RIGHT])
        TOP_LEFT = None
        BOTTOM_RIGHT = None

canvas.bind('<Button-1>', on_click)
canvas.create_image((0,0), anchor=tkinter.NW, image=IMG)

def onClose(e):
    np.save(lineOutputFile, np.array(lines))
    master.destroy()
master.bind('<Escape>', onClose)
master.mainloop()