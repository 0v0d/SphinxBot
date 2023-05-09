import os

import requests as requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")

class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def weather(self, ctx, location):
        location = str(location)
        weather = get_weather(location + ',JP')
        if weather:
            response = '現在の{}の天気は{}です。気温は{}度、湿度は{}％です。'.format(location,
                                                                        weather['weather'][0]['description'],
                                                                        weather['main']['temp'],
                                                                        weather['main']['humidity'])
        else:
            response = 'その場所の天気を取得できませんでした。'

        await ctx.respond(response)


def get_weather(location):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print('接続問題')
        return None
