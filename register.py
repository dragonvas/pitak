from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3


# Загружаем интерфейс из файла .kv
Builder.load_file("register.kv")
Builder.load_file("register_suc.kv")


class RegisterScreen(Screen):
    def register_user(self):
        login = self.ids.login.text
        passw = self.ids.password.text
        passw_ag = self.ids.password_again.text

        conn = sqlite3.connect('pyatachok.db')
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO pyatachok (login, passw) VALUES (?, ?)',
                (login, passw)
                )
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            conn.close()
            return False

    def reg_button(self):
        login = self.ids.login.text
        passw = self.ids.password.text
        passw_ag = self.ids.password_again.text
        if passw == passw_ag:
            if passw != '' and login != '':
                # RegisterScreen.register_user(self)
                self.manager.current = 'register_suc'
            else:
                self.ids.koka.text = "Логин и пароль не могут быть пусты"
        else:
            self.ids.koka.text = "Пароли должны совподать"
class RegisterSucScreen(Screen):
    pass
class PytakApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(RegisterScreen(name='register'))
        sm.add_widget(RegisterSucScreen(name='register_suc'))
        return sm


if __name__ == "__main__":
    PytakApp().run()