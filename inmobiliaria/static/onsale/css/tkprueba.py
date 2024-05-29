import tkinter as tk

class MultiWindowApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Multi-Window App")
        
        self.create_main_window()
        
    def create_main_window(self):
        self.main_window = tk.Toplevel(self.root)
        self.main_window.title("Main Window")
        
        # Add widgets and functionality to the main window
        
        # Example: Add a button to open a new window
        open_window_button = tk.Button(self.main_window, text="Open New Window", command=self.open_new_window)
        open_window_button.pack()
        
    def open_new_window(self):
        new_window = tk.Toplevel(self.root)
        new_window.title("New Window")
        
        # Add widgets and functionality to the new window
        
    def run(self):
        self.root.mainloop()

# Create an instance of the MultiWindowApp class and run the application
app = MultiWindowApp()
app.run()