import socket
from threading import Thread
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pygame import mixer




PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096


name = None
listbox =  None
textarea= None
labelchat = None
text_message = None
g = None

# Starting the mixer
mixer.init()




# Boilerplate Code

   

# Teacher Activity


# Prevoius class code
# Here we ended the last class
def connectToServer():
    global SERVER
    global name
    global sending_file

    cname = name.get()
    SERVER.send(cname.encode())

def find():
    global g
    global text_message
    f = filedialog.askopenfilename()
    g = f
    mixer.music.load(g)
    mixer.music.set_volume(0.7)
    mixer.music.play()
    text_message.insert('1.0',g)

def playMusic():
    global mixer
    global g
    mixer.music.unpause()

def pauseMusic():
    global mixer
    global g
    mixer.music.pause()
    
def openChatWindow():

    print("\n\t\t\t\tIP MESSENGER")

    #Client GUI starts here
    window=Tk()
    window.title('Messenger')
    window.geometry("500x350")
    window.configure(bg = '#0b1a1a')
    

    global name
    global listbox
    global textarea
    global labelchat
    global text_message
    global filePathLabel

    namelabel = Label(window, text= "Enter Your Name",bg = '#0b1a1a', fg = 'white', font = ("Calibri",10))
    namelabel.place(x=10, y=8)

    name = Entry(window,width =30,bg = '#055164',fg = 'white',font = ("Calibri",10))
    name.place(x=120,y=8)
    name.focus()

    connectserver = Button(window,text="Jump in!",bd=1,bg = '#1e4545',fg = 'white', font = ("Calibri",10), command = connectToServer)
    connectserver.place(x=350,y=6)

    separator = ttk.Separator(window, orient='horizontal')
    separator.place(x=0, y=35, relwidth=1, height=0.1)

    labelusers = Label(window, text= "Available songs",bg = '#0b1a1a', fg = 'white', font = ("Calibri",10))
    labelusers.place(x=10, y=50)

    listbox = Listbox(window,height = 5,width = 67,bg = '#055164',fg = 'white',activestyle = 'dotbox', font = ("Calibri",10))
    listbox.place(x=10, y=70)

    scrollbar1 = Scrollbar(listbox)
    scrollbar1.place(relheight = 1,relx = 1)
    scrollbar1.config(command = listbox.yview)

    # Student Activity 1
    connectButton=Button(window,text="Download",bd=1,bg = '#1e4545',fg = 'white', font = ("Calibri",10))
    connectButton.place(x=282,y=160)

    # Bolierplate Code
    disconnectButton=Button(window,text="Upload",bd=1,bg = '#1e4545',fg = 'white', font = ("Calibri",10))
    disconnectButton.place(x=350,y=160)

    # Teacher Activity
    refresh=Button(window,text="Refresh",bd=1,bg = '#1e4545',fg = 'white', font = ("Calibri",10), )
    refresh.place(x=435,y=160)

    labelchat = Label(window, text= "Downloaded songs",bg = '#0b1a1a', fg = 'white', font = ("Calibri",10))
    labelchat.place(x=10, y=180)

    textarea = Text(window, width = 67,height = 6,bg = '#055164',fg = 'white',font = ("Calibri",10))
    textarea.place(x=10,y=200)

    scrollbar2 = Scrollbar(textarea)
    scrollbar2.place(relheight = 1,relx = 1)
    scrollbar2.config(command = listbox.yview)

    pause=Button(window,text="Pause",bd=1,bg = '#1e4545',fg = 'white', font = ("Calibri",10), command = pauseMusic)
    pause.place(x=10,y=305)

    playButton = Button(window,text="Play",bd=1,bg = '#1e4545',fg = 'white', font = ("Calibri",10), command = playMusic)
    playButton.place(x=60,y=305)

    text_message = Text(window, width =40,height = 0.6,bg = '#055164',fg = 'white', font = ("Calibri",12))
    text_message.pack()
    text_message.place(x=98,y=306)

    choose=Button(window,text="Choose",bd=1,bg = '#1e4545',fg = 'white', font = ("Calibri",10), command = find)
    choose.place(x=430,y=305)

    filePathLabel = Label(window, text= "",bg = '#0b1a1a',fg = "white", font = ("Calibri",8))
    filePathLabel.place(x=10, y=330)

    window.mainloop()


def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))


    # Boilerlate Code
    

    openChatWindow()

setup()
