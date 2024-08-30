#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *  # Import necessary modules from the tkinter library for creating a graphical user interface (GUI).
from tkinter import ttk


# In[7]:


#This defines a class Todo to structure the application
class Todo():
  def __init__(self, root):   #initializes the main window and its components
    self.root = root         #set up the main window with title, size, and position 
    self.root.title("To-Do-List")
    self.root.geometry("650x510+350+200")

    self.label=Label(self.root, text='To-Do-List-App', font='times_new_roman 24 bold',
                     width=30, bd=5, bg='blue', fg='black')
    self.label.pack(side='top') #to display the label
    

    self.label2=Label(self.root, text='Add Task', font='arial 20 bold',
                     width=10, bd=5, bg='orange', fg='black')
    self.label.place(x=40, y=52) #to display the label   
    
    
    self.label3=Label(self.root, text='Task_list', font='arial 20 bold',
                     width=10, bd=5, bg='orange', fg='black')
    self.label.place(x=40, y=52) #to display the label
    

    self.main_text = Listbox(self.root, height=9, bd=5, width=23, font='arial 16 italic bold')
    self.main_text.place(x=280, y=115)

    self.text = Text(self.root, bd=5, height=2, width=30, font='arial 10 bold')
    self.text.place(x=28, y=120)

    
     #................Add list........................#

    def add():
      content = self.text.get(1.0, END)
      self.main_text.insert(END, content)
      with open('data.txt', 'a') as file:
        file.write(content)
        file.seek(0)
        file.close()
      self.text.delete(1.0, END)

    
    def delete():
      delete_ = self.main_text.curselection()
      look = self.main_text.get(delete_)
      with open('data.txt', 'r+') as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
          item= str(look)
          if item not in line:
            f.write(line)
        f.truncate()
      self.main_text.delete(delete_)

  
    #...................Load existing tasks.................#

    with open('data.txt', 'r') as file:
      read = file.readlines()
      for i in read:
        ready = i.split()
        self.main_text.insert(END, ready)
      file.close()
    
    
    #...............Create Buttons............................#
    self.button = Button(self.root, text='Add Task', font='times_new_roman 20 bold',
                     width=10, bd=5, bg='green', fg='black', command=add)
    self.button.place(x=30, y=180)

    self.button2 = Button(self.root, text='Delete', font='times_new_roman 20 bold',
                     width=10, bd=5, bg='orange', fg='black', command=delete)
    self.button2.place(x=30, y=280)



# Define main function  
    
    
def main():
  root = Tk()            # Create the root Tkinter window here
  obj = Todo(root)       # Pass it to the Todo class
  root.mainloop()

if __name__ == "__main__":
  main()  #call without arguments


# In[ ]:




