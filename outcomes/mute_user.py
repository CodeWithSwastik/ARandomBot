import random
import asyncio

async def main(ctx):
    role = ctx.guild.get_role(766469426429820949)
    await ctx.message.author.add_roles(role)
    await ctx.send(f"lol get muted {ctx.message.author.mention}")
    await asyncio.sleep(random.randint(5, 60))
    await ctx.message.author.remove_roles(role)
