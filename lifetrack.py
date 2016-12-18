'''
Copyright December 2016 paulmotey @ github
    This program (lifetrack) is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''
#! /usr/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import colorchooser

import math, random, threading, time, datetime
import calendar
import sys
import struct
import subprocess
from subprocess import call
from PIL import Image 
from array import array

'''
lifetrack is intended to be a linux only program as it specifically uses 
many features of linux to monitor memory and process that is not easily
available in other sytems as well as reducing the complexity of dealing
with versions of software that has hidden specifications which can change
and render the software useless without a means to correct the problem.

This is also intended to be a teaching process 
and each part of how to use this program is to be documented to allow
modification for whatever purposes a person might apply it.

It originated because I wanted to see how various aspects of memory
management could better be displayed and monitored that the 
system monitor application GUI. Specifically how much cache was allocated
 and how that impacted performance as well as attempting to identify
 applications that leaked memory over a long term.
 
For business I wanted a simple utility to track time per job easily
and produce reports for billing or simply to identify time costs
of a project.

Steps:
1. create a github repository with .gitignore and LICENSE as well 
as a README.md file in markdown.   
2. git clone git@github.com:paulmotey/lifetrack.git
3. modify files for version 1
4. git add *
5. git commit -m "Initial version"
6. git push origin master
7. test and modify source
8. repeat steps 4 thru 6 on stable changes

Objectives
# I can click on a specific task and it will mark the time of it
# Save info by ticks from a specific date at midnight
# given 24 hrs is 1240, then that will be the window size with 1 minute increments

# Data files: updated on 1 minute intervals tracking changes in configuration
# memory at a specific time>file with process additions like ps -ALf
# activity at a specific time>file from dropdown
# network at a specific time>file 
# CPU usage>file
# notes based on a specific time like history > file
# drop down menus for config and utilities and about 

Things learned from the process:

1. tkinter is different for python3 and the names as well
as capitilization rules vary across versions
2. tkinter has 3 different ways to make a presentation

Of course this link could rot in time

http://www.python-course.eu/tkinter_layout_management.php

	1.grid
	2.pack
	3.place

3. I will try each and see what works best for the final cut

Things I tested

#stdoutdata = subprocess.getoutput("wc --lines /var/log/syslog")
#print("stdoutdata: " + stdoutdata.split()[0])

print("now is ",datetime.datetime.now().weekday())
x=datetime.date.today()
print (calendar.day_name[x.weekday()])

messagebox.showinfo(title="About Motey", message="Motie engineer maybe")  

#itemsforlistbox=['one','two','three','four','five','six','seven']
#varScale=0
#def CurSelect(evt):
	#global varScale
	#value=str((List1.get(ACTIVE)))
	#chosen=str(List1.get(List1.curselection()))
	#print("pre ",value," chosen ",chosen," scale ",varScale,float(Slider1.get()))
	#varScale=23
##mylistbox=Listbox(root,width=60,height=10,font=('times',13))
##mylistbox.bind('<<ListboxSelect>>',CurSelect)
##mylistbox.place(x=32,y=90)
#Box1=Spinbox(root,from_=0,to=10)

##Box1.pack()
#List1 = Listbox(root ,width=60,height=1,font=('times',13))
##List1.place(x=32,y=90)
#List1.bind('<<ListboxSelect>>',CurSelect)
#List1.insert(1,"One")
#List1.insert(2,"Two")
#List1.insert(3,"Help")
#List1.insert(4,"Eat")
#List1.insert(5,"Sleep")
#List1.insert(6,"Study")
#List1.insert(8,"Python")
#for items in itemsforlistbox:
    #List1.insert(END,items)
##List1.pack()
#Slider1 = Scale(root, label="Day of Month", fg="green", orient=HORIZONTAL, length=300, width=20, sliderlength=20, from_=0,to=100, tickinterval=10, variable=varScale)
##Slider1.pack()
#mvar=IntVar()
#Check1 = Checkbutton(root,state=ACTIVE,width=1,height=1, variable=mvar, bg="red", command=CurSelect2)
##Check1.pack()
##Check1.bind('<<CheckbuttonSelect>>',CurSelect2)
#Check1.var=mvar

#        self.destroy()
#        root.destroy()
#        self.master.destroy()
#        sys.exit()

		#legend_text = """
		#-------------------
		#|   ------     line1    |
		#|   ------     line2    |
		#|   ------     line3    |
		#-------------------"""
		#legend_frame = LabelFrame(Canvas,text='Legend',padx=5, pady=5)
		#legend_label = Label(legend_frame,text=legend_text)
		#legend_label.pack()

#		photo_label.grid()
#		self.photo_label.image = photo
#load=Image.open('dip.png')
#		render=Image(load)
#		img = Label(self, image=render)
#		img.image=render
#		img.place(x=0,y=0)


#		self.l9 = OptionsMenu (cf, text="Options",relief=RAISED)
#		self.l9.grid(column=1,row=5)

##Check1.pack()
##Check1.bind('<<CheckbuttonSelect>>',CurSelect2)
		#Box1.grid(column=1,row=2)
		#List1.grid(column=1,row=1)

		#thread.daemon = True
		#thread.start()
		#time.sleep(20)
		#print("main thread end...")
		#sys.exit()


'''



root = Tk()

OPTIONS = [    "egg",    "bunny",    "chicken"]

''' A routine to trace at console to see if a specific thing actually happens as expected'''
def Activity2():
	print("Trace 2")
	
''' Ways to end without leaving things behind'''
def Quit2():
	root.destroy()
	sys.exit()

''' Procedures for the top dropdown menus
message box can be various formats like info and alert and ask
'''
def AboutBox():
	if messagebox.askyesno("Version 0.0001 paulmotey","Print Report to console?"):
		print("Doing a mock report of time.",datetime.datetime.now())
		print("Year ",datetime.datetime.now().year)

def openFile():
	mLabel4 = Label(root,text="green").pack()
	toImport=filedialog.askopenfile(mode='r')
	return 1

def colorChooser():
	aColor=colorchooser.askcolor()
	mLabel4 = Label(root,text=aColor).pack()
	return

'''Create the dropdowns
Tearoff is an interesting option.
'''
mainMenu=Menu(root)
root.configure(menu=mainMenu)
subMenu=Menu(mainMenu, tearoff=0)
subMenu2=Menu(mainMenu)
mainMenu.add_cascade(label="Track Time",menu=subMenu)
subMenu.add_command(label ="Sleep",command=Activity2 )
subMenu.add_command(label ="Coffee",command=Activity2 )
subMenu.add_command(label ="Eat",command=Activity2 )
mainMenu.add_cascade(label="Add note",menu=subMenu2)
subMenu2.add_command(label ="Message",command=Activity2 )
subMenu2.add_command(label ="Import graph",command=openFile )
subMenu2.add_command(label ="Color Select",command=colorChooser )
subMenu2.add_separator()
subMenu2.add_command(label ="About",command=AboutBox )


mvar=IntVar()
''' 
This is the chart of memory at intervals
'''
class StripChart:
	def __init__(self, root):
		self.gf = self.makeGraph(root)
		self.cf = self.makeControls(root)
		self.gf.pack()
		self.cf.pack()
		self.Reset()
		variable = StringVar(root)
		variable.set(OPTIONS[0]) # default value
	
	'''Code tracking'''

	def Activity(self):
		print("Activity select")
	
	def CurSelect2(self):
		print(" box ",self.Check1.var.get())

	def Quit(self):
		self.go=0

	def Stop(self):
		self.go = 0
		for t in threading.enumerate():
			if t.name == "_gen_":
				t.join()

	def Reset(self):
		self.Stop()
		self.clearstrip(self.gf.p, '#345')

	def Run(self):
		self.go = 1
		for t in threading.enumerate():
			if t.name == "_gen_":
				print("already running")
				return
		threading.Thread(target=self.do_start, name="_gen_").start()
		thread = threading.Thread(target=self.do_start, name="_gen")


	def GetMem(self):
		val1=0.9 #Total=1
		val2=0.9 #used
		val3=0.9 #free
		val4=0.9 #shared
		val5=0.9 #cache
		val6=0.9 #avail

		p = subprocess.Popen('free -m',shell=True,stdout=subprocess.PIPE)
		#print("Checking memory.",p)
		for line in p.stdout.readlines():
			datalist=line.split()
			if b'Mem:' in datalist[0]:
				val1=float(int(datalist[1]))/float(int(datalist[1]))-0.01
				val2=float(int(datalist[2]))/float(int(datalist[1]))
				val3=float(int(datalist[3]))/float(int(datalist[1]))
				val4=float(int(datalist[4]))/float(int(datalist[1]))
				val5=float(int(datalist[5]))/float(int(datalist[1]))
				val6=float(int(datalist[6]))/float(int(datalist[1]))
		try:
				p.terminate
		except:
				print("Terminate failed!")
				
		return val1,val2,val3,val4,val5,val6 #0-1.0 as floats
		

	def makeGraph(self, frame):
		self.sw = 60*24
		self.h = 100
		self.top = 4
		gf = Canvas(frame, width=self.sw, height=self.h+10,bg="#704", bd=0, highlightthickness=0)
		gf.p = PhotoImage(width=2*self.sw, height=self.h)
		self.item = gf.create_image(0, self.top, image=gf.p, anchor=NW)
		return(gf)
	
	def makeControls(self, frame):
		global mvar
		cf = Frame(frame, borderwidth=1, relief="raised")
		Button(cf, text="Run", command=self.Run).grid(column=2, row=2)
		Button(cf, text="Stop?", command=self.Stop).grid(column=4, row=2)
		Button(cf, text="Reset", command=self.Reset).grid(column=6, row=2)
		Button(cf, text="Quit", command=Quit2).grid(column=8, row=2)
		Button(cf, text="Stop", command=self.Quit).grid(column=10, row=2)
		self.fps = Label(cf, text="0 minutes")
		self.fps.grid(column=2, row=4)
		self.l5 = Label(cf, text="cache", fg="yellow", bg="black")
		self.l5.grid(column=3, row=4)
		self.l6 = Label(cf, text="avail", fg="purple", bg="white")
		self.l6.grid(column=4, row=4)
		self.l4 = Label(cf, text="share", fg="blue", bg="white")
		self.l4.grid(column=5, row=4)
		self.l3 = Label(cf, text="free", fg="green", bg="white")
		self.l3.grid(column=6, row=4)
		self.l2 = Label(cf, text="used", fg="red", bg="white")
		self.l2.grid(column=7, row=4)
		self.l1 = Label(cf, text="total", fg="white", bg="black")
		self.l1.grid(column=8, row=4)
		self.l10 = Button(cf, text="Activity", fg="black", bg="white", command=self.Activity).grid(column=9, row=4)
		self.Slider1 = Scale(cf, label="Day of Month", fg="green", orient=HORIZONTAL, length=300, width=20, sliderlength=20, from_=0,to=100, tickinterval=10)
		self.Check1 = Checkbutton(cf,state=ACTIVE,width=1,height=1, bg="red", variable=mvar, command=self.CurSelect2)
		self.Check1.grid(column=1, row=1)
		self.Slider1.grid(column=2, row=3)
		self.Check1.var=mvar
		photo = PhotoImage(file="dip.png")
		self.photo_label = Label(cf,image=photo)
		self.photo_label.grid(column=1,row=8)
		self.photo_label.image = photo
		return(cf)

	def do_start(self):
		dotSpacing=11
		t = 0
		s = 0.0
		y2 = 0
		tx = time.time()
		y7=1.0/8.0
		y8=1.0/8.0
		self.fps.config(text='%0.2f minutes' % float(float(s)/6.0))
		y1,y2,y3,y4,y5,y6 = self.GetMem() 
		self.scrollstrip(self.gf.p,
				   (y1,   y2, y3,   y4,  y5,  y6, y7, y7+0.125,y7+0.250,y7+0.375, y7+0.5, y7+0.625,y7+0.750,y7+0.875),
				   ( '#fff', '#f00', '#0f0', '#00f', '#ff0', '#f0f',  "" if s % dotSpacing else "#f88", "" if s % dotSpacing else "#f88", "" if s % dotSpacing else "#f88", "" if s % dotSpacing else "#f88",  "" if s % dotSpacing else "#f88", "" if s % dotSpacing else "#f88", "" if s % dotSpacing else "#f88", "" if s % dotSpacing else "#f88"),
				 "" if s % 60 else "#088")
		while self.go:
			t += 1
			time.sleep(0.10)
			if t == 6:
				t=0
				s+=1.0
				tx2 = time.time()
				tx = tx2
				if s<2 and s>0:
					self.fps.config(text='%0.f minute' % float(s))
				else:
					self.fps.config(text='%0.f minutes' % float(s))
				y1 = 0.2*math.sin(0.02*math.pi*t)
				y1,y2,y3,y4,y5,y6 = self.GetMem() 
				self.scrollstrip(self.gf.p,
				   (y1,   y2, y3,   y4,  y5,  y6, y7, y7+0.125,y7+0.250,y7+0.375, y7+0.5, y7+0.625,y7+0.750,y7+0.875),
				   ( '#fff', '#f00', '#0f0', '#00f', '#ff0', '#f0f',  "" if s % dotSpacing else "#f88", "" if s % dotSpacing else "#f88", "" if s % dotSpacing else "#f88", "" if s % dotSpacing else "#f88",  "" if s % dotSpacing else "#f88", "" if s % dotSpacing else "#f88", "" if s % dotSpacing else "#f88", "" if s % dotSpacing else "#f88"),
				 "" if s % 60 else "#088")

	def clearstrip(self, p, color):  # Fill strip with background color
		self.bg = color              # save background color for scroll
		self.data = None             # clear previous data
		self.x = 0
		p.tk.call(p, 'put', color, '-to', 0, 0, p['width'], p['height'])

	def scrollstrip(self, p, data, colors, bar=""):   # Scroll the strip, add new data
		self.x = (self.x + 1) % self.sw               # x = double buffer position
		bg = bar if bar else self.bg
		p.tk.call(p, 'put', bg, '-to', self.x, 0,
				  self.x+1, self.h)
		p.tk.call(p, 'put', bg, '-to', self.x+self.sw, 0,
				  self.x+self.sw+1, self.h)
		self.gf.coords(self.item, -1-self.x, self.top)  # scroll to just-written column
		if not self.data:
			self.data = data
		for d in range(len(data)):
			y0 = int((self.h-1) * (1.0-self.data[d]))   # plot all the data points
			y1 = int((self.h-1) * (1.0-data[d]))
			ya, yb = sorted((y0, y1))
			for y in range(ya, yb+1):                   # connect the dots
				p.put(colors[d], (self.x,y))
				p.put(colors[d], (self.x+self.sw,y))
		self.data = data            # save for next call
  
def main():
	root.title("lifetrack")
	app = StripChart(root)
	root.mainloop()
	sys.exit()
main()

'''
Test 1 does it run? NO!
Looking for dip.png :)
Test 2 unexpected indent 247 on comment
Test 3 success

'''
