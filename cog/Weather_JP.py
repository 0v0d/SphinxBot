from typing import Any

import discord
import requests as requests
from discord.ext import commands

from cog.Utility import extract_value_from_map

url: str = "https://www.jma.go.jp/bosai/forecast/data/forecast/"
json: str = '.json'
location_map = {
  "大阪": 270000,
  "奈良": 290000,
  "三重": 240000,
}


class Weather_JP(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.slash_command(description="天気情報")
  async def weather_tomorrow(
    self, ctx, location: discord.Option(str, choices=['大阪', '三重', '奈良'])):
    weather_data = get_weather(extract_value_from_map(location, location_map))
    if weather_data:
      embed = discord.Embed(title=f'{location}の天気予報',
                            color=discord.Color.blue())
      for data in weather_data:
        time = data['time']
        weather = data['weather']
        embed.add_field(name=time, value=f"天気: {weather}", inline=False)
      await ctx.respond(embed=embed)
    else:
      await ctx.respond('天気情報を取得できませんでした。')


def get_weather(location_code: int):
  jma_json = requests.get(f"{url}{location_code}{json}").json()
  weather_data = []
  range_: int = len(jma_json[0]["timeSeries"][0]["timeDefines"])
  for i in range(range_):
    time = f'{jma_json[0]["timeSeries"][0]["timeDefines"][i]}'
    weather = f'{jma_json[0]["timeSeries"][0]["areas"][0]["weathers"][i]}'
    weather_data.append({
      'time': f"{time[:10]} {time[11:16]}",
      'weather': weather.replace('　', '')
    })
  return weather_data
