from tkinter import *
def increment_counter():
  global counter
  counter += 200
  label.config(text=f"Your current score is {counter}") #This is an f-string (or string formatting), where the curly braces contain the value of the integer variable "counter," which is then incorporated into the string.
#for more details chek : https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/4
def decerement_counter():
  global counter
  counter -= 200
  label.config(text = f"your current score is {counter}")
def reset_counter():
    global counter
    counter = 0
    label.config(text=f"Your current score is {counter}")
root = Tk()
root.title("Counter Application")
counter = 0
label = Label(root, text=f"Your current score is {counter}")
label.pack(pady = 50, padx = 100)
button = Button(root, text="Increment", command=increment_counter)
button.pack(pady = 20)
buton2 = Button(root, text="decerement", command=decerement_counter)
buton2.pack(pady = 20)
button3 = Button(root,text ="reset", command=reset_counter)
button3.pack(pady=20)
root.mainloop()