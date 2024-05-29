import tkinter as tk

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My App")
        
        self.button1 = tk.Button(self.root, text="Open Window 1", command=self.open_window1)
        self.button1.pack()
        
        self.button2 = tk.Button(self.root, text="Open Window 2", command=self.open_window2)
        self.button2.pack()
        
    def open_window1(self):
        window1 = tk.Toplevel(self.root)
        window1.title("Window 1")
        # Add widgets and functionality to Window 1
        
    def open_window2(self):
        window2 = tk.Toplevel(self.root)
        window2.title("Window 2")
        # Add widgets and functionality to Window 2

root = tk.Tk()
app = MyApp(root)
root.mainloop()