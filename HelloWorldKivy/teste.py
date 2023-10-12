from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(1, 0, 0, 1)  # Cor vermelha (R, G, B, A)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_rect, size=self.update_rect)

    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        layout1 = BoxLayout(orientation='horizontal', size_hint=(1, 0.5))
        label1 = Label(text="Este BoxLayout não é pintado")
        layout1.add_widget(label1)

        layout2 = MyBoxLayout(orientation='horizontal', size_hint=(1, 0.5))
        label2 = Label(text="Este BoxLayout é pintado")
        layout2.add_widget(label2)

        layout.add_widget(layout1)
        layout.add_widget(layout2)

        return layout

if __name__ == '__main__':
    MyApp().run()
