from django import template
from pathlib import Path
import qrcode
import json
import time


register = template.Library()

users = [
    {
        'course': 'МП-301',
        'last_name': 'Гражданко',
        'first_name': 'Кирилл',
        'middle_name': 'Генадьевич',
        'login': 'admin',
        'pass': 'password',
        'points': 10000182,
    },
    {
        'course': 'МП-302',
        'login': 'usr1',
        'pass': 'pass1',
        'last_name': 'Корчагина',
        'first_name': 'Екатерина',
        'middle_name': 'Сергеевна',
        'points': 506,
    },
    {
        'course': 'МН-302',
        'login': 'usr2',
        'pass': 'pass2',
        'last_name': 'Ефремова',
        'first_name': 'Елизавета',
        'middle_name': 'Владимировна',
        'points': 1026,
    },
    {
        'course': 'МП-302',
        'login': 'usr3',
        'pass': 'pass3',
        'last_name': 'Павлов',
        'first_name': 'Даниэль',
        'middle_name': 'Владимирович',
        'points': 102,
    },
]


@register.simple_tag(takes_context=True)
def generateQR(context):
    data = {
        'course': getInfo(context, 'course'),
        'first_name': getInfo(context, 'first_name'),
        'middle_name': getInfo(context, 'middle_name'),
        'last_name': getInfo(context, 'last_name'),
        'timestamp': time.time(),
    }

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4
    )

    obj = json.dumps(data, ensure_ascii=False)

    qr.add_data(obj)
    qr.make(fit=True)
    img = qr.make_image()
    
    Path("static/QR/Pictures").mkdir(parents=True, exist_ok=True)
    img.save('static/QR/Pictures/' + getInfo(context, 'login') + '_QR.png')
    return ''


@register.tag(name="info")
@register.simple_tag(takes_context=True)
def getInfo(context, info):
    login = context['request'].session.get('Login', True)
    for i in users:
        if login == i.get('login'):
            return i.get(info)


@register.simple_tag(takes_context=False)
def schedule():
    content = {
        'Понедельник': [
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
        ],
        'Вторник': [
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
        ],
        'Среда': [
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
        ],
        'Четверг': [
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
        ],
        'Пятница': [
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
        ],
        'Суббота': [
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
            {
                'Start': '13:15',
                'End': '14:45',
                'Name': 'Ин. яз.',
                'Cabinet': '1к. ауд. 417',
                'Lecturer': 'Иванов И. А',
            },
        ],
    }

    result = ""
    for i in content:
        result += """
		<div class="day">
			<p class="weekday">"""+i+"""</p>"""
        for j in content.get(i):
            result += """
			<div class="lesson">
				<div class="time">
					<span class="start_time">"""+j.get('Start')+"""</span>
					<span class="end_time">"""+j.get('End')+"""</span>
				</div>
				<div class="info">
					<span>"""+j.get('Name')+"""</span>
					<span>"""+j.get('Cabinet')+"""</span>
				</div>
				<div class="lecturer">
					<span>"""+j.get('Lecturer')+"""</span>
				</div>
			</div>
			"""
        result += """</div>"""
    return result

    # <div class="day">
    # <p class="weekday">Понедельник</p>
    # <div class="lesson">
    # <div class="time">
    # <span class="start_time">13:15</span>
    # <span class="end_time">14:45</span>
    # </div>
    # <div class="info">
    # <span>Ин. яз.</span>
    # <span>1к. ауд. 417</span>
    # </div>
    # <div class="lecturer">
    # <span>Иванов И.А.</span>
    # </div>
    # </div>
    # </div>
