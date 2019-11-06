import eel
import sys

options = {
	'mode' : 'custom',
	'args' : ['/usr/bin/electron' if sys.platform == 'linux' else '', '.']
}

eel.init('view')

@eel.expose
def test ():
	print('test')

def main():
	eel.start('home.html', position=(175,50), options=options)


if __name__ == '__main__':
	main()
