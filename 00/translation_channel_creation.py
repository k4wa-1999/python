from asyncio.windows_events import NULL
from discord.ext import commands
import discord
from libs.ch_make_embed import ch_make_msg
from libs.channel_make import cg_ch_make
from libs.db_control import search,change,dell

from data.bot_data import token

TOKEN = token


class MyBot(commands.Bot):
    async def com_up(self):
        await self.tree.sync(guild=None)


intents = discord.Intents.default()
intents.message_content = True
bot = MyBot(command_prefix="!", intents=intents,case_insensitive=True)

com_executing = []
db_name= "guild_info"
db_index = ["category","ch1_jp","ch2_en","ch3_cn","ch4_kr","ch5_th","ch6_id"]

print("翻訳BOT")

#DMは無視する。
@bot.check
async def globally_block_dms(ctx):
    return ctx.guild is not None


@bot.hybrid_command(description="翻訳チャンネルを作成します。",with_app_command=True)
@commands.has_permissions(administrator=True)
async def ch_make(ctx):
    await ctx.send("チャネルを作成します。")
    for guild_id in com_executing:
        if ctx.guild.id == guild_id[0]:
            await ctx.send("コマンドは既に実行されています。")
            return
    if len(search(db_name,ctx.guild.id)) == 0:
        com_executing.append([ctx.guild.id,NULL,NULL,NULL,NULL,NULL,NULL,NULL])
        embed = discord.Embed(title=f"使用する言語",color=0xCCFFFF)
        reaction_msg = await ch_make_msg(bot,embed,ctx.channel.id)
        for i,guild_info in enumerate(com_executing):
            if guild_info[0] == ctx.guild.id:
                com_executing[i][1] = reaction_msg.id
                return
    else:
        await ctx.send("チャンネルが既に存在します。")


@bot.hybrid_command(description="翻訳チャンネルを削除します。",with_app_command=True)
@commands.has_permissions(administrator=True)
async def ch_del(ctx):
    #同じuserか
    def check(msg):
        return msg.author == ctx.author

    await ctx.send("チャンネルを削除しまか？　y/n")
    msg = await bot.wait_for('message', check=check, timeout=30)
    if msg.content == "n":
        await ctx.send("チャンネルを削除を中断します。")
        return
    elif msg.content == "y":
        await ctx.send("チャンネルを削除します。")
        if len(search(db_name,ctx.guild.id)) == 0:
            await ctx.send("チャンネルがありません。")
        else:
            ch_id = search(db_name,ctx.guild.id)
            for i,id in enumerate(ch_id[0][2:]):
                if id == None:
                    continue
                del_ch = bot.get_channel(id)
                try:
                    await del_ch.delete()
                except AttributeError:
                    pass
                change(db_name,ctx.guild.id,db_index[i],"NULL")
            dell(db_name,ch_id[0][0])
            await ctx.send("チャンネルを削除しました！！")
    else:
        await ctx.send("不明な選択です。")
async def setup(bot):
    bot.add_command(ch_make,ch_del)

#追加するリアクション
reaction_data = ["🇯🇵","🇺🇸","🇨🇳","🇰🇷","🇹🇭","🇮🇩","🆗"]

@bot.event
async def on_reaction_add(reaction,user):
    if user.bot:
        return
    for com_i,msg_id in enumerate(com_executing):
        if reaction.message.id == msg_id[1]:
            for reaction_i,on_reaction in enumerate(reaction_data):
                if str(reaction)==on_reaction:
                    if str(reaction) == "🆗":
                        await reaction.message.delete()
                        await cg_ch_make(bot,user.guild,reaction,com_executing[com_i])
                        for i,guild_id in enumerate(com_executing):
                            if user.guild.id == guild_id[0]:
                                com_executing.pop(i)

                                
                    else:
                        com_executing[com_i][reaction_i+2]=(str(reaction))
                        await reaction.message.channel.send(f"{on_reaction}を追加しました。",delete_after=3.0)

#コマンドエラー処理
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions):
        await ctx.send("権限がありません。")




bot.run(TOKEN)