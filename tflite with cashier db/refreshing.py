import Tkinter as tk


class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        <other code here... >


class Application:
    def __init__(self):
        self.root = tk.Tk()
        self.frame = None
        refreshButton = tk.Button(
            self.root, text="refresh", command=self.refresh)
        self.refresh()

    def refresh(self):
        if self.frame is not None:
            self.frame.destroy()
        self.frame = Example(self.root)
        self.frame.grid
