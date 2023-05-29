from discord.ext import commands

import random


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="ランダムな数字を生成")
    async def random(self, ctx, min_val:str,max_val:str):
        try:
            min_val = int(min_val)
            max_val = int(max_val)
        except ValueError:
            await ctx.respond('Error')
            return
        if min_val > max_val:
            await ctx.respond('小さいほうを先に書いてね')
            return
        await ctx.respond(f'{random.randint(min_val, max_val)}')