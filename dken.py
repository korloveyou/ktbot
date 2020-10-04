import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("섹스한다 이기야")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("할말")
    if message.content.startswith("시발"):
        await message.channel.send("어허")
    if message.content.startswith("좆까"):
        await message.channel.send("니좆")
    if message.content.startswith("병신"):
        await message.channel.send("니미요")
    if message.content.startswith("노무현"):
        await message.channel.send("이야 기분좋다~")
    if message.content.startswith("일베"):
        await message.channel.send("https://www.ilbe.com/")
    if message.content.startswith("네이버"):
        await message.channel.send("https://www.naver.com")
    if message.content.startswith("구글"):
        await message.channel.send("https://www.google.com")
    if message.content.startswith("폰허브"):
        await message.channel.send("https://pornhub.com")
        await message.channel.send("!vpn필수!")
    if message.content.startswith("들어와"):
        await message.channel.send("@everyone 들어와라 이기야")
        await message.channel.send("@everyone 들어와라 이기야")
        await message.channel.send("@everyone 들어와라 이기야")
        await message.channel.send("@everyone 들어와라 이기야")
        await message.channel.send("@everyone 들어와라 이기야")
        await message.channel.send("@everyone 들어와라 이기야")
    if message.content.startswith("섹스"):
        await message.channel.send("하핳 너무 아파요 살살해주요ㅠ")
    if message.content.startswith("!도움"):
        await message.channel.send("뭘 도와드릴까요?")
    if message.content.startswith("!ㅇㅁㅁ"):
        await message.channel.send("762172517938626591")

    if message.content.startswith("!구매"):
        await message.channel.send("넷플릭스 UHD")
        await message.channel.send("유튜브 프리미엄")
        await message.channel.send("랜덤계정")

    if message.content.startswith("!넷플릭스"):
        await message.channel.send("1개월 UHD - 8500원")
        await message.channel.send("4개월 UHD - 35000원")

    if message.content.startswith("!유튜브"):
        await message.channel.send("1개월 - 5000원")
        await message.channel.send("18개월 - 45000원")

    if message.content.startswith("!스포티파이"):
        await message.channel.send("1개월 - 7000원")
        await message.channel.send("12개월 - 70000원")

    if message.content.startswith("!랜덤계정"):
        await message.channel.send("```")


        #await message.channel.send("배그 - 6500원")
        #await message.channel.send("오버워치 - 7500원")
        #await message.channel.send("GTA5 - 4000원")

    if message.content.startswith("/DM"):
            author = message.guild.get_member(int(message.content[4:22]))
            msg = message.content[23:]
            await author.send(msg)

    if message.content.startswith('!전체디엠'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[5:]
                    embed = discord.Embed(title="제목", description=msg, color=0x3C54CD)
                    embed.set_author(name="이름", icon_url="아이콘사진")
                    embed.set_footer(text="아래쪽 텍스트")
                    embed.set_image(url="사진")
                    await i.send(embed=embed)
                except:
                    pass



client.run("NzYyMTUyNjQ0MjI2ODQyNjU0.X3k_9g.mBUkRYNcMwKybuW2VKWR450JGE8")

