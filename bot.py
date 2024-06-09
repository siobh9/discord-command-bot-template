import discord, os
from discord.ext import commands
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.slash_command(guild_ids=[891051215843098635])
async def hello(ctx):
    await ctx.respond("Hello!")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command.")

load_dotenv() # so we can easily access the TOKEN env var
bot.run(os.getenv("TOKEN"))