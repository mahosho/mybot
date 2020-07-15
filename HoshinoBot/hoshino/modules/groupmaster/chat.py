import random
from datetime import timedelta

from nonebot import on_command
from hoshino import util
from hoshino.res import R
from hoshino.service import Service, Privilege as Priv

# basic function for debug, not included in Service('chat')
@on_command('zai?', aliases=('在?', '在？', '在吗', '在么？', '在嘛', '在嘛？'))
async def say_hello(session):
    await session.send('咕噜灵波~')

sv = Service('chat', manage_priv=Priv.SUPERUSER, visible=False)

@sv.on_command('沙雕机器人', aliases=('沙雕機器人',), only_to_me=False)
async def say_sorry(session):
    await session.send('ごめんなさい！嘤嘤嘤(〒︿〒)')

@sv.on_command('box上报', only_to_me=False)
async def box(session):
    await session.send('152.136.113.143:2333')
    
@sv.on_command('老婆', aliases=('waifu', 'laopo'), only_to_me=True)
async def chat_waifu(session):
    if not sv.check_priv(session.ctx, Priv.SUPERUSER):
        await session.send(R.img('laopo.jpg').cqcode)
    else:
        await session.send('mua~')

@sv.on_command('老公', only_to_me=True)
async def chat_laogong(session):
    await session.send('这样很不礼貌噢！', at_sender=True)

@sv.on_command('mua', only_to_me=True)
async def chat_mua(session):
    await session.send('笨蛋~', at_sender=True)
    
@sv.on_command('咕噜灵波', only_to_me=True)
async def chat_gulu(session):
    await session.send('[CQ:record,file=咕噜灵波.mp3]')

@sv.on_command('请多指教', only_to_me=True)
async def chat_zhijiao(session):
    await session.send('[CQ:record,file=请多指教.m4a]')

@sv.on_command('早安', aliases=('早上好'),only_to_me=True)
async def chat_zaoan(session):
    await session.send('[CQ:record,file=早安.m4a]')


@sv.on_command('晚安', aliases=('晚上好'),only_to_me=True)
async def chat_oyasumi(session):
    await session.send('[CQ:record,file=晚安.m4a]')   

@sv.on_command('cygames', only_to_me=True)
async def chat_zaoan(session):
    await session.send('[CQ:record,file=cygames.m4a]')

@sv.on_command('小狐狸的告白魔法', only_to_me=True)
async def chat_zaoan(session):
    await session.send('[CQ:record,file=告白魔法.mp3]')
    
@sv.on_command('出货', aliases=('出货啦', '出货了'), only_to_me=True)
async def chat_zaoan(session):
    await session.send('[CQ:record,file=恭喜.m4a]')  

@sv.on_command('来点星奏', only_to_me=False)
async def seina(session):
    await session.send(R.img('星奏.png').cqcode)

@sv.on_command('我好了', only_to_me=False)
async def nihaole(session):
    await session.send('不许好，憋回去！')
    await util.silence(session.ctx, 30)

# ============================================ #

@sv.on_keyword(('朋友'))
async def pyhaole(bot, ctx):
    if random.random() < 0.20:
        await bot.send(ctx, f'那个朋友是不是你自己？', at_sender=True)

@sv.on_keyword(('确实', '有一说一', 'u1s1', 'yysy'))
async def chat_queshi(bot, ctx):
    if random.random() < 0.05:
        await bot.send(ctx, R.img('确实.jpg').cqcode)

@sv.on_keyword(('会战', '刀'))
async def chat_clanba(bot, ctx):
    if random.random() < 0.03:
        await bot.send(ctx, R.img('我的天啊你看看都几度了.jpg').cqcode)

@sv.on_keyword(('内鬼'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.10:
        await bot.send(ctx, R.img('内鬼.png').cqcode)

@sv.on_keyword(('咕噜灵波'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.20:
        await bot.send(ctx, R.img('小心咕噜灵波.jpg').cqcode)

@sv.on_keyword(('开心'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.20:
        await bot.send(ctx, R.img('真步开心.jpg').cqcode)     

@sv.on_keyword(('炮'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.20:
        await bot.send(ctx, R.img('光杀炮.jpg').cqcode)           

@sv.on_keyword(('街头', '接头'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.20:
        await bot.send(ctx, R.img('接头.jpg').cqcode)       

@sv.on_keyword(('魔法'))
async def chat_neigui(bot, ctx):
    if random.random() < 0.20:
        await bot.send(ctx, R.img('魔法.jpg').cqcode)