import time
from tkinter import *
import threading

class GraphDrawer:

    window_width = 1280
    window_height = 720
    standard_font = ("Arial Bold", 20)
    root = Tk()
    canvas = Canvas(root)#TODO resize canvas with window size!!! eig auch alle anderen sachen

    def start(self):
        self.root.configure(width=self.window_width, height=self.window_height)

        self.__init()
        #ne update funktion oder so damit der canvas bei bildänderung angepasst wird
        thread = threading.Thread()
        thread.daemon = self.update()
        thread.start() #TODO das geht bestimmt schöner und ich brauch noch ne endfct die den thread destroyed!
        self.root.mainloop()

    def __init(self):
        top_frame = Frame(self.root)
        top_frame.grid(column=0, row=0, sticky="w")

        lbl_enter_function = Label(top_frame, text="Enter function f(x):", font=self.standard_font)
        lbl_enter_function.grid(column=0, row=0)

        entry_function = Entry(top_frame, width=20, font=self.standard_font)
        entry_function.grid(column=1,row=0)

        btn_generate_function = Button(top_frame, text="Generate", font=self.standard_font)
        btn_generate_function.grid(column=2, row=0)

        def generate_function():
            print(self.canvas.winfo_height(), " ", self.canvas.winfo_width())
        btn_generate_function.configure(command=generate_function)

        self.canvas.configure(width=self.window_width, height=int(self.window_height*0.8),  borderwidth=2, relief="solid")
        self.canvas.grid(column=0, row=1)
        self.draw_canvas()


        lbl_info = Label(self.root, text="Success",  borderwidth=2, relief="groove", font=self.standard_font)
        lbl_info.grid(column=0, row=2, sticky="w")

    def update(self):
        while True:
            self.root.update()
            self.draw_canvas()
            time.sleep(0.1)
            print("sose")

    def draw_canvas(self):
        # draw axis, maybe change later if you include zoom or other features
        axis_offset = 10
        self.canvas.create_line(0 + axis_offset, 0 + axis_offset, axis_offset, self.canvas.winfo_height() + axis_offset)
        self.canvas.create_line(0 + axis_offset, self.canvas.winfo_height() - axis_offset, self.canvas.winfo_width() + axis_offset, self.canvas.winfo_height() - axis_offset)
        # self.canvas.create_line(0 + axis_offset, 0 + axis_offset, axis_offset, 584 + axis_offset)
        # self.canvas.create_line(0 + axis_offset, 584 - axis_offset, 1288 + axis_offset, 584 - axis_offset)

