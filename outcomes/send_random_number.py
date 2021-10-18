import random

async def main(ctx):
    await ctx.send(f"Here's your random number: {random.randint(-10000, 10000)}")