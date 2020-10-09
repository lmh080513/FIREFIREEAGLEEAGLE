import discord

client = discord.Client()

@client .event
async def on_ready():
    print(client.user.id)
    print("ready")


@client.event
async def on_message(message):
    if message.content.startswitch("FIRE EAGLE소개"):
        await message.chennal.send("FIRE EAGLE은 GTA5 ONLINE의 에어쇼이며, 항공팀/ 지상팀/ 홍보팀으로 나누어져 있습니다.")


client.run("NzYzOTY1NDM3Mjk3MDMzMjI2.X3_YQg.lYSvcd_oasgFt1ECueQh2SIGcI8")




