from tkinter import *
from tkinter import messagebox
import random

allbu=0
stop="next"
def click(button_code):
    global but , stop , allbu
    if stop=="next":
        bu[button_code]['text']=but[button_code]
        if but[button_code]=="min":
            bu[button_code].configure(bg="red")
            for i in range (0,len(but)):
                if but[i]=="min":
                    bu[i].configure(bg='red')
                    bu[i]['text']='min'
            messagebox.showinfo("0__0","0__0")
            stop="stop"
        else:
            allbu+=1
        if allbu==buttons-mins:
            messagebox.showinfo("win","win")
            stop="stop"


radif=4                   #-----
soton=4                   #-----
buttons=radif*soton       #-----
mins=3                    #-----
but=[]                    #-----

for i in range (0,buttons):
    but.append("-")

n=0
while n<mins :
    rand=random.randint(0,buttons-1)
    if but[rand]!="min":
        but[rand]="min"
        n+=1


print(but[0],but[3],but[6])
print(but[1],but[4],but[7])      
print(but[2],but[5],but[8],"\n")


for i in range (0,buttons):
    n=0
    if but[i]!="min":
        if (i%soton != 0) and (i-1 >= 0) and (but[i-1] == "min") : n+=1
        if ((i+1)%soton != 0) and (i+1 < buttons) and (but[i+1] == "min") : n+=1

        if (i-soton >= 0) and (but[i-soton] == "min") : n+=1
        if (i%soton != 0) and (i-soton-1 >=0) and (but[i-soton-1] == "min") : n+=1
        if ((i+1)%soton != 0) and (i-soton+1 >=0) and (but[i-soton+1] == "min") : n+=1

        if (i+soton < buttons) and (but[i+soton] == "min") : n+=1
        if (i%soton != 0) and (i+soton-1 < buttons) and (but[i+soton-1] == "min") : n+=1
        if ((i+1)%soton !=0) and (i+soton+1 < buttons) and (but[i+soton+1] == "min") : n+=1
        
        but[i]=str(n)
        

print(but[0],but[3],but[6])
print(but[1],but[4],but[7])      
print(but[2],but[5],but[8])      
        
    

print(but)

root=Tk()

sizex=50
sizey=50
bu=[]
bu.append(Button(root,command=lambda:click(0),padx=sizex,pady=sizey))
bu[0].grid(column=0,row=0)
bu.append(Button(root,command=lambda:click(1),padx=sizex,pady=sizey))
bu[1].grid(column=0,row=1)
bu.append(Button(root,command=lambda:click(2),padx=sizex,pady=sizey))
bu[2].grid(column=0,row=2)
bu.append(Button(root,command=lambda:click(3),padx=sizex,pady=sizey))
bu[3].grid(column=0,row=3)
bu.append(Button(root,command=lambda:click(4),padx=sizex,pady=sizey))
bu[4].grid(column=1,row=0)
bu.append(Button(root,command=lambda:click(5),padx=sizex,pady=sizey))
bu[5].grid(column=1,row=1)
bu.append(Button(root,command=lambda:click(6),padx=sizex,pady=sizey))
bu[6].grid(column=1,row=2)
bu.append(Button(root,command=lambda:click(7),padx=sizex,pady=sizey))
bu[7].grid(column=1,row=3)
bu.append(Button(root,command=lambda:click(8),padx=sizex,pady=sizey))
bu[8].grid(column=2,row=0)
bu.append(Button(root,command=lambda:click(9),padx=sizex,pady=sizey))
bu[9].grid(column=2,row=1)
bu.append(Button(root,command=lambda:click(10),padx=sizex,pady=sizey))
bu[10].grid(column=2,row=2)
bu.append(Button(root,command=lambda:click(11),padx=sizex,pady=sizey))
bu[11].grid(column=2,row=3)
bu.append(Button(root,command=lambda:click(12),padx=sizex,pady=sizey))
bu[12].grid(column=3,row=0)
bu.append(Button(root,command=lambda:click(13),padx=sizex,pady=sizey))
bu[13].grid(column=3,row=1)
bu.append(Button(root,command=lambda:click(14),padx=sizex,pady=sizey))
bu[14].grid(column=3,row=2)
bu.append(Button(root,command=lambda:click(15),padx=sizex,pady=sizey))
bu[15].grid(column=3,row=3)

root.geometry('500x500')


mainloop()
