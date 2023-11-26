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
    symboles = ['-',
                '*',
                '-*',
                '^',
                '-^',
                '#',
                '_#']
    colors = ['red',
              'yellow',
              'green',
              'blue',
              'purple',
              'pink',
              'black',
              'brown',
              'white',
              'orange']
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
        groups = []
        temp = {}
        n = 0
        temp['']
        for i in data:
            if type(i) is list or type(i) is tuple:
                if len(temp)==0:
                    temp['x']=i
                elif len(temp) ==1:
                    temp['y'] =i

                else:
                    groups.append(temp)
                    temp = {}
                    temp['x']=i
            elif i in self.symboles:
                temp['sym'] = i
            elif i in self.colors:
                temp['col'] = i
        
            
        


