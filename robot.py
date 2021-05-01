from cmd import cmd
import bot
while True:
	x=input('?/>')
	if bot.ory(x == 'exit',x == '?!exit,,!'):
		break
	cmd(x)