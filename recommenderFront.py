## ======== Select a directory:
#
#import Tkinter, tkFileDialog
#
#root = Tkinter.Tk()
#dirname = tkFileDialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
#if len(dirname ) > 0:
#   print "You chose %s" % dirname 


# ======== Select a file for opening:
import Tkinter,tkFileDialog 
from Tkinter import *

root = Tkinter.Tk()
#def callback():
#   print "click!"
       
def selectFile():
   filename = tkFileDialog.askopenfilename(parent=root,title='Choose a file')
   #file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
   #if file != None:
      #data = file.read()
   #file.close()
   #print "I got {1} bytes from file:{2}".format(len(data), str(file))
   print('get file: {0}'.format(filename))
   out.insert(END,'Input:{0}\n'.format(filename))
   out.insert(END, 'You may also like...\n')
   out.insert(END, 'Nothing found\n')
   out.insert(END,'======================\n')


t = Tkinter.Label(root, text="Classical Music Recommender\n Please select a song to get recommendations based on composition style similarity.")
t.pack()
b = Tkinter.Button(root, text="Select a file", command=selectFile)
b.pack()
out = Tkinter.Text()
out.insert(END,'Recommendations:\n')
out.insert(END,'======================\n')
out.pack()

       
mainloop()



# ======== "Save as" dialog:
#import Tkinter,tkFileDialog
#
#myFormats = [
#      ('Windows Bitmap','*.bmp'),
#      ('Portable Network Graphics','*.png'),
#      ('JPEG / JFIF','*.jpg'),
#      ('CompuServer GIF','*.gif'),
#      ]
#
#root = Tkinter.Tk()
#fileName = tkFileDialog.asksaveasfilename(parent=root,filetypes=myFormats ,title="Save the image as...")
#if len(fileName ) > 0:
#   print "Now saving under %s" % nomFichier
