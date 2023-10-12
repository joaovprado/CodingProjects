from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.uix.image import Image
from kivy.graphics.texture import Texture

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


class Card(BoxLayout):
    def cria(self):             
    ################## CARD ##################
        # 1ª linha
        self.name_input = TextInput(hint_text='Insira o nome do processo', halign = 'center')
         
        # 2ª linha
        self.label_in = Label(text='Input')
        self.label_in.bold = True  # Texto em negrito
        self.label_out = Label(text='Output')
        self.label_out.bold = True  # Texto em negrito
        self.label_tempo = Label(text='Tempo (min)')
        self.label_tempo.bold = True  # Texto em negrito
        # Layout 2ª linha
        label_layout = BoxLayout(spacing=10)
        label_layout.add_widget(self.label_in)
        label_layout.add_widget(self.label_out)
        label_layout.add_widget(self.label_tempo)
        
        
        # 3ª linha
        self.input_in = TextInput(hint_text='Quantidade', input_filter=int, halign = 'center')
        self.input_out = TextInput(hint_text='Quantidade', input_filter=int, halign = 'center')
        self.input_tempo = TextInput(hint_text='Tempo', input_filter=float, halign = 'center')
        # Layout 3ª linha
        input_layout = BoxLayout(spacing=10)
        input_layout.add_widget(self.input_in)
        input_layout.add_widget(self.input_out)
        input_layout.add_widget(self.input_tempo)
        
        # 4ª linha
        self.label_capacidade = Label(text='Capacidade')
        
        # "Cards"
        card = MyBoxLayout(orientation='vertical', size_hint=(1, None), height=135, spacing = .5)
        
        card.add_widget(self.name_input)
        card.add_widget(label_layout)
        card.add_widget(input_layout)
        card.add_widget(self.label_capacidade)
        
        return card


class DadosProcesso(Screen):
    def __init__(self, **kwargs):
        super(DadosProcesso, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)
        
        ##### COR DE FUNDO ####
        with self.canvas.before:
             # Defina a cor do fundo aqui (R, G, B, A)
             Color(0, 1, 1, 1)  # Por exemplo, uma cor cinza escuro
             self.rect = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_rect, size=self.update_rect)
        
        ##################################################
        ##################### BOTÕES #####################
        bts = BoxLayout(orientation='vertical', size_hint=(1, None), height=120)
        
        # 1ª linha
        self.calc_button = Button(text='Qual é o gargalo?')
        self.calc_button.bind(on_press=self.calcs)
        
        
        # 2ª linha
        self.add_button = Button(text='+ Adicione uma etapa do processo')
        self.add_button.bind(on_press=self.add_card)
        self.delete_button = Button(text='- Exclua a última etapa do processo')
        self.delete_button.bind(on_press=self.delete_card)
        #Posicionamento dos botões da 2ª linha
        button_layout = BoxLayout(spacing=10)
        button_layout.add_widget(self.add_button)
        button_layout.add_widget(self.delete_button)
        
        # Posicionamento dos botões
        bts.add_widget(self.calc_button)
        bts.add_widget(button_layout)
        self.layout.add_widget(bts)
        
        # Cria uma região de scroll
        self.scrollview = ScrollView(size_hint=(1, 1))
        self.scroll_layout = BoxLayout(orientation='vertical', spacing=10, size_hint=(1, None))
        self.scroll_layout.bind(minimum_height=self.scroll_layout.setter('height'))
        self.layout.add_widget(self.scrollview)
        self.scrollview.add_widget(self.scroll_layout)
        
        

        self.input_fields = []

    def update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size
           
    def add_card(self, instance):
        new_card = Card().cria()
        self.scroll_layout.add_widget(new_card)
        self.input_fields.append(new_card)
        
        
    
    def delete_card(self, instance):
        if self.input_fields:
            last_input = self.input_fields.pop()
            self.scroll_layout.remove_widget(last_input)
       
        
    def calcs(self, instance):
        user_data = {
        }
        dados_screen = self.manager.get_screen('second')
        dados_screen.user_data = user_data
        self.manager.current = 'second'


class EstatScreen(Screen):
    def __init__(self, **kwargs):
        super(EstatScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

        self.welcome_label = Label(text='Bem-vindo')
        self.layout.add_widget(self.welcome_label)

        self.back_button = Button(text='Voltar para o Login')
        self.back_button.bind(on_press=self.go_to_login)
        self.layout.add_widget(self.back_button)

    def on_pre_enter(self):
        #user_data = self.user_data
        #self.welcome_label.text = f"Olá {user_data['name']}, seu e-mail é {user_data['email']}. Sua senha atual é {user_data['password']}"
        pass
    
    def go_to_login(self, instance):
        self.manager.current = 'first'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        first_screen = DadosProcesso(name='first')
        second_screen = EstatScreen(name='second')
        sm.add_widget(first_screen)
        sm.add_widget(second_screen)
        return sm


if __name__ == '__main__':
    MyApp().run()
