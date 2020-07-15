from hoshino import R, Service, Privilege as Priv
import pytz
import random
from datetime import datetime


svcn = Service('买药小助手-cn', manage_priv=Priv.ADMIN, enable_on_default=False)


buyexpimg = R.img(f"priconne/买药小助手{random.randint(1, 2)}.jpg").cqcode



@svcn.scheduled_job('cron', hour='6, 12, 18, 0', minute='0')
async def buyexp_cn():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    await svcn.broadcast(f'[CQ:at,qq=all]咕噜灵波~骑士君别忘了买药噢~\n{buyexpimg}', 'pcr-reminder-cn', 0.2)