'''Built by: TRENTON HAGERMAN Trentsbilling@gmail.com

Developed to create custom numerical coloring applications in tkinter.

Currently there is one function rgb(red,green,blue)
Currently there is one class numColor

'''
import tkinter as tk
def rgb(r,g,b):
    '''Function Description:
Returns a hexidecimal representaion of a color.

The #(red)(green)(blue)
'''
    red = str(hex(r%256)).replace('x','')
    green = str(hex(g%256)).replace('x','')
    blue = str(hex(b%256)).replace('x','')
    if len(red) <2:
        red = '0'+red
    elif len(red)>2:
        red = red[1:]
    if len(green) <2:
        green = '0'+green
    elif len(green)>2:
        green = green[1:]
    if len(blue) <2:
        blue = '0'+blue
    elif len(blue)>2:
        blue = blue[1:]
    return '#'+red+green+blue

class numColor:
    def __init__(self,MIN,MAX,offset= 0,boost=['red'],lowwer=['blue'],correct=True):
        self.min = MIN
        self.max = MAX
        self.step = (255.)/float(abs(MAX-MIN))
        self.low = {'red':offset,'green':offset,'blue':offset}
        self.boost = boost
        self.lowwer = lowwer
        self.correct = correct

    def color(self,x):
        if x>= self.min and x<=self.max:
                
            dcolor = self.step*(x-self.min)
            for colors in self.boost:
                self.low[colors] = int(dcolor)
            for colors in self.lowwer:
                self.low[colors] = int(255-dcolor)
            return rgb(self.low['red'],self.low['green'],self.low['blue'])
        elif x<self.min:
            if self.correct:
                print('WARNING: VALUE OUTSIDE OF STATED RANGE. NEW MIN HAS BEEN SET')
                self.min = x
                return self.color(x)
        elif x<self.max:
            if self.correct:
                print('WARNING: VALUE OUTSIDE OF STATED RANGE. NEW MAX HAS BEEN SET')
                self.max = x
                return self.color(x)
    def __repr__(self):
        root = tk.Tk()
        root.title('Color Scale')
        root.focus()
        canvas = tk.Canvas(root,width=356,height=75)
        step = (self.max-self.min)/255.
        canvas.pack()
        dx = 50
        for i in range(0,256):
            canvas.create_rectangle(i+dx,0,i+5+dx,50,fill=self.color(step*i+self.min),outline='')
            if i%32 ==0:
                canvas.create_text(i+3+dx,65,text='{}'.format(round(step*i+self.min,2)),anchor=tk.CENTER)
            if i == 255:
                canvas.create_text(i+3+dx,65,text='{}'.format(round(step*i+self.min,2)),anchor=tk.CENTER)
                
            
        
        tk.mainloop()
    

        def __write__(self,x):
            __repr__()
            return ''
        return ''
    
    def scale(self,master):
        canvas = tk.Canvas(master,width=356,height=75)
        step = (self.max-self.min)/255.
        canvas.pack(side=tk.LEFT)
        offSet = tk.IntVar()
        offSlider = tk.Scale(master,from_=0,to=255,variable = offSet)
        offSlider.pack(side=tk.RIGHT)
        dx = 50
        for i in range(0,256):
            canvas.create_rectangle(i+dx,0,i+5+dx,50,fill=self.color(step*i+self.min),outline='')
            if i%32 ==0:
                canvas.create_text(i+3+dx,65,text='{}'.format(round(step*i+self.min,2)),anchor=tk.CENTER)
            if i == 255:
                canvas.create_text(i+3+dx,65,text='{}'.format(round(step*i+self.min,2)),anchor=tk.CENTER)
    
        
