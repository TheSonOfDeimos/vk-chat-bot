import requests
from bs4 import BeautifulSoup


class Weather:
    @staticmethod
    def get_weather_today(city: str = "санкт-петербург") -> list:

        http = "https://sinoptik.com.ru/погода-" + city
        b = BeautifulSoup(requests.get(http).text, "html.parser")

        # p3 = b.select('.temperature .p3')
        # weather1 = p3[0].getText()

        all_temperature = b.find_all(class_= 'table__temp')
        temperature_night = all_temperature[1].getText()
        temperature_morning = all_temperature[3].getText()
        temperature_day = all_temperature[5].getText()
        temperature_evening = all_temperature[7].getText()

        result = ''
        result = result + ('Ночью : ' + temperature_night) + '\n'
        result = result + ('Утром : ' + temperature_morning) + '\n'
        result = result + ('Днем : ' + temperature_day) + '\n'
        result = result + ('Вечером : ' + temperature_evening) + '\n'

        weathre_discription_1 = b.find_all(class_= 'weather__article_description-text')[0].getText()
        weathre_discription_2 = b.find_all(class_= 'weather__article_forecast-text')[0].getText()
        
        result = result + '\n' + weathre_discription_1.strip() + '\n \n' + weathre_discription_2.strip()

        return result
