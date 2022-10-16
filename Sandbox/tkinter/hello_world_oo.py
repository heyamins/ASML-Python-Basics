import tkinter as tk


class App(tk.Frame):

    def __init__(self, master = None):
        w = tk.Label(master, text = 'Hello, world!')
        w.pack()


if __name__ == '__main__':
    
    root = tk.Tk()
    root.geometry('500x200+100+100')
    root.title('tkinter demo')
    
    app = App(root)

    root.mainloop()