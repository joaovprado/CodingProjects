from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

        self.name_input = TextInput(hint_text='Nome')
        self.email_input = TextInput(hint_text='Email')
        self.password_input = TextInput(hint_text='Senha', password=True)

        self.register_button = Button(text='Cadastrar')
        self.register_button.bind(on_press=self.register)
        self.login_button = Button(text='Logar')
        self.login_button.bind(on_press=self.login)

        self.layout.add_widget(self.name_input)
        self.layout.add_widget(self.email_input)
        self.layout.add_widget(self.password_input)
        self.layout.add_widget(self.register_button)
        self.layout.add_widget(self.login_button)

    def register(self, instance):
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text
        App.get_running_app().user_data = {'name': name, 'email': email, 'password': password}
        self.manager.current = 'welcome'

    def login(self, instance):
        self.manager.current = 'welcome'

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.add_widget(self.layout)

        self.welcome_label = Label(text='Bem-vindo')
        self.layout.add_widget(self.welcome_label)

        self.back_button = Button(text='Voltar para o Login')
        self.back_button.bind(on_press=self.go_to_login)
        self.layout.add_widget(self.back_button)

    def on_pre_enter(self):
        user_data = App.get_running_app().user_data
        self.welcome_label.text = f"Olá {user_data['name']}, seu e-mail é {user_data['email']}. Sua senha atual é {user_data['password']}"

    def go_to_login(self, instance):
        self.manager.current = 'login'


class MyApp(App):
    def build(self):
        sm = ScreenManager()
        login_screen = LoginScreen(name='login')
        welcome_screen = WelcomeScreen(name='welcome')
        sm.add_widget(login_screen)
        sm.add_widget(welcome_screen)
        return sm

if __name__ == '__main__':
    MyApp().run()
