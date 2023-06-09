from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image, ImageTk

root=Tk()
root.title("QR Code Generator")
root.geometry('500x550')
def create_code():
    #file path
    input_path = filedialog.asksaveasfilename(title='Saved Image', filetyp=(("PNG File", ".png"),("ALL Files", "*.*"))) 
    if input_path:
        if input_path.endswith(".png"):
            #qr generator
            get_code = pyqrcode.create(my_entry.get())

            #file save
            get_code.png(input_path, scale=5)


    else:
        #add png
        input_path = f'{input_path}.png'
        #create qr code
        get_code = pyqrcode.create(my_entry.get())
        #save png
        get_code.png(input_path, scale=5)

    #put qr in new window
    global get_image
    get_image = ImageTk.PhotoImage(Image.open(input_path))
    #add image to label
    my_label.config(image = get_image)
    #clear entry box
    my_entry.delete(0,END)
    #succesfully generated
    my_entry.insert(0,'Succesfully Generated!')

def clear_all():
    my_entry.delete(0,END)
    my_label.config(image='')

#GUI
my_entry = Entry(root, font=("Helvetica", 20))
my_entry.pack(pady=20)

my_button = Button(root,text= "Generate", command=create_code)
my_button.pack(pady=20)

my_button2= Button(root, text="clear", command=clear_all)
my_button2.pack()

my_label = Label(root, text= '')
my_label.pack(pady=20)

root.mainloop()