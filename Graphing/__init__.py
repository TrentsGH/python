from tkinter import *
import tkColors
class graph(Canvas):
    options = {'width':600,
               'height':400,
               'ax_dx':50,
               'ax_dy':70,
               'offset_y':-25,
               'offset_x':0,
               'bg':'white',
               'grid_color':'light grey',
               'text_color':'black',
               'ax_color':'black',
               'ax_width':3,
               'grid':True,
               'ax':True,
               'min':False,
               'max':False,
               'title':'Untitled',
               'nx':9,
               'ny':9
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
            self.master.title('')
            self.launch = True
        else:
            self.master = master
            self.launch = False
        
        super().__init__(master)
        
        self.set_opt(options)
        self.data = data 
        self.lines = self.parse(data)
        self.items = {}
        self.config_master()
        self.build()

        

        if self.launch:
            self.play()
    
    def build(self):
        self.make_grid()
        self.make_axis() 
        

    def play(self):
        self.pack(expand=True,fill=BOTH)
        mainloop()

    def config_master(self):
        width = self.options['width']
        height = self.options['height']
        bg = self.options['bg']
        title = self.options['title']
        self.master.configure(bg=bg,width=width,height=height)
        self.config(width=width,height=height,bg=bg)
        self.master.title(title)

    def set_opt(self,opt):
        for i in opt:
            if i in self.options:
                self.options[i] = opt[i]
            else:
                print('{} is not a valid option'.format(i))

    def make_axis(self):
        op = self.options
        if self.options['ax']:
            ax_width = op['ax_width']
            offx = op['offset_x']
            offy = op['offset_y']
            dx1 = op['ax_dx']+offx
            dy1 = op['ax_dy']+offy
            dx2 = op['width']-dx1+offx
            dy2 = op['height']-dy1+offy
            print(dx1,dx2,dy1,dy2)
            self.items['axis']=self.create_rectangle(dx1,dy1,dx2,dy2,outline='black',width=ax_width)

    def make_grid(self):
        op = self.options
        nx = op['nx']
        ny = op['ny']
        offx = op['offset_x']
        offy = op['offset_y']
        dx1 = op['ax_dx']+offx
        dy1 = op['ax_dy']+offy
        dx2 = op['width']-dx1+offx
        dy2 = op['height']-dy1+offy

        grid = []
        dx = abs(dx1-dx2)/(nx-1)
        dy = abs(dy1-dy2)/(ny-1)
        for i in range(nx):
            x = dx1 + (i)*dx
            grid.append(self.create_line(x,dy1,x,dy2,fill=op['grid_color'],dash=(4,4)))
        for i in range(ny):
            y = dy1 + (i)*dy
            grid.append(self.create_line(dx1,y,dx2,y,fill=op['grid_color'],dash=(4,4)))


    def parse(self,data):
        groups = []
        temp = {}
        n = 0
        temp['id'] = n
        for i in data:
            if type(i) is list or type(i) is tuple:
                if len(temp)==0:
                    temp['x']=i
                elif len(temp) ==1:
                    temp['y'] =i
                else:
                    if 'sym' not in temp:
                        temp['sym'] = self.symboles[0]
                    if 'col' not in temp:
                        temp['col'] = self.colors[n]
                    groups.append(temp)
                    temp = {}
                    n+=1
                    temp['id'] = n
                    temp['x']=i
            elif i in self.symboles:
                temp['sym'] = i
            elif i in self.colors:
                temp['col'] = i
        return groups
    
    def scale_x(self,x):
        pass


k = graph()
            
        
            
        


