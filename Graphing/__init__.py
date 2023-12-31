from tkinter import *
import tkColors
from numb_space import vect, linspace
import math 
class graph(Canvas):
    #Configuration Options
    options = {'width':600,
               'height':500,
               'ax_dx':80,
               'ax_dy':100,
               'offset_y':-20,
               'offset_x':0,
               'offset_title':15,
               'offset_titleAX':45,
               'bg':'white',
               'grid_color':'light grey',
               'text_color':'black',
               'ax_color':'black',
               'ax_width':3,
               'grid':True,
               'grid_tip':20,
               'ax':True,
               'min_x':False,
               'max_x':False,
               'min_y':False,
               'max_y':False,
               'title':'Untitled',
               'title_x':'',
               'title_y':'',
               'nx':9,
               'ny':9,
               'master':None,
               'title_font':('Times New Roman bold',16),
               'axis_font':('Times New Roman bold',12)
               }
    #Plot Syles
    symboles = ['~',
                '+',
                '-',
                '*',
                '-*',
                '^',
                '-^',
                '#',
                '_#']
    #built-in colors
    colors = ['blue',
              'red',
              'green',
              'yellow',
              'purple',
              'pink',
              'black',
              'brown',
              'white',
              'orange']
    def __init__(self,*data,**options):
        self.set_opt(options)

        if not self.options['master']:
            self.master = Tk()
            self.master.title('')
            self.launch = True
        else:
            self.master = self.options['master']
            self.launch = False
        
        super().__init__(self.master)
        
        
        self.data = data 
        self.lines = self.parse(data)
        self.items = {}
        self.config_master()
        self.set_extremes()
        self.build()

        

        if self.launch:
            self.play()
    
    def build(self):
        self.make_grid()
        self.make_axis() 
        self.scale()
        self.make_title()
        self.axis_titles()
        
        
    def make_title(self):
        op = self.options
        offy = op['offset_y']
        title = op['title']
        title_off = op['offset_title']
        x = op['width']/2.0
        tip = op['grid_tip']
        y =  op['ax_dy']+offy-title_off-tip
        font = op['title_font']
        self.create_text(x,y,text=title,font=font)
    
    def axis_titles(self):
        op = self.options
        offy = op['offset_y']
        offx = op['offset_x']
        titlex = op['title_x']
        titley = op['title_y']
        title_off = op['offset_titleAX']
        tip = op['grid_tip']

        dx1 = op['ax_dx']+offx
        dy1 = op['ax_dy']+offy
        dx2 = op['width']-dx1+offx
        dy2 = op['height']-dy1+offy

        y_ax_hor = dy2+tip+title_off
        x_ax_hor = (dx1 + dx2)/2.0

        x_ax_ver = dx1 - tip - title_off
        y_ax_ver = (dy1+dy2)/2.0
        

        font = op['axis_font']
        self.create_text(x_ax_hor,y_ax_hor,text=titlex,font=font)
        self.create_text(x_ax_ver,y_ax_ver,text=titley,font=font,angle=90)

    def play(self):
        self.pack(expand=True,fill=BOTH)
        self.after(100,self.resize)
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
            tip = op['grid_tip']
            self.items['axis']=self.create_rectangle(dx1-tip,dy1-tip,
                                                     dx2+tip,dy2+tip,
                                                     outline='black',
                                                     width=ax_width)

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
        tip = op['grid_tip']
        min_x = op['min_x']
        max_x = op['max_x']
        min_y = op['min_y']
        max_y = op['max_y']
        grid = []
        dx = abs(dx1-dx2)/(nx-1)
        dy = abs(dy1-dy2)/(ny-1)
        num_x = linspace(min_x,max_x,nx)
        num_y = linspace(max_y,min_y,ny)
        for i in range(nx):
            x = dx1 + (i)*dx
            grid.append(self.create_line(x,dy1-tip,x,dy2+tip,fill=op['grid_color'],dash=(4,4)))
            grid.append(self.create_text(x,dy2+1.5*tip,text=str(round(num_x[i],2))))
        for i in range(ny):
            y = dy1 + (i)*dy
            grid.append(self.create_line(dx1-tip,y,dx2+tip,y,fill=op['grid_color'],dash=(4,4)))
            grid.append(self.create_text(dx1-2.0*tip,y,text=str(round(num_y[i],2))))

    def parse(self,data):
        groups = []
        temp = {}
        n = 0
        temp['id'] = n
        
        for i in data:
        
            if type(i).__name__ in ('list', 'tuple','vect'):
                
                if len(temp)==1:
                    temp['x']=i
                elif len(temp) ==2:
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
        if 'sym' not in temp:
            temp['sym'] = self.symboles[0]
        if 'col' not in temp:
            temp['col'] = self.colors[n]
        groups.append(temp)
        return groups
    
    def set_extremes(self):
        self.set_max()
        self.set_min()

    def set_max(self):
        op = self.options
        xy = ('x','y')
        for a in xy:
            max_ = op['max_{}'.format(a)]
            if not max_:
                max_ = max(self.lines[0][a])
                for i in self.lines:
                    temp = self._get_max(i,a)
                    if max_ < temp:
                        max_ = temp
            else:
                pass
            self.options['max_{}'.format(a)] = max_
    def set_min(self):
        op = self.options
        xy = ('x','y')
        for a in xy:
            min_ = op['min_{}'.format(a)]
            if not min_:
                min_ = min(self.lines[0][a])
                for i in self.lines:
                    temp = self._get_min(i,a)
                    if min_ > temp:
                        min_ = temp
            else:
                pass
            self.options['min_{}'.format(a)] = min_

    def _get_max(self,line,key):
        return max(line[key]) 
    
    def _get_min(self,line,key):
        return min(line[key]) 
    def scale(self):
        op = self.options
        offx = op['offset_x']
        offy = op['offset_y']
        dx1 = op['ax_dx']+offx
        dy1 = op['ax_dy']+offy
        dx2 = op['width']-dx1+offx
        dy2 = op['height']-dy1+offy
        min_x = op['min_x']
        max_x = op['max_x']
        min_y = op['min_y']
        max_y = op['max_y']
        
        for i in self.lines:
            x = i['x']
            y = i['y']
            col = i['col']
            sym = i['sym']
            X = ((dx2-dx1)/(max_x-min_x))*(x-min_x)+dx1
            Y = -((dy2-dy1)/(max_y-min_y))*(y-min_y)+dy2
            self.draw(X,Y,col,sym)

    def resize(self):
        old_w = self.options['width']
        new_w = self.winfo_width()-4
        old_h = self.options['height']
        new_h = self.winfo_height()-4
        if old_w != new_w or new_h != old_h:
            self.delete('all')
            self.options['width'] = new_w
            self.options['height'] = new_h
            self.build()

        self.after(100,self.resize)
    def draw(self,X,Y,col,sym):
        op = self.symboles
        if sym == op[0]:
            for i in range(len(x)-1):
                self.create_line(X[i],Y[i],X[i+1],Y[i+1],fill=col,width=2)
        if sym == op[1]:
            for i in range(len(x)):
                self.create_text(X[i],Y[i],text='+',fill=col,font=('Times New Roman',16))
        if sym == op[2]:
            for i in range(len(x)-1):
                self.create_line(X[i],Y[i],(X[i]+X[i+1])/2.0,(Y[i]+Y[i+1])/2.0,fill=col,width=2)
        if sym == op[3]:
            for i in range(len(x)):
                self.create_text(X[i],Y[i],text='*',fill=col,font=('Times New Roman',16))
            
            
'''
  symboles = ['~',
                '+',
                '-',
                '*',
                '-*',
                '^',
                '-^',
                '#',
                '_#']  
  '''      

def f(x):
    return math.sin(x)

x = linspace(-math.pi,math.pi,100)
y = x.funct(f)


      
a=graph(x,y,title = 'Example Graph',)


        
            
        


