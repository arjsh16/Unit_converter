
from tkinter import *
import tkinter.messagebox
import math

#defining the conversions
class calc1:
    def unit_converting(self,x):
	    self.x=x
    def radian_to_degree(self):
        return (float(self.x) * 180 / math.pi)
    def degree_to_radian(self):
        return (float(self.x) * math.pi / 180)
    def meters_to_feet(self):
        return (float(self.x) * 3.28084)
    def meters_to_inches(self):
       return (float(self.x) * 39.3701)
    def feet_to_meters(self):
        return (float(self.x) / 3.28084)
    def feet_to_inches(self):
        return (float(self.x) * 12)
    def inches_to_meters(self):
        return (float(self.x) / 39.3701)
    def inches_to_feet(self):
        return (float(self.x) / 12)
calc1=calc1()

#creating the screen
root1=Tk()
root1.title("Unit Converter")
root1.configure(background = '#101820')
root1.geometry("480x568")

#Taking the input value
e1=Entry(root1,font=('Ariel',20,'bold'),bg='white',fg='black',width=28,bd=30,justify=RIGHT)
e1.pack()

#defining the button commands
def OnClick_conv1():
    var=e1.get()
    calc1.unit_converting(var)
    lb1=Label(root1,text= f"{var} radian in degree is {calc1.radian_to_degree()}",font=('Ariel',15,'bold'))
    lb1.pack()
def OnClick_conv2():
    var=e1.get()
    calc1.unit_converting(var)
    lb1=Label(root1,text= f"{var} degree in radian is {calc1.degree_to_radian()}",font=('Ariel',15,'bold'))
    lb1.pack()
def OnClick_conv3():
    var=e1.get()
    calc1.unit_converting(var)
    lb1=Label(root1,text= f"{var} meters in feets is {calc1.meters_to_feet()}",font=('Ariel',15,'bold'))
    lb1.pack()
def OnClick_conv4():
    var=e1.get()
    calc1.unit_converting(var)
    lb1=Label(root1,text= f"{var} meters in inches is {calc1.meters_to_inches()}",font=('Ariel',15,'bold'))
    lb1.pack()
def OnClick_conv5():
    var=e1.get()
    calc1.unit_converting(var)
    lb1=Label(root1,text= f"{var} feet in meters is {calc1.feet_to_meters()}",font=('Ariel',15,'bold'))
    lb1.pack()
def OnClick_conv6():
    var=e1.get()
    calc1.unit_converting(var)
    lb1=Label(root1,text= f"{var} feet in inches is {calc1.feet_to_inches()}",font=('Ariel',15,'bold'))
    lb1.pack()
def OnClick_conv7():
    var=e1.get()
    calc1.unit_converting(var)
    lb1=Label(root1,text= f"{var} inches in meters is {calc1.inches_to_meters()}",font=('Ariel',15,'bold'))
    lb1.pack()
def OnClick_conv8():
    var=e1.get()
    calc1.unit_converting(var)
    lb1=Label(root1,text= f"{var} inches in feet is {calc1.inches_to_feet()}",font=('Ariel',15,'bold'))
    lb1.pack()
def OnClick_conv9():
    conv_Exit = tkinter.messagebox.askyesno("Unit Converter",
										"Do you want to exit ?")
    if conv_Exit>0:
        root1.destroy()  
  
#The buttons 
bt_conv1=Button(root1,text='radian to degree',command=OnClick_conv1,fg='#FEE715',bg='black',font=('Ariel',10,'bold'))
bt_conv1.pack()

bt_conv2=Button(root1,text='degree to radian',command=OnClick_conv2,fg='#FEE715',bg='black',font=('Ariel',10,'bold'))
bt_conv2.pack()

bt_conv3=Button(root1,text=' meters to feet ',command=OnClick_conv3,fg='#FEE715',bg='black',font=('Ariel',10,'bold'))
bt_conv3.pack()

bt_conv4=Button(root1,text='meters to inches',command=OnClick_conv4,fg='#FEE715',bg='black',font=('Ariel',10,'bold'))
bt_conv4.pack()

bt_conv5=Button(root1,text=' feet to meters ',command=OnClick_conv5,fg='#FEE715',bg='black',font=('Ariel',10,'bold'))
bt_conv5.pack()

bt_conv6=Button(root1,text=' feet to inches ',command=OnClick_conv6,fg='#FEE715',bg='black',font=('Ariel',10,'bold'))
bt_conv6.pack()

bt_conv7=Button(root1,text='inches to meters',command=OnClick_conv7,fg='#FEE715',bg='black',font=('Ariel',10,'bold'))
bt_conv7.pack()

bt_conv8=Button(root1,text=' inches to feet ',command=OnClick_conv8,fg='#FEE715',bg='black',font=('Ariel',10,'bold'))
bt_conv8.pack()

bt_conv9=Button(root1,text='      Exit      ',command=OnClick_conv9,fg='#101820',bg='#FEE715',font=('Ariel',10,'bold'))
bt_conv9.pack()

root1.mainloop()