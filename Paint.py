from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color,Ellipse,Line
from random import random

class myPaintWidget(Widget):
    def on_touch_down(self,touch):
        touch.ud={'line':[]}
        color=(random(),random(),random())
        with self.canvas:
            Color(*color)
            d=30
            Ellipse(pos=(touch.x-15,touch.y-15),size=(d,d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]
            
        print touch.x,touch.y

class myPaintApp(App):
    def build(self):
        return myPaintWidget()

if __name__=="__main__":
    myPaintApp().run()
