from tkinter import *

class graph(Canvas):
    options = {'width':600,
               'height':400,
               'bg_color':'white',
               'grid_color':'grey',
               'text_color':'black',
               'box_color':'black',
               'grid':True,
               'box':True,
               }
    def __init__(self,master=None,*data,**options):

        if not master:
            self.master = Tk()
            self.launch = True
        else:
            self.master = master
            self.launch = False
        super().__init__(master)

        self.data = data 
        self.lines = []

        if self.launch:
            self.play()
    def parse(self,data):
        pass
        

    def play(self):
        mainloop()


k = graph()
