from tkinter import *
import os
import subprocess

a=0
os.system("ls")
root = Tk()

f = ('times',20)

def llss():
       
        #os.system("cmd0")
        tx = ls["text"]
        dir.config(font=f,text="ENTER DIRECTORY ")
        dir.place(x=280,y=280)
        dire.place(x=280+200+20+40+10+45,y=280)
        
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        sub.place(x=280+200+20+40,y=320+40+100)
        l.config(text="Command - "+tx)
        #s = dire.get()


        #os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
      

        
        #os.system("xterm -hold")
        #os.system("-- echo hello");
	#os.system("ls ~")
 	#os.system("gnome-terminal -- echo hello")
	#os.system("gnome-terminal -- ls ~ --")
       
def ccdd():
        tx = cd["text"]
        dir.config(font=f,text="ENTER DIRECTORY ")
        dir.place(x=280,y=280)
        dire.place(x=280+200+20+40+10+45,y=280)
        l.config(text="Command - "+tx)
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        sub.place(x=280+200+20+40,y=320+40+100)

def ccaall():
        tx = cal["text"]
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        l.config(text="Command - "+tx)
        os.system("gnome-terminal -- /bin/sh -c 'cal;exec bash'")
        sub.place(x=280+200+20+40+2000,y=320+40+100+2000)

def ddaattee():
        tx = date["text"]
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        sub.place(x=280+200+20+40+2000,y=320+40+100+2000)
        l.config(text="Command - "+tx)
        os.system("gnome-terminal -- /bin/sh -c 'cal;exec bash'")

def wwhhoo():
        
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        l.config(text="Command - "+tx)
        os.system("gnome-terminal -- /bin/sh -c 'who;exec bash'")
        sub.place(x=280+200+20+40+2000,y=320+40+100+2000)

def mmaann():
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir.config(text="ENTER THE COMMAND ")
        tx = man["text"]
        l.config(text="Command - "+tx)
        dir.place(x=280,y=280)
        dire.place(x=280+200+20+40+10+45,y=280)
        sub.place(x=280+200+20+40,y=320+40+100)

        
def mmkkddiirr():
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir.config(text="ENTER THE DIRECTORY NAME ")
        tx = mkdir["text"]
        dir.place(x=180,y=280)
        
        dire.place(x=280+200+20+40+10+45,y=280)
        sub.place(x=280+200+20+40,y=320+40+100)
        
        
def rrmmkkddiirr():
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir.config(text="ENTER THE DIRECTORY NAME ")
        tx = rmdir["text"]
        dir.place(x=180,y=280)
        dire.place(x=280+200+20+40+10+45,y=280)
        sub.place(x=280+200+20+40,y=320+40+100)
        l.config(text="Command - "+tx)
def mmvv():
        dir.config(text="ENTER THE SOURCE ")
        tx = mv["text"]
        dir1.place(x=180,y=320)
        dire1.place(x=280+200+20+40+10+45,y=320)
        dir.place(x=180,y=280)
        dire.place(x=280+200+20+40+10+45,y=280)
        sub.place(x=280+200+20+40,y=320+40+100)
        l.config(text="Command - "+tx)
def ppwwdd():
        tx = pwd["text"]
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        l.config(text="Command - "+tx)
        sub.place(x=280+200+20+40+2000,y=320+40+100+2000)
        os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+";exec bash'")
def rrmm():
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir.place(x=180,y=280)
        dire.place(x=280+200+20+40+10+45,y=280)
        dir.config(text="ENTER THE DIRECTORY ")
        tx = rm["text"]
        sub.place(x=280+200+20+40,y=320+40+100)
        l.config(text="Command - "+tx)

def ccpp():
        dir.config(text="ENTER THE SOURCE ")
        dir1.config(text="ENTER THE DESTINATION ")
        tx = cp["text"]
        dir.place(x=180,y=280)
        dire.place(x=280+200+20+40+10+45,y=280)
        dir1.place(x=180,y=320)
        dire1.place(x=280+200+20+40+10+45,y=320)
        sub.place(x=280+200+20+40,y=320+40+100)
        l.config(text="Command - "+tx)
def wwhhoo():
        tx = who["text"]
        dire1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dire.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir.place(x=280+200+20+40+10+45+1000,y=320+2000)
        dir1.place(x=280+200+20+40+10+45+1000,y=320+2000)
        l.config(text="Command - "+tx)
        sub.place(x=280+200+20+40+2000,y=320+40+100+2000)
        os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+";exec bash'")


def subm():
      
        if(l.cget("text")=="Command - ls"):
                tx = ls["text"]
                s = dire.get() 
                os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
              
        elif(l.cget("text")=="Command - cd"):
                tx = cd["text"]
                s = dire.get() 
                os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
                

        elif(l.cget("text")=="Command - man"):
                tx = man["text"]
                s = dire.get() 
                os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
              
        elif(l.cget("text")=="Command - mkdir"):
                tx = mkdir["text"]
                s = dire.get() 
                os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
               
        elif(l.cget("text")=="Command - rmdir"):
                tx = rmdir["text"]
                s = dire.get() 
                os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
             
                
        elif(l.cget("text")=="Command - mv"):
                tx = mv["text"]
                s = dire.get() 
                os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
               

        elif(l.cget("text")=="Command - pwd"):
                tx = pwd["text"]
                s = dire.get() 
                os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
               
        elif(l.cget("text")=="Command - rm"):
                tx = rm["text"]
                s = dire.get() 
                os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
         
      
        elif(l.cget("text")=="Command - cal"):
                tx = cal["text"]
                s = dire.get() 
                os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
           
        elif(l.cget("text")=="Command - who"):
                tx = who["text"]
                s = dire.get() 
                os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
               
        elif(l.cget("text")=="Command - date"):
                tx = date["text"]
                s = dire.get() 
                os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
               
        elif(l.cget("text")=="Command - cp"):
                tx = cp["text"]
                s = dire.get() 
                os.system("gnome-terminal -- /bin/sh -c '"+tx+" "+s+";exec bash'")
               
        
        


	
root.title('LINUX COMMANDS - OS PROJECT')
root.configure(width=800,height=10,background="#873131")
root.attributes("-fullscreen",True)

fr = Frame(root,background="#873131")
fr.config(width=1100,height=650)
fr.place(x=140+280,y=100+100)

l = Label(fr,background="#873131",foreground="white")
l.config(width=20,height=3,font=('times',25,'bold'))
l.place(x=400,y=0)

dir1 = Label(fr,text="ENTER THE DESTINATION ",background="#873131",foreground="white")
dir1.config(font=f)
dir1.place(x=280+200+20+40+10+45+2000,y=320+2000)

dire1 = Entry(fr,background="#873131",foreground="white")
dire1.config(font=f)
dire1.place(x=280+200+20+40+10+45+2000,y=320+2000)




dir = Label(fr,background="#873131",foreground="white")
dir.config(font=f,text="ENTER DIRECTORY ")
#dir.place(x=280,y=280)

dire = Entry(fr,background="#873131",foreground="white")
dire.config(font=f)
#dire.place(x=280+200+20+40+10+45,y=280)

sub = Button(fr,background="#CFE9A7",foreground="black")
sub.config(font=f,text="OK",command=subm)
sub.place(x=280+200+20+40,y=320+40+100)
sub.place(x=280+200+20+40+2000,y=320+40+100+2000)



h = Label(root,text="LINUX COMMANDS",background="#873131",foreground="white")
h.config(width=20)
h.config(font=('times',25,'bold'))
#h.grid(row=1,column=10,padx=350)
h.place(x=800,y=50)


ls = Button(root,text="ls",width="15",command=llss)
ls.config(font = f,foreground="black",background="#CFE9A7")
#ls.grid(row=2,column=1,padx=150,pady=40,sticky=W)
ls.place(x=140,y=200)

cd = Button(root,text="cd",width="15")
cd.config(font = f,foreground="black",background="#CFE9A7",command=ccdd)
#cd.grid(row=3,column=1,padx=150,pady=40,sticky=W)
cd.place(x=140,y=300)


man = Button(root,text="man",width="15")
man.config(font = f,foreground="black",background="#CFE9A7",command=mmaann)
#man.grid(row=5,column=1,padx=150,pady=40,sticky=W)
man.place(x=140,y=400)

mkdir = Button(root,text="mkdir",width="15")
mkdir.config(font = f,foreground="black",background="#CFE9A7",command=mmkkddiirr)
#mkdir.grid(row=6,column=1,padx=150,pady=40,sticky=W)
mkdir.place(x=140,y=500)


rmdir = Button(root,text="rmdir",width="15")
rmdir.config(font = f,foreground="black",background="#CFE9A7",command=rrmmkkddiirr)
#rmdir.grid(row=7,column=1,padx=150,pady=40,sticky=W)
rmdir.place(x=140,y=600)


mv = Button(root,text="mv",width="15")
mv.config(font = f,foreground="black",background="#CFE9A7",command=mmvv)
#mv.grid(row=2,column=2,padx=500,pady=40,sticky=W)
mv.place(x=140,y=700)


pwd = Button(root,text="pwd",width="15")
pwd.config(font = f,foreground="black",background="#CFE9A7",command=ppwwdd)
#mv.grid(row=2,column=2,padx=500,pady=40,sticky=W)
pwd.place(x=140+730+700,y=200)


rm = Button(root,text="rm",width="15")
rm.config(font = f,foreground="black",background="#CFE9A7",command=rrmm)
#mv.grid(row=2,column=2,padx=500,pady=40,sticky=W)
rm.place(x=140+730+700,y=300)


cp = Button(root,text="cp",width="15")
cp.config(font = f,foreground="black",background="#CFE9A7",command=ccpp)
#mv.grid(row=2,column=2,padx=500,pady=40,sticky=W)
cp.place(x=140+730+700,y=400)



cal = Button(root,text="cal",width="15")
cal.config(font = f,foreground="black",background="#CFE9A7",command=ccaall)
#mv.grid(row=2,column=2,padx=500,pady=40,sticky=W)
cal.place(x=140+730+700,y=500)

who = Button(root,text="who",width="15")
who.config(font = f,foreground="black",background="#CFE9A7",command=wwhhoo)
#mv.grid(row=2,column=2,padx=500,pady=40,sticky=W)
who.place(x=140+730+700,y=600)

date = Button(root,text="date",width="15")
date.config(font = f,foreground="black",background="#CFE9A7",command=ddaattee)
#mv.grid(row=2,column=2,padx=500,pady=40,sticky=W)
date.place(x=140+730+700,y=700)

root.mainloop()
