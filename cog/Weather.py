import os

import discord
import requests as requests
from discord.ext import commands

API_KEY = os.environ.get("API_KEY")


class Weather(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command()
  async def weather_now(self, ctx, location):
    weather = get_weather(str(location) + ',JP')
    if weather:
      response = '{} 現在の天気:{} 気温:{}度'.format(
        location, weather['weather'][0]['description'],
        weather['main']['temp'])
    else:
      response = f'{location}の天気を取得できませんでした。'
    await ctx.respond(response)

  @commands.slash_command()
  async def weather_daily(self, ctx, location):
    weather_data = get_daily_weather(str(location) + ',JP')

    if weather_data:
      embed = discord.Embed(title=f"{location}の天気予報",
                            color=discord.Color.blue())
      for data in weather_data:
        time = data['time']
        temperature = data['temperature']
        weather = data['weather']
        embed.add_field(name=time,
                        value=f"天気: {weather} / 気温: {temperature}℃",
                        inline=False)
      await ctx.respond(embed=embed)
    else:
      await ctx.respond('天気情報を取得できませんでした。')


def get_weather(location):
  response = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={API_KEY}'
  )
  if response.status_code == 200:
    return response.json()
  else:
    print('エラー')
    return None


def get_daily_weather(location):
  response = requests.get(
    f"http://api.openweathermap.org/data/2.5/forecast?q={location}&units=metric&appid={API_KEY}"
  )
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
        'weather': weather
      })
    return weather_data
  else:
    print('エラー')
    return None
