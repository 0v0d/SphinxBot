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
        area = data['area_name']
        embed.add_field(name=time, value=f"{area}の天気: {weather}", inline=False)
      await ctx.respond(embed=embed)
    else:
      await ctx.respond('天気情報を取得できませんでした。')


def get_weather(location_code: int):
  jma_json = requests.get(f"{url}{location_code}{json}").json()
  weather_data = []
  time_series = jma_json[0]["timeSeries"][0]
  time_defines = time_series["timeDefines"]
  areas = time_series["areas"]

  for day in range(len(time_defines)):
    time_define = time_defines[day]
    formatted_time = f'{time_define}'
    for area_num in range(len(areas)):
      area_data = areas[area_num]
      area_name = f'{area_data["area"]["name"]}'
      weather = f'{area_data["weathers"][day]}'
      weather_data.append({
        'time': f"{formatted_time[:10]} {formatted_time[11:16]}",
        'area_name': area_name.replace('　', ''),
        'weather': weather.replace('　', '')
      })
  return weather_data