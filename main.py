import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!ping":
        await message.channel.send("Pong 🏓")

client.run(os.getenv("TOKEN"))

import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

@bot.command()
async def embed(ctx):
    emb = discord.Embed(
        title="📢 إعلان",
        description="أهلاً بك في السيرفر 🔥",
        color=discord.Color.blue()
    )

    emb.add_field(name="📌 القوانين", value="احترام الجميع", inline=False)
    emb.add_field(name="🎮 فعاليات", value="قريباً...", inline=False)

    emb.set_footer(text="بوت رهيب 😎")

    await ctx.send(embed=emb)

bot.run(os.getenv("TOKEN"))
