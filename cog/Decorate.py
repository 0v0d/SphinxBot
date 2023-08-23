import discord
from discord.ext import commands

class DecorateText(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def decorate_code(self, ctx, language: discord.Option(str,
    choices=['py', 'cpp', 'cs', 'java', 'cs', 'ts', 'js','md', 'diff']), code: str):
        await ctx.respond(f'```{language}\n{code}\n```')
