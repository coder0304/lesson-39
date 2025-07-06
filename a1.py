from tkinter import*
from tkinter.filedialog import askopenfilename,asksaveasfilename

window=Tk()
window.title("codingal's Text Editor")
window.geometry("600x500")
window.rowconfigure(0,minsize=800,weight=1)
window.columnfigure(1,minsize=800,weight=1)

def open_file():
    """Open a file for editing."""
    filepath=askopenfilename( filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0,END)

    with open(filepath,"r")as input_file:
    text=input_file.read()
    txt_edit.insert(END,text)
    input_file.close()
window.title(f"Codingal's Text Editor-{filepath}")
def save_file():
    filepath=asksaveasfilename(defaultextension="txt")
    filetypes=[("Text Files","*.txt"),("All Files","*.*")],
if not filepath:
    return
with open(filepath,"w")as output_file:
    text=txt_edit;get(1.0,END)
    output_file.write(text)
window.title(f"Codingal's Text Editor-{filepath}")
txt_edit=Text(window)
fr_buttons=Frame(window,relief=RAISED,bd=2)
btn_save=Button(fr_buttons,text="save As.....")


 