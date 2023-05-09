from discord.ext import commands


class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    ARGUMENTS_ERROR_MESSAGE = "引数が少なすぎます。2つ以上の数値を入力してください。"
    NUMERIC_ERROR_MESSAGE = "数値以外の入力がありました。数値を入力してください。"
    ZERO_DIVISION_ERROR_MESSAGE = "0で割ることはできません。別の数値を入力してください。"

    async def check_args(self, ctx, a, b):
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            await ctx.respond(self.NUMERIC_ERROR_MESSAGE)
            return None
        return a, b

    @commands.slash_command()
    async def add(self, ctx, a: str, b: str):
        numbers = await self.check_args(ctx, a, b)
        if numbers is None:
            return
        result = sum(numbers)
        await ctx.respond(f"結果は{result}")

    @commands.slash_command()
    async def sub(self, ctx, a: str, b: str):
        numbers = await self.check_args(ctx, a, b)
        if numbers is None:
            return
        result = numbers[0] - numbers[1]
        await ctx.respond(f"結果は{result}")

    @commands.slash_command()
    async def mul(self, ctx, a: str, b: str):
        numbers = await self.check_args(ctx, a, b)
        if numbers is None:
            return
        result = numbers[0] * numbers[1]
        await ctx.respond(f"結果は{result}")

    @commands.slash_command()
    async def div(self, ctx, a: str, b: str):
        numbers = await self.check_args(ctx, a, b)
        if numbers is None:
            return
        if numbers[1] == 0:
            await ctx.respond(self.ZERO_DIVISION_ERROR_MESSAGE)
            return
        result = numbers[0] / numbers[1]
        await ctx.respond(f"結果は{result}")

