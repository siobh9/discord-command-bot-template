import discord, os, aiohttp, random, json
from dotenv import load_dotenv

load_dotenv() # so we can easily access env vars
TOKEN = os.getenv("TOKEN")
GUILD_IDS = json.loads(os.getenv("GUILD_IDS"))

bot = discord.Bot()

# EVENTS

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

@bot.slash_command(guild_ids=GUILD_IDS)
async def ping(ctx):
    await ctx.respond("Pong!")

@bot.slash_command(guild_ids=GUILD_IDS)
async def gtn(ctx, guess:int):
    number = random.randint(1, 3)
    if guess == number:
        await ctx.send("You guessed it!")
    else:
        await ctx.send("Nope! Better luck next time :)")

@bot.slash_command(guild_ids=GUILD_IDS)
async def hello(ctx):
    await ctx.respond("Hello!")

@bot.slash_command(guild_ids=GUILD_IDS)
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

bot.run(TOKEN)