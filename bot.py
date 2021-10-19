import os, random
from dotenv import load_dotenv

from discord.ext import commands

bot = commands.Bot()

@bot.command(name="random")
async def random_(ctx):
    outcomes = os.path.join(os.getcwd(), "outcomes")
    file = random.choice(os.listdir(outcomes))
    file = os.path.join(outcomes, file)
    with open(file, "r") as f:
        exec(f.read(), globals())
        await main(ctx)


if __name__ == "__main__":
    load_dotenv()
    bot.run(os.getenv("TOKEN"))
