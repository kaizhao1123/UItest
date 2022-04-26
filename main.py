import tkinter as tk


def process():
    print('hello')


# set up the window
def setUpWindow(win):
    window.title('Volume Calculating')
    window.geometry('700x500')

    startY = 100
    rowGap = 40
    fontSize = 14

    # create elements per row
    # "user name"
    tk.Label(window, text='User Name: ', font=('Arial', fontSize)).place(x=10, y=startY)
    var_usr_name = tk.StringVar()
    var_usr_name.set('example@python.com')
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name, font=('Arial', fontSize))
    entry_usr_name.place(x=130, y=startY)

    # "seed type"
    startY += rowGap
    tk.Label(window, text='Seed Type: ', font=('Arial', fontSize)).place(x=10, y=startY)
    var_seed_type = tk.StringVar()
    entry_seed_type = tk.Entry(window, textvariable=var_seed_type, font=('Arial', fontSize))
    entry_seed_type.place(x=130, y=startY)

    # "seed id"
    startY += rowGap
    tk.Label(window, text='Seed ID: ', font=('Arial', fontSize)).place(x=10, y=startY)
    var_seed_id = tk.StringVar()
    entry_seed_id = tk.Entry(window, textvariable=var_seed_id, font=('Arial', fontSize))
    entry_seed_id.place(x=130, y=startY)

    # "whether show 3d model"
    startY += rowGap
    var_show_model = tk.StringVar()
    button_show_model = tk.Checkbutton(window, text='Show 3d Model', variable=var_show_model, onvalue=1, offvalue=0)
    button_show_model.place(x=130, y=startY)

    # "run" and "exit"
    startY += rowGap
    button_run = tk.Button(window, text='Run', font=('Arial', fontSize), width=10, height=1, command=process)
    button_run.place(x=60, y=startY)
    button_exit = tk.Button(window, text='Exit', font=('Arial', fontSize), width=10, height=1, command=exit)
    button_exit.place(x=220, y=startY)



if __name__ == '__main__':
    window = tk.Tk()
    setUpWindow(window)
    window.mainloop()


