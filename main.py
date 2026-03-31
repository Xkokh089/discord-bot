import discord
from discord import app_commands
from discord.ext import commands
import os

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)

# لما يشتغل البوت
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

# أمر الامبيد
@bot.tree.command(name="embed", description="سوي امبيد بنفسك")
@app_commands.describe(
    title="العنوان",
    description="الوصف",
    image="رابط صورة (اختياري)",
    color="لون Hex مثل FF0000 (اختياري)"
)
async def embed(
    interaction: discord.Interaction,
    title: str,
    description: str,
    image: str = None,
    color: str = None
):
    # اللون
    try:
        color = int(color, 16) if color else 0x3498db
    except:
        color = 0x3498db

    emb = discord.Embed(
        title=title,
        description=description,
        color=color
    )

    # الصورة (اختياري)
    if image:
        emb.set_image(url=image)
        
    # الفوتر التلقائي
    emb.set_footer(text="Made by PAĮN")

    # إرسال الامبيد
    await interaction.response.send_message(embed=emb)

# تشغيل البوت
bot.run(os.getenv("TOKEN"))
