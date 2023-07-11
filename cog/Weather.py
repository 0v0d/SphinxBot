import os

import discord
import requests as requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.environ.get("API_KEY")
url:str = "http://api.openweathermap.org/data/2.5/"


class Weather(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="現在の天気情報")
    async def weather_now(self, ctx, location):
        weather_data = get_weather(str(location) + ',JP')
        if weather_data:
            weather = weather_data['weather'][0]['description']
            temp = weather_data['main']['temp']
            embed = discord.Embed(title=f"{location}の天気", color=discord.Color.blue())
            embed.add_field(name="現在", value=f"天気:{weather}/" f" 気温: {temp}℃", inline=False)
            await ctx.respond(embed=embed)
        else:
            await ctx.respond(f'{location}の天気を取得できませんでした。')

    @commands.slash_command(description="4日間の天気情報")
    async def weather_daily(self, ctx, location):
        weather_data = get_daily_weather(str(location) + ',JP')

        if weather_data:
            embed = discord.Embed(title=f"{location}の天気予報", color=discord.Color.blue())
            for data in weather_data:
                time = data['time']
                temperature = data['temperature']
                weather = data['weather']
                embed.add_field(name=time, value=f"天気: {weather} / 気温: {temperature}℃", inline=False)
            await ctx.respond(embed=embed)
        else:
            await ctx.respond('天気情報を取得できませんでした。')


def get_weather(location):
    response = requests.get(f'{url}weather?q={location}&units=metric&appid={API_KEY}')
    if response.status_code == 200:
        return response.json()
    else:
        print('エラー')
        return None


def get_daily_weather(location):
    response = requests.get(f"{url}forecast?q={location}&units=metric&appid={API_KEY}")
    if response.status_code == 200:
        data = response.json()
        weather_data = []

        for forecast in data['list']:
            time = forecast['dt_txt']
            temperature = forecast['main']['temp']
            weather = forecast['weather'][0]['description']
            weather_data.append({
                'time': time,
                'temperature': temperature,
                'weather': weather})
        return weather_data
    else:
        print('エラー')
        return None
