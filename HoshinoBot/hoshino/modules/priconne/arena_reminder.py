from hoshino.service import Service
from hoshino import R

svcn = Service('pcr-arena-reminder-cn', enable_on_default=False)
svjp = Service('pcr-arena-reminder-jp', enable_on_default=False)
msg = f'骑士君，准备好背刺了吗？{R.img("priconne/beici.jpg").cqcode}'

@svcn.scheduled_job('cron', hour='14', minute='45')
async def pcr_reminder_cn():
    await svcn.broadcast(msg, 'pcr-reminder-cn', 0.2)

@svjp.scheduled_job('cron', hour='13', minute='45')
async def pcr_reminder_jp():
    await svjp.broadcast(msg, 'pcr-reminder-jp', 0.2)
