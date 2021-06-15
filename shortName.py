from tkinter import *

def shortName():
    
    firstName_get = firstName_ent.get()
    lastName_get = lastName_ent.get()
    
    lst = []
    for i in range(4):
        lst.append(lastName_get[i])
    
    joined_lst = ''.join(lst)
    
    res_label = Label(window,text = f'{firstName_get[0]}. {joined_lst}').grid(row = 3, column = 0, padx = 10, pady = 10)

window = Tk()
main_frm = LabelFrame()
window.title('Short name')
window.iconbitmap('name.ico')

firstName_lbl = Label(window,text = 'First Name:').grid(row = 0, column = 0, padx = 10, pady = 10)
firstName_ent = Entry(window)
lastName_lbl = Label(window,text = 'Last Name:').grid(row = 1, column = 0, padx = 10, pady = 10)
lastName_ent = Entry(window)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3,command = shortName).grid(row = 2, column = 0, padx = 10, pady = 10)

main_frm.grid(row = 0, column = 0, padx = 10, pady = 10)
firstName_ent.grid(row = 0, column = 1, padx = 10, pady = 10)
lastName_ent.grid(row = 1, column = 1, padx = 10, pady = 10)

window.mainloop()