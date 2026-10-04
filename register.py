from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import sqlite3


# Загружаем интерфейс из файла .kv
Builder.load_file("register.kv")


class RegisterScreen(Screen):
    def register_user(self):
        login = self.ids.login.text
        passw = self.ids.password.text
        passw_ag = self.ids.password_again.text
        if passw == passw_ag:
            conn = sqlite3.connect('pyatachok.db')
            cursor = conn.cursor()
            try:
                cursor.execute(
                    'INSERT INTO users (login, passw) VALUES (?, ?)',
                    (login, passw)
                )
                conn.commit()
                conn.close()
                return True
            except sqlite3.IntegrityError:
                conn.close()
                return False


        else:
            #Вставить ошибку о несовпадении паролей
            pass
    def test_button(self):
        # Здесь можно писать код для проверки кнопки
        self.ids.status.text = "Кнопка работает!"


class MyApp(App):
    def build(self):
        # Возвращаем экран приложения
        return RegisterScreen()


if __name__ == "__main__":
    MyApp().run()
