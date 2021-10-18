import random

async def main(ctx):
    m = random.choice(ctx.guild.members)
    await ctx.send(f"Here's a random member: {m.mention}")