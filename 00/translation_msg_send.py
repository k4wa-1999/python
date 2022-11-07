import discord

from libs.translate_msg_send import tr_send
from libs.db_control import search

from data.bot_data import token
TOKEN = token

intents = intent=discord.Intents.all()
intents.members = True
intents.guilds = True
client = discord.Client(intents=intents)

db_name= "guild_info"

print("翻訳BOTメッセージ")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    Embed = discord.Embed
    guild = message.guild.id
    channel = message.channel.id
    if search(db_name,guild):
        guild_info = search(db_name,guild)[0]
        if channel in guild_info:
            await tr_send(db_name,client,Embed,guild,channel,message)
    
client.run(TOKEN)