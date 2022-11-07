from asyncio.windows_events import NULL
from libs.db_control import add,change,search
import discord
# ch1_jp,ch2_en,ch3_cn,ch4_kr,ch5_th,ch6_id
reaction_data = ["🇯🇵","🇺🇸","🇨🇳","🇰🇷","🇹🇭","🇮🇩"]
db_index = ["ch1_jp","ch2_en","ch3_cn","ch4_kr","ch5_th","ch6_id"]
db_name= "guild_info"

#role = await client.create_role(author.server, name=role_name, colour=discord.Colour(0x0000FF))
async def cg_ch_make(client,guild,reaction,com_executing):
    guild_id = guild.id
    if len(search(db_name,guild_id)) == 0:
        Category = await guild.create_category("translation_ch")
        await Category.set_permissions(guild.default_role, read_messages=False,send_messages=False)
        add(db_name,guild.id,Category.id)
        for i,lang in enumerate(com_executing[2:]):
            if lang == NULL:
                continue
            else:
                p_roll = await guild.create_role(name=f'{db_index[i]}', permissions=discord.Permissions(permissions=0), colour=0xffffff)
                ch = await guild.create_text_channel(f"{reaction_data[i]}", category = Category)
                await ch.set_permissions(p_roll, read_messages=True,send_messages=True)
                change(db_name,guild.id,db_index[i],ch.id)
        await reaction.message.channel.send("チャンネルを作成しました！！")