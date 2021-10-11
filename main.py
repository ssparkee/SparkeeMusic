import discord
import os
from replit import db
from discord.ext import commands
import music

cogs = [music]
client = commands.Bot(command_prefix="?", intents = discord.Intents.all())
token = os.environ['TOKEN']

for i in range(len(cogs)):
  cogs[i].setup(client)

client.run(token)