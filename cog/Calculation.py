from discord.ext import commands


class Calculator(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  ZERO_DIVISION_ERROR_MESSAGE = "0で割ることはできません。別の数値を入力してください。"

  @commands.slash_command(description="加算")
  async def add(self, ctx, a: float, b: float):
    await ctx.respond(f"結果は{a + b}")

  @commands.slash_command(description="減算")
  async def sub(self, ctx, a: float, b: float):
    await ctx.respond(f"結果は{a - b}")

  @commands.slash_command(description="乗算")
  async def mul(self, ctx, a: str, b: str):
    await ctx.respond(f"結果は{a * b}")

  @commands.slash_command(description="除算")
  async def div(self, ctx, a: float, b: float):
    #0の時エラー
    if a == 0:
      return await ctx.respond(self.ZERO_DIVISION_ERROR_MESSAGE)
    await ctx.respond(f"結果は{a / b}")

  @commands.slash_command(description="商算")
  async def mod(self, ctx, a: float, b: float):
    #0の時エラー
    if a == 0:
      return await ctx.respond(self.ZERO_DIVISION_ERROR_MESSAGE)
    await ctx.respond(f"結果は{a % b}")