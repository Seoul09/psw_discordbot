from http import client
from json.tool import main
import discord 
from discord.ext import commands 
import requests
from bs4 import BeautifulSoup


app = commands.Bot(command_prefix='!') 

@app.event 
async def on_ready(): 
    print(app.user.name, '동아리 도움봇 준비 완료') 
    await app.change_presence(status=discord.Status.online, activity=None) 
    print("ready")
     

@app.command(name='공지')
async def roll(ctx):
    url = 'http://gnubs-h.gne.go.kr/gnubs-h/na/ntt/selectNttList.do?mi=529980&bbsId=5038685'

    # URL에서 HTML을 추출한다.
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('#subContent > div > div:nth-child(7) > div.board-text > table > tbody > tr:nth-child(1)')
        title = title.get_text()
        title = title.split()
        main_result = ''
        for i in title:
            main_result += i + ' '
        title = title[:-1]
        embed=discord.Embed(title="학교 공지 사항", description="학교에서 공지하는 알림 중 가장 최근 제목을 불러옵니다.")
        embed.add_field(name="공지사항", value=main_result, inline=True)
        await ctx.send(embed=embed)
    else :
        print(response.status_code)


@app.command(name='급식')
async def roll(ctx):
    # 추출할 사이트 주소
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B2%BD%EC%83%81%EA%B5%AD%EB%A6%BD%EB%8C%80%ED%95%99%EA%B5%90%EC%82%AC%EB%B2%94%EB%8C%80%ED%95%99%EB%B6%80%EC%84%A4%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90&oquery=%EA%B2%BD%EC%83%81%EA%B5%AD%EB%A6%BD%EB%8C%80%ED%95%99%EA%B5%90&tqi=hEpsjsp0JXVssbuCKKZssssssnZ-421774'

    # URL에서 HTML을 추출한다.
    response = requests.get(url)

    if response.status_code == 200:
        result = ''
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('#main_pack > div.sc_new.cs_common_module.case_normal.color_23._school.cs_kindergarten._edu_list > div.cm_content_wrap > div:nth-child(3) > div > div.scroll_box._button_scroller > div > div > ul > li:nth-child(1) > div')
        title = title.get_text()
        title = title.split()
        embed=discord.Embed(title="* 급식안내 *", description="- 최근 급식을 안내해줍니다 -", color=0x50b6d7)
        day = ''
        main_result = ''
        for i in title[3:]:
            main_result += i + '\n'
        print(main_result)
        for i in title[0:2]:
            day += i +' '
        embed.add_field(name=day, value=main_result, inline=False)
        await ctx.send(embed=embed)
@app.command(name='도움말')
async def roll(ctx):
    embed=discord.Embed(title="봇 안내", description="이 봇은 PSW 동아리에서 크롤링을 이용하여 학교 정보 가공하기 프로젝트를 진행한 봇입니다.", color=0xffffff)
    embed.add_field(name="/급식", value="제일 최근 급식을 불러와 보여줍니다.", inline=True)
    embed.add_field(name="/공지", value="제일 최근 학교 공지사항 제목을 불러와 알려드립니다!", inline=True)
    await ctx.send(embed=embed)


app.run('ODM4OTcwNDA4MDk0NjYyNjY2.Ggy1Pn.NcNl31p9OK-rEsTLBDZu_ln8cQc11BG7BJH5sI')
