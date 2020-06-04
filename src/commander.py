from command_enum import Command
from mode_enum import Mode

from weather import Weather
from myanimelist import Myanimelist

class Commander:

    def __init__(self):

        # Текущий, предыдущий режимы
        self.now_mode = Mode.default
        self.last_mode = Mode.default

        self.last_command = None
        self.last_ans = None

    def change_mode(self, to_mode):
        self.last_mode = self.now_mode
        self.now_mode = to_mode
        self.last_ans = None

    def input(self, msg):
        # Проверка на команду смены мода
        if msg.startswith("/"):
            for mode in Mode:
                if msg[1::] in mode.value:
                    self.change_mode(mode)
                    return "Режим изменен на " + self.now_mode.value[0]
            return "Неизвестный мод " + msg[1::]

        # Режим получения ответа
        if self.now_mode == Mode.get_ans:
            self.last_ans = msg
            self.now_mode = self.last_mode
            return "Ok!"

        if self.now_mode == Mode.default:
            # Погода
            if msg in Command.weather.value:
                return Weather.get_weather_today()

            # Топ аниме
            if msg in Command.anime_top.value:
                res = ""
                top = Myanimelist.get_top()
                for anime in top:
                    res += anime + " : " + top[anime] + "\n"

                return res

        if self.now_mode == Mode.translate:
            return "Данная функция не доступна."

        return "Команда не распознана!"
