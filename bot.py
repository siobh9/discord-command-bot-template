import discord
import os
import aiohttp
from dotenv import load_dotenv

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('members'):
        await message.channel.send('here are all of the members!')

@bot.slash_command(guild_ids=[891051215843098635])
async def hello(ctx):
    await ctx.respond("Hello!")

@bot.slash_command(guild_ids=[891051215843098635])
async def randomfact(ctx):
    # This will prevent your bot from stopping everything when doing a web request - see: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
    async with aiohttp.ClientSession() as session:
        async with session.get(
            "https://uselessfacts.jsph.pl/random.json?language=en"
        ) as request:
            if request.status == 200:
                data = await request.json()
                embed = discord.Embed(description=data["text"], color=0xD75BF4)
            else:
                embed = discord.Embed(
                    title="Error!",
                    description="There is something wrong with the API, please try again later",
                    color=0xE02B2B,
                )
            await ctx.respond(embed=embed)

load_dotenv() # so we can easily access the TOKEN env var
bot.run(os.getenv("TOKEN"))