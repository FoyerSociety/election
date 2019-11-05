import eel


options = {
	'mode' : 'custom',
	'args' : ['/usr/bin/electron', '.']
}

eel.init('view')



eel.start('home.html', position=(175,50), options=options)
