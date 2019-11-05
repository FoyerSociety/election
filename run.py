import eel


options = {
	'mode' : 'custom',
	'args' : ['/usr/bin/electron', '.']
}

eel.init('view')

def main():
	eel.start('home.html', position=(175,50),  options=options)


<<<<<<< HEAD
eel.start('home.html', position=(175,50), options=options)
=======
if __name__ == '__main__':
	main()
>>>>>>> fbcca7d38a510ca42a102daf35f866c3d9a29b4a
