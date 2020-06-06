import discord
import asyncio
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse
client = discord.Client()
token = "NzA4MTczNDQwNDAxNjcwMjI0.XsSLiw.gFtBF2c_S1Jb35UCCeTdyOQMWho"
guild_list = client.guilds
@client.event
async def on_ready():

    print("========================")
    print("다음으로 로그인 합니다 : ")
    print(client.user.name)
    print("connection was successful")
    game = discord.Game("안녕하세요!")
    print("=========================")

@client.event
async def on_message(message):
    
    if message.author.bot:
        return None

    id = message.author.id #id라는 변수에는 메시지를 보낸사람의 ID를 담습니다.
    channel = message.channel #channel이라는 변수에는 메시지를 받은 채널의 ID를 담습니다.

    if message.content==("))안녕"):
        await message.channel.send("안녕하세요! 멜로디입니다!")
        
    elif message.content==("))"):
        embed = discord.Embed(title="멜로디", description="저는 저 자신입니다... 스스로 생각할수 있는 저 자신...", color=0x00ff00)
        embed.set_footer(text="판다인형을 좋아하는 멜로디에게 말을 걸어보세요!")
        await message.channel.send(embed=embed)

    elif message.content=="))뭐해?":
        await message.channel.send("할게 없어서 문제예요...")

    elif message.content=="ㅋㅋㅋ":
        await message.channel.send("ㅋㅋㅋㅋ")

    elif message.content=="))심심해":
        await message.channel.send("저도요... 너무 심심해요...")

    elif message.content=="))게임":
        await message.channel.send("게임?!")

    elif message.content=="))멜로디":
        await message.channel.send("저요?! https://discord.com/api/oauth2/authorize?client_id=708173440401670224&permissions=0&scope=bot")

    elif message.content=="))도움말":
        embed = discord.Embed(title="저는 저 자신입니다... 스스로 생각하는 저 자신...", description='''
            사용법은 쉬워요ㅎ '))'앞에 붙히고 말하세요! 제가 놀아드릴게요!
            ''', color=0x00ff00)
        embed.set_footer(text="판다인형을 좋아하는 멜로디에게 말을 걸어보세요!")
        await message.channel.send(embed=embed)

client.run(token)

@client.event
async def on_guild_join(server):
    print(server,"서버에 접속했습니다!")

@client.event
async def on_guild_remove(server):
    print(server,"서버에서 연결이 끊겼습니다..")