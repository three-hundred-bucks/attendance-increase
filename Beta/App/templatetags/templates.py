from django import template

register = template.Library()

# @register.simple_tag(takes_context = False)
@register.simple_tag()
def schedule(): # could feed in additional argument to use as default value
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