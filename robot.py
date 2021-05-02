from cmd import cmd
import bot
while True:
	x=input('?/>')
	if bot.or_(x == 'exit',x == '?!exit,,!'):
		break
	cmd(x)