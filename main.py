import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()

botToken = os.getenv('BOTTOKEN')

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.tree.command(name="hello", description="Say Hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello World!", ephemeral=True)

@bot.tree.command(name="order", description="Bestelle eine Bibel!")
async def order(
    interaction: discord.Interaction,
    anrede: str,
    vorname: str,
    nachname: str,
    straße_hausnummer: str,
    postleitzahl: str,
    stadt: str,
    email: str,
    warum: str
):
    # Your logic to handle the order goes here.
    print(anrede, vorname, nachname, straße_hausnummer, postleitzahl, stadt, email, warum)

@bot.event
async def on_ready():
    print("Bot logged in.")
    try:
        # Register slash commands for all guilds
        for guild in bot.guilds:
            synced = await bot.tree.sync()
            print(f"Synced {len(synced)} commands for Guild ID: {guild.id}")
    except Exception as e:
        print(e)

bot.run(botToken)
