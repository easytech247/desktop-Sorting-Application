"""Desktop Sorting Application that automatically arranges 
the desktop based on file types and file extensions."""

import os
import shutil
import getpass
from Tkinter import *
import tkMessageBox

"""
creating the GUI with Tkinter 
"""
parent = Tk()
frame = Frame(parent)
label = Label(frame, text="Desktop Sorting Application")
label3= Label(frame)
frame2 = Frame(parent)



#Getting the username of the computer without having to take any input from the user
username = getpass.getuser()
"""
All the directories to sort in the various files are declared here, and they are put on the desktop
"""
_doc = 'C:\\Users\\{}\\Desktop\\DOCUMENT files'.format(username)
_pdf = '{}\\PDF files'.format(_doc)
_text = '{}\\TEXT files'.format(_doc)
__doc = '{}\\DOC files'.format(_doc)
_docx = '{}\\DOCX files'.format(_doc)
_txt = '{}\\TXT files'.format(_doc)
_epub = '{}\\EPUB files'.format(_doc)
_audio = 'C:\\Users\\{}\\Desktop\\AUDIO files'.format(username)
_video = 'C:\\Users\\{}\\Desktop\\VIDEO files'.format(username)
_image = 'C:\\Users\\{}\\Desktop\\IMAGE files'.format(username)
_exe = 'C:\\Users\\{}\\Desktop\\EXE files'.format(username)
compressed = 'C:\\Users\\{}\\Desktop\\COMPRESSED files'.format(username)
_saved = 'C:\\Users\\{}\\Desktop\\SAVED PAGES'.format(username)
_tgz = '{}\\TGZ files'.format(compressed)
_7z = '{}\\7Z files'.format(compressed)
_tar = '{}\\TAR files'.format(compressed)
_rar = '{}\\RAR files'.format(compressed)
_zip = '{}\\ZIP files'.format(compressed)
_iso = '{}\\ISO files'.format(compressed)
_gz = '{}\\GZ files'.format(compressed)


    
    
desktop = 'C:\\Users\\{}\\Desktop'.format(username)
os.chdir(desktop)

 
def get_audio_files():
    """
    This function handles the audio files based
    on some of the popularly known audio file extensions
    """
    try: os.mkdir(_audio)
    except: pass
    try:
        for filename in os.listdir(desktop):
            if filename.endswith('.mp3'):
                pathname = os.path.join(filename)
                if os.path.isfile(pathname):
                    shutil.move(pathname, _audio)
            elif filename.endswith('.wma'):
                pathname = os.path.join(filename)
                if os.path.isfile(pathname):
                    shutil.move(pathname, _audio)
            elif filename.endswith('.aac'):
                pathname = os.path.join(filename)
                if os.path.isfile(pathname):
                    shutil.move(pathname, _audio)
                shutil.move(filename, _audio)
            elif filename.endswith('.wav'):
                pathname = os.path.join(filename)
                if os.path.isfile(pathname):
                    shutil.move(pathname, _audio)
            elif filename.endswith('.MP3'):
                pathname = os.path.join(filename)
                if os.path.isfile(pathname):
                    shutil.move(pathname, _audio)
            elif filename.endswith('.WMA'):
                pathname = os.path.join(filename)
                if os.path.isfile(pathname):
                    shutil.move(pathname, _audio)
    except: pass
    



def get_image_files():
    """
    This function handles the image files based
    on some of the popularly known image file extensions
    """
    try: os.mkdir(_image)
    except: pass
    try:
        for filename in os.listdir(desktop):
            if filename.endswith('.jpg'):
                shutil.move(filename, _image)
            elif filename.endswith('.JPG'):
                shutil.move(filename, _image)
            elif filename.endswith('.jpeg'):
                shutil.move(filename, _image)
            elif filename.endswith('.JPEG'):
                shutil.move(filename, _image)
            elif filename.endswith('.bmp'):
                shutil.move(filename, _image)
            elif filename.endswith('.BMP'):
                shutil.move(filename, _image)
            elif filename.endswith('.png'):
                shutil.move(filename, _image)
            elif filename.endswith('.PNG'):
                shutil.move(filename, _image)
            elif filename.endswith('.gif'):
                shutil.move(filename, _image)
            elif filename.endswith('.GIF'):
                shutil.move(filename, _image)
            elif filename.endswith('.tiff'):
                shutil.move(filename, _image)
            elif filename.endswith('.TIFF'):
                shutil.move(filename, _image)
            elif filename.endswith('.nef'):
                shutil.move(filename, _image)
            elif filename.endswith('.NEF'):
                shutil.move(filename, _image)
    except: os.remove(filename)


def get_compressed_files():
    """
    This function handles the compressed files based
    on some of the popularly known compressed file extensions
    """
    try:
        os.mkdir(compressed)
        os.mkdir(_zip)
        os.mkdir(_tgz)
        os.mkdir(_rar)
        os.mkdir(_tar)
        os.mkdir(_7z)
        os.mkdir(_iso)
        os.mkdir(_gz)
    except: pass
    try:
        for filename in os.listdir(desktop):
            if filename.endswith('.zip'):
                shutil.move(filename, _zip)
            elif filename.endswith('.7z'):
                shutil.move(filename, _7z)
            elif filename.endswith('.rar'):
                shutil.move(filename, _rar)
            elif filename.endswith('.tar'):
                shutil.move(filename, _tar)
            elif filename.endswith('.tgz'):
                shutil.move(filename, _tgz)
            elif filename.endswith('.iso'):
                shutil.move(filename, _iso)
            elif filename.endswith('.gz'):
                shutil.move(filename, _gz)
    except: pass


def get_video_files():
    """
    This function handles the video files based
    on some of the popularly known video file extensions
    """
    try: os.mkdir(_video)
    except: pass
    try:
        for filename in os.listdir(desktop):
            if filename.endswith('.mp4'):
                shutil.move(filename, _video)
            elif filename.endswith('.MP4'):
                shutil.move(filename, _video)
            elif filename.endswith('.mpeg'):
                shutil.move(filename, _video)
            elif filename.endswith('.MPEG'):
                shutil.move(filename, _video)
            elif filename.endswith('.3gp'):
                shutil.move(filename, _video)
            elif filename.endswith('.3GP'):
                shutil.move(filename, _video)
            elif filename.endswith('.avi'):
                shutil.move(filename, _video)
            elif filename.endswith('AVI'):
                shutil.move(filename, _video)
            elif filename.endswith('wmv'):
                shutil.move(filename, _video)
            elif filename.endswith(".WMV"):
                shutil.move(filename, _video)
            elif filename.endswith('mkv'):
                shutil.move(filename, _video)
            elif filename.endswith('.MKV'):
                shutil.move(filename, _video)
            elif filename.endswith('.mov'):
                shutil.move(filename, _video)
            elif filename.endswith('.MOV'):
                shutil.move(filename, _video)
            elif filename.endswith('.flv'):
                shutil.move(filename, _video)
            elif filename.endswith('.FLV'):
                shutil.move(filename, _video)
            elif filename.endswith('.srt'):
                shutil.move(filename, _video)
            elif filename.endswith('.mpg'):
                shutil.move(filename, _video)
            elif filename.endswith('.MPG'):
                shutil.move(filename,_video)
    except: os.remove(filename)
    

def get_saved_pages():
    """
    This function handles the saved paged from the internet based
    on some of the popularly known internet pages extensions
    """
    try: os.mkdir(_saved)
    except: pass
    try:
        for filename in os.listdir(desktop):
            newname = ""
            if filename.endswith('.htm'):
                newname = filename[:-4] + "_files"
                shutil.move(filename, _saved)
                for filename2 in os.listdir(desktop):
                    if filename2 == newname:
                        shutil.move(filename2, _saved)
            elif filename.endswith('.HTM'):
                newname = filename[:-5] + "_files"
                for filename2 in os.listdir(desktop):
                    if filename2 == newname:
                        shutil.move(filename, _saved)
                        shutil.move(filename2, _saved)
            elif filename.endswith('.html'):
                newname = filename[:-5] + "_files"
                for filename2 in os.listdir(desktop):
                    if filename2 == newname:
                        shutil.move(filename, _saved)
                        shutil.move(filename2, _saved)
            elif filename.endswith('.HTML'):
                newname = filename[:-5] + "_files"
                for filename2 in os.listdir(desktop):
                    if filename2 == newname:
                        shutil.move(filename, _saved)
                        shutil.move(filename2, _saved)
    except: os.remove(filename)


def get_doc_files():
    """
    This function handles the document files based
    on some of the popularly known document file extensions
    """
    try: 
        os.mkdir(_doc)
        os.mkdir(__doc)
        os.mkdir(_txt)
        os.mkdir(_text)
        os.mkdir(_pdf)
        os.mkdir(_docx)
        os.mkdir(_epub)
    except: pass
    try: 
        for filename in os.listdir(desktop):
            if filename.endswith('.doc'):
                shutil.move(filename, __doc)
            elif filename.endswith('.txt'):
                shutil.move(filename, _txt)
            elif filename.endswith('.text'):
                shutil.move(filename, _text)
            elif filename.endswith('.docx'):
                shutil.move(filename, _docx)
            elif filename.endswith('.pdf'):
                shutil.move(filename, _pdf)
            elif filename.endswith('.epub'):
                shutil.move(filename, _epub)
            elif filename.endswith('.PDF'):
                shutil.move(filename, _pdf)
            elif filename.endswith('.DOC'):
                shutil.move(filename, __doc)
            elif filename.endswith('.TXT'):
                shutil.move(filename, _txt)
            elif filename.endswith('.EPUB'):
                shutil.move(filename, _epub)
            elif filename.endswith('.DOCX'):
                shutil.move(filename, _docx)
            elif filename.endswith('.TEXT'):
                shutil.move(filename, _text)
    except: pass

def kill():
    """
    The function to handle the close button for the GUI
    """
    parent.destroy()
    
    
def about_message():
    """
    Shows the about message box popup of the GUI
    """
    tkMessageBox.showinfo("About", "Welcome to the Automatic Desktop Sorting Application\
    \nBy EasyTech\nContact @ techeasy247@gmail.com\
    \nVersion 1.0")


def help_menu():
    """
    Shows the help message box popup of the GUI
    """
    tkMessageBox.showinfo("Help", "1. Click on any of the buttons to sort\
    \n2. Only the files on your Desktop are sorted\
    \n3. The files are sorted based only on their extension, eg '.mp3', '.pdf', etc")
    

"""
Setting out the GUI and attaching of events to various buttons,
and arranging the child widgets into the parent widget
"""

menu_bar = Menu(parent)
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='File', menu=file_menu)
about_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Help', menu=about_menu)
file_menu.add_command(label="Exit", accelerator="Alt + F4", compound='left', command=kill)
about_menu.add_command(label="About", compound='right', command=about_message)
about_menu.add_command(label='Help',compound='center', command=help_menu)
parent.config(menu=menu_bar)
label.grid(row=0, column=1)
label3.grid(row=1, column = 1)
frame.pack()
btn1 = Button(frame2, text="Sort Audio Files", command=get_audio_files)
btn2 = Button(frame2, text="Sort Video Files", command=get_video_files)
btn3 = Button(frame2, text="Sort Image Files", command=get_image_files)
btn4 = Button(frame2, text="Sort Compressed Files",command=get_compressed_files)
btn5 = Button(frame2, text="Sort Document Files", command=get_doc_files)
btn6 = Button(frame2, text="Sort Saved Pages", command=get_saved_pages)

btn1.grid(row=0, column=1)
btn2.grid(row=1, column=1)
btn3.grid(row=2, column=1)
btn4.grid(row=3, column=1)
btn5.grid(row=4, column=1)
btn6.grid(row=5, column=1)
frame2.pack()
parent.title("Desktop Sorting Application")
parent.resizable(0, 0)
parent.wm_maxsize(5000, 5000)
parent.iconbitmap(r'C:\Users\Sulaiman\workspace\Automatic Sorting Windows\src\icon.ico')
parent.mainloop()