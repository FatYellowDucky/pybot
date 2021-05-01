import bot
import os
def cmd(cmd):
	cmd=str(cmd).split()
	res={
		'hello': 'hi',
		'hi': 'hello',
		'bored':'not me',
		'$?version?': '1.0',
		'$?len?': 'en-gb'
	}
	try:
		if cmd[0] == 'say':
			print('?bot/>'+res[cmd[1]])
		elif cmd[0] == 'j,,i':
			print('j,,i!'+res['$?len?']+'!'+res['$?version?'])
		elif cmd[0] == 'support?':
			print('?support/>'+'python 3.8.2 or higher')
		elif cmd[0] == 'info?':
			bot.info(cmd[1])
		elif cmd[0] == 'cls':
			if os.name == 'nt':
				os.system('cls')
			else:
				os.system('clear')
		else:
			print('?bot/>'+str(cmd)+' not valied')
	except Exception as err:
		bot.find_error(IndexError)