from tkinter import *

if __name__ == '__main__':
    window_width = 1280
    window_height = 720
    standard_font = ("Arial Bold", 20)
    root = Tk()
    root.configure(width=window_width, height=window_height)

    top_frame = Frame(root)
    top_frame.grid(column=0, row=0, sticky="w")

    lbl_enter_function = Label(top_frame, text="Enter function f(x):", font=standard_font)
    lbl_enter_function.grid(column=0, row=0)

    entry_function = Entry(top_frame, width=20, font=standard_font)
    entry_function.grid(column=1,row=0)

    btn_generate_function = Button(top_frame, text="Generate", font=standard_font)
    btn_generate_function.grid(column=2, row=0)

    def generate_function():
        print("shalom")
    btn_generate_function.configure(command=generate_function)

    canvas = Canvas(root,width=window_width, height=int(window_height*0.8),  borderwidth=2, relief="solid")
    canvas.grid(column=0, row=1)
    #draw axis, maybe change later if you include zoom or other features
    canvas.create_line(0,0,50,50) # just for testing purposes

    lbl_info = Label(root, text="Success",  borderwidth=2, relief="groove", font=standard_font)
    lbl_info.grid(column=0, row=2, sticky="w")

    root.mainloop()

