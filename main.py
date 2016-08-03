#!/usr/bin/python


import os
import subprocess
import shutil
import MySQLdb
from Tkinter import Tk, Frame, Menu
import button
import press_up
import press_down
#import press_left
import press_right
import global_var


db=MySQLdb.connect("localhost","root","root","books")
cur=db.cursor()


cur.execute("drop table if exists ebooks")
cur.execute("create table ebooks(ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,Book_Name varchar(50),Author_Name varchar(50),Book_Path varchar(50), UNIQUE(Book_Name,Book_Path));")
db.commit()

cur.execute("drop table if exists evoice")
cur.execute("create table evoice(ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,Voice_Name varchar(50),Voice_Path varchar(50), UNIQUE(Voice_Name,Voice_Path));")
db.commit()

cur.execute("drop table if exists eaudio")
cur.execute("create table eaudio(ID int NOT NULL AUTO_INCREMENT PRIMARY KEY,Audio_Name varchar(50),Audio_Path varchar(50), UNIQUE(Audio_Name,Audio_Path));")
db.commit()


#speed=130
#pitch=40

def change_speed(menu,entry):
		global_var.speed
		print menu
		print entry
		print global_var.speed
		global_var.speed= 30 * entry
		print global_var.speed
	
def change_pitch(menu,entry):
		global_var.pitch
		print menu
		print entry
		print global_var.pitch
		global_var.pitch= 20 * entry
		print global_var.pitch

for root, dirs, files in os.walk("/home/pi/rpi"): ##Extracting .txt files from the directory
	for file in files:
        	if file.endswith(".txt"):
	        	fullpath=(os.path.join(root, file))
			name=file
			
			try:
				query=("INSERT INTO ebooks (Book_Name,Book_Path) Values(%s,%s)") #insert the particularfile 														in db
				data=(name,fullpath)
		      		cur.execute(query,data)
				db.commit()
		
			except: 
				print "duplicate entry"
				db.rollback()
for root, dirs, files in os.walk("/home/pi/rpi"):
	for file_v in files:
		if file_v.endswith(".wav"):
      			fullpath_v=(os.path.join(root, file_v))
			name_v=file_v
					
			try:
				query_v=("INSERT INTO evoice(Voice_Name,Voice_Path) Values(%s,%s)")
				data_v=(name_v,fullpath_v)
				cur.execute(query_v,data_v)
				db.commit()
			except:
				print "duplicate voice"
				db.rollback()
				pass	

for root, dirs, files in os.walk("/home/pi/rpi"):
	for file_v in files:
		if file_v.endswith(".mp3"):
      			fullpath_v=(os.path.join(root, file_v))
			name_v=file_v
					
			try:
				query_v=("INSERT INTO eaudio(Audio_Name,Audio_Path) Values(%s,%s)")
				data_v=(name_v,fullpath_v)
				cur.execute(query_v,data_v)
				db.commit()
			except:
				print "duplicate audio"
				db.rollback()
				pass

class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent

        self.initUI()

        self.update_read()

    def initUI(self):

        self.parent.title("Audio Book Reader")

        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar)
	
	cur.execute("SELECT count(*) from ebooks")
	count=cur.fetchone()[0]
	print count
	
	
		

	def reading(menu,entry):
		def execute_unix(inputcommand):
	   		p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
			(output, err) = p.communicate()
			return output
		print menu
		print entry
		x="".join(entry)
		print x
		print global_var.speed
		subprocess.call(['espeak','-ven+f3','-s',str(global_var.speed),'-p',str(global_var.pitch),'-f',x])
		
	#book_rmenu=Menu(fileMenu)
	for i in range(1,count+1):
         	#for i in range(1,10):
		if i==1:
			book_rmenu=Menu(fileMenu)
		cur.execute("SELECT Book_Name from ebooks where ID=%s",i)
		var=cur.fetchone()
		book_rmenu.add_command(label=var,font=('Times New Roman',22),command = lambda var=var:reading('Read',var))		

	def deletingb(menu,entry):
		print menu
		print entry
		x="".join(entry)
		print x
		os.remove(x)
		
		book_dmenu.delete(entry)
		book_rmenu.delete(entry)
		#cur.execute("UPDATE ebooks SET ID=ID-1 WHERE ID>%s",id)
		#cur.execute("UPDATE ebooks SET ID=ID-1 WHERE ID>%s",id)
				
		#maximum_v=cur.execute("SELECT max(ID) from ebooks")
		#maximum_v=maximum_v+1
		#cur.execute("ALTER table ebooksAUTO_INCREMENT=%s",maximum_v)
		db.commit()
		
	book_dmenu=Menu(fileMenu)	
	for i in range(1,count+1):
		#if i==1:
		#	book_dmenu=Menu(fileMenu)
		cur.execute("SELECT Book_Name from ebooks where ID=%s",i)
		var=cur.fetchone()
		book_dmenu.add_command(label=var,font=('Times New Roman',22),command = lambda var=var:deletingb('Delete',var))		


	
	def playing(menu,entry):
		print menu
		print entry
		x="".join(entry)
		print x
		import pygame
		pygame.init()
		pygame.mixer.init()
		pygame.mixer.music.load(x)
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy() == True:
    			continue		
	
	def deletingv(menu,entry):
		print menu
		print entry
		x="".join(entry)
		print x
		os.remove(x)
		
		voice_dmenu.delete(entry)
		voice_dmenu.delete(entry)
		#cur.execute("UPDATE evoice SET ID=ID-1 WHERE ID>%s",id)
		#cur.execute("UPDATE evoice SET ID=ID-1 WHERE ID>%s",id)
				
		#maximum_v=cur.execute("SELECT max(ID) from evoice")
		#maximum_v=maximum_v+1
		#cur.execute("ALTER table evoice AUTO_INCREMENT=%s",maximum_v)
		db.commit()
		
	
	cur.execute("SELECT count(*) from evoice")
	count=cur.fetchone()[0]
	print "count"
	voice_pmenu=Menu(fileMenu)
	for i in range(1,count+1):
		#if i==1:
		#	voice_pmenu=Menu(fileMenu)
		cur.execute("SELECT Voice_Name from evoice where ID=%s",i)
		var=cur.fetchone()
		voice_pmenu.add_command(label=var,font=('Times New Roman',22),command = lambda var=var:playing('Play',var))	
	
	voice_dmenu=Menu(fileMenu)
	for i in range(1,count+1):
		#if i==1:
		#	voice_dmenu=Menu(fileMenu)
		cur.execute("SELECT Voice_Name from evoice where ID=%s",i)
		var=cur.fetchone()
		voice_dmenu.add_command(label=var,font=('Times New Roman',22),command = lambda var=var:deletingv('Play',var))	
	
	cur.execute("SELECT count(*) from eaudio")
	count=cur.fetchone()[0]
	audio_menu=Menu(fileMenu)
	for i in range(1,count+1):
		#if i==1:
		#	audio_menu=Menu(fileMenu)
		cur.execute("SELECT Audio_Name from eaudio where ID=%s",i)
		var=cur.fetchone()
		audio_menu.add_command(label=var,font=('Times New Roman',22),command = lambda var=var:playing('Audio Books',var))	

  
	

	speedmenu=Menu(fileMenu)
	for i in range(1,11):
		speedmenu.add_command(label= i ,font=('Times New Roman',22),command = lambda i=i:change_speed('Speed',i))	

	pitchmenu=Menu(fileMenu)
	for i in range(1,11):	
		pitchmenu.add_command(label=i,font=('Times New Roman',22),command = lambda i=i:change_pitch('pitch',i))
	

	submenu2=Menu(fileMenu)
	submenu2.add_cascade(label='Speed',menu=speedmenu,font=('Times New Roman',22))
	submenu2.add_cascade(label='Pitch',menu=pitchmenu,font=('Times New Roman',22))


        submenu = Menu(fileMenu)
	submenu.add_cascade(label="Read",menu=book_rmenu,font=('Times New Roman',22))
        submenu.add_cascade(label="Delete",menu=book_dmenu, font=('Times New Roman',22))
        submenu.add_command(label="Back",font=('Times New Roman',22))
        fileMenu.add_cascade(label='Books', menu=submenu, underline=0,font=('Times New Roman',22))

	def my_process():
		#a1="arecord -f cd -D plughw:1,0 -d 10 b.wav"
		#subprocess.call(a1,shell=True)
		subprocess.call('arecord','-d','5','-r','48000','w.wav')
		print "We are done"
	def recording():
		import sys,threading
		thread=threading.Thread(target=my_process)
		thread.start()
		print "audio recording"
		
	
	
        fileMenu.add_separator()
        submenu1 = Menu(fileMenu)
        submenu1.add_command(label="Record", font=('Times New Roman',22),command = lambda var=var:recording())
        submenu1.add_cascade(label="Play",menu=voice_pmenu,font=('Times New Roman',22))
        submenu1.add_cascade(label="Delete",menu=voice_dmenu,font=('Times New Roman',22))
        fileMenu.add_cascade(label='Voice Notes', menu=submenu1,underline=5,font=('Times New Roman',22))
	fileMenu.add_cascade(label='Audio Books',menu=audio_menu,underline=0,font=('Times New Roman',22))
	fileMenu.add_cascade(label='Options',menu=submenu2,underline=0,font=('Times New Roman',22))

        fileMenu.add_command(label="Exit", underline=0, command=self.onExit,font=('Times New Roman',22))
        menubar.add_cascade(label="File", underline=0, menu=fileMenu,font=('Times New Roman',22))

	
   

    def update_read(self):
        print "str"
        button.one()
	press_up.button_up()
	press_down.button_down()
	#press_left.button_left()
	press_right.button_right()
	
        self.parent.after(100 , self.update_read)
	
	
    def onExit(self):
        self.quit()




def main():

    root = Tk()
    root.geometry("500x350+300+300")
    app = Example(root)
    
    root.mainloop()
    




if __name__ == '__main__':
    main()





      
