#!/usr/bin/python


import MySQLdb
from Tkinter import Tk, Frame, Menu

db=MySQLdb.connect("localhost","root","root","stp6_abr")
cur=db.cursor()
#sql="SELECT Book_Name from ebooks"
#cur.execute(sql)
#db.close()

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

    def initUI(self):

        self.parent.title("Audio Book Reader")

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
	
	cur.execute("SELECT count(*) from ebooks")
	count=cur.fetchone()[0]
	print count

	for i in range(1,count+1):
		if i==1:
			book_menu=Menu(fileMenu)
		cur.execute("SELECT Book_Name from ebooks where ID=%s",i)
		var=cur.fetchone()
		book_menu.add_command(label=var,font=('Times New Roman',20))		

	cur.execute("SELECT count(*) from audio_books")
	count=cur.fetchone()[0]
	audio_menu=Menu(fileMenu)
	for i in range(1,count+1):
		#if i==1:
		#	audio_menu=Menu(fileMenu)
		cur.execute("SELECT Aud_Name from audio_books where ID_a=%s",i)
		var=cur.fetchone()
		audio_menu.add_command(label=var,font=('Times New Roman',20))	

	cur.execute("SELECT count(*) from voice_notes")
	count=cur.fetchone()[0]
	voice_menu=Menu(fileMenu)
	for i in range(1,count+1):
		#if i==1:
		#	voice_menu=Menu(fileMenu)
		cur.execute("SELECT Rec_Name from voice_notes where ID_v=%s",i)
		var=cur.fetchone()
		voice_menu.add_command(label=var,font=('Times New Roman',20))	

	speedmenu=Menu(fileMenu)
	speedmenu.add_command(label='Low',font=('Times New Roman',20))
	speedmenu.add_command(label='Medium',font=('Times New Roman',20))
	speedmenu.add_command(label='High',font=('Times New Roman',20))	

	volumemenu=Menu(fileMenu)
	volumemenu.add_command(label='Low',font=('Times New Roman',20))
	volumemenu.add_command(label='Medium',font=('Times New Roman',20))
	volumemenu.add_command(label='High',font=('Times New Roman',20))	


	submenu2=Menu(fileMenu)
	submenu2.add_cascade(label='Speed',menu=speedmenu,font=('Times New Roman',20))
	submenu2.add_cascade(label='Volume',menu=volumemenu,font=('Times New Roman',20))


        submenu = Menu(fileMenu)
	submenu.add_cascade(label="Read",menu=book_menu,font=('Times New Roman',20))
        submenu.add_cascade(label="Delete",menu=book_menu, font=('Times New Roman',20))
        submenu.add_command(label="Back",font=('Times New Roman',20))
        fileMenu.add_cascade(label='Books', menu=submenu, underline=0,font=('Times New Roman',20))

        fileMenu.add_separator()
        submenu1 = Menu(fileMenu)
        submenu1.add_command(label="Record", font=('Times New Roman',20))
        submenu1.add_cascade(label="Play",menu=voice_menu,font=('Times New Roman',20))
        submenu1.add_command(label="Back",font=('Times New Roman',20))
        fileMenu.add_cascade(label='Voice Notes', menu=submenu1,underline=5,font=('Times New Roman',20))
	fileMenu.add_cascade(label='Audio Books',menu=audio_menu,underline=0,font=('Times New Roman',20))
	fileMenu.add_cascade(label='Options',menu=submenu2,underline=0,font=('Times New Roman',20))

        fileMenu.add_command(label="Exit", underline=0, command=self.onExit,font=('Times New Roman',20))
        menubar.add_cascade(label="File", underline=0, menu=fileMenu,font=('Times New Roman',20))


    def onExit(self):
        self.quit()
def main():

    root = Tk()
    root.geometry("500x350+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()





      
