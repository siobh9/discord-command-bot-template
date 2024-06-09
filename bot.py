import discord, os, aiohttp
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# EVENTS

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# REGULAR COMMANDS (are prefixed by command_prefix)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command.")

# SLASH COMMANDS

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

# LOADING

load_dotenv() # so we can easily access the TOKEN env var
bot.run(os.getenv("TOKEN"))