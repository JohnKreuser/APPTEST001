from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen

class MyApp(App):
    def build(self):
        self.sm = ScreenManager()  # Create a ScreenManager

        # Create screens
        for i in range(4):
            screen = Screen(name=f'Screen{i}')
            label = Label(text=f'Welcome to Screen {i + 1}')
            screen.add_widget(label)
            self.sm.add_widget(screen)

        # Create the main layout
        layout = BoxLayout(orientation='vertical')

        # Create ScreenManager and add it to the layout
        layout.add_widget(self.sm)

        # Create a layout for the bottom buttons
        buttons_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height=50)

        # Create buttons
        for i in range(4):
            button = Button(text=f'Screen {i + 1}', size_hint=(None, None), size=(100, 50))
            button.bind(on_press=lambda instance, screen_name=f'Screen{i}': self.switch_screen(screen_name))
            buttons_layout.add_widget(button)

        layout.add_widget(buttons_layout)

        return layout

    def switch_screen(self, screen_name):
        self.sm.current = screen_name

if __name__ == '__main__':
    Config.set('graphics', 'width', '270')  # Set width to match your phone's resolution
    Config.set('graphics', 'height', '585')  # Set height to match your phone's resolution
    MyApp().run()
