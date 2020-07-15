import nonebot
import json

from datetime import timedelta
from hoshino.service import Service
from quart import request,session,redirect,Blueprint
from .data_source import render_template,get_random_str

switcher = Blueprint('switcher',__name__)
bot = nonebot.get_bot()
app = bot.server_app
if not app.config.get('SECRET_KEY'):
    app.config['SECRET_KEY'] = get_random_str(10)

public_address = '106.53.224.154' #改为你服务器的公网ip,域名应该也可以，我没试过
port = bot.config.PORT
passwd = 'wa102612' #登录密码

@switcher.before_request
async def _():
    user_ip = request.remote_addr
    if request.path == '/login':
        return
    if request.path == '/check':
        return
    if session.get('user_ip') == user_ip:
        return
    return redirect('/login') 

@switcher.route('/login',methods=['GET','POST'])
async def login():
    print(request.method)
    if request.method == 'GET':
        return await render_template('login.html',passwd=passwd,public_address=public_address,port=port)
    else:
        login_data = await request.form
        input_psd = login_data.get('password')
        if input_psd == passwd:
            user_ip = request.remote_addr
            session['user_ip'] = user_ip
            session.permanent = True
            app.permanent_session_lifetime = timedelta(weeks=2)
            return redirect('/manager')
        else:
            return redirect('/login')

@switcher.route('/manager')
async def manager():
    return await render_template('main.html',public_address=public_address,port=port)

@switcher.route('/group')
async def test():
    groups = await get_groups()
    return await render_template('by_group.html',items=groups,public_address=public_address,port=port)

@switcher.route('/service')
async def show_all_services():
    svs = Service.get_loaded_services()
    sv_names = list(svs)
    return await render_template('by_service.html',items=sv_names,public_address=public_address,port=port)

@switcher.route('/group/<gid_str>')
async def show_group_services(gid_str:str):
    #group_svs = get_group_services(int(gid))
    gid = int(gid_str)
    svs = Service.get_loaded_services()
    conf = {}
    conf[gid_str] = {}
    for key in svs:
        conf[gid_str][key] = svs[key].check_enabled(gid)
    return await render_template('group_services.html',group_id=gid_str,conf=conf,public_address=public_address,port=port)

@switcher.route('/service/<sv_name>')
async def show_service_groups(sv_name:str):
    svs = Service.get_loaded_services()
    groups = await get_groups()
    conf = {}
    for group in groups :
        gid = group['group_id']
        gid_str = str(gid)
        conf[gid_str] = {}
        if svs[sv_name].check_enabled(gid):
            conf[gid_str][sv_name] = True
        else:
            conf[gid_str][sv_name] = False
    return await render_template('service_groups.html',sv_name=sv_name,conf=conf,groups=groups,public_address=public_address,port=port)

async def get_groups():
    return await bot.get_group_list()

@switcher.route('/set/',methods=['GET','POST'])
async def set_group():
    #接收前端传来的配置数据，数据格式{"10000":{'serviceA':True,'serviceB':False}}
    if request.method == 'POST':
        data = await request.get_data()
        conf = json.loads(data.decode())
    svs = Service.get_loaded_services()
    for k in conf:
        gid = int(k)
        for sv_name in conf[k]:
            if conf[k][sv_name]:
                svs[sv_name].set_enable(gid)
            else:
                svs[sv_name].set_disable(gid)
    return 'ok'


@bot.on_message('private')
async def setting(ctx):
    message = ctx['raw_message']
    if message == 'bot设置':
        await bot.send(ctx,f'http://{public_address}:{port}/manager',at_sender=False)
