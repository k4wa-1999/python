lang_list = [
    [":flag_jp:","Japan"],
    [":flag_us:","America"],
    [":flag_cn:","China"],
    [":flag_kr:","Korea"],
    [":flag_th:","Thailand"],
    [":flag_id:","India"]
]
emoji_data = ["🇯🇵","🇺🇸","🇨🇳","🇰🇷","🇹🇭","🇮🇩","🆗"]

async def ch_make_msg(client,embed,msg_send_ch):
    #embed = discord.Embed(title=f"{title_name}",color=0xCCFFFF)
    for i in range(len(lang_list)):
        embed.add_field(name=f"{lang_list[i][0]}",value=f"{lang_list[i][1]}",inline=False)
    message_send_channel = client.get_channel(msg_send_ch)
    reaction_message = await message_send_channel.send(embed=embed)
    for reaction_number in range(len(emoji_data)):
        await reaction_message.add_reaction(emoji_data[reaction_number])
    return reaction_message