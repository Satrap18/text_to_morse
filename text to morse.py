while True:
	string = input('Enter Text:').upper()
	tr = tuple(string)
	all = []
	
	for i in tr:
		if i == 'A':
			all.append('.-')
		elif i == 'B':
			all.append('-...')
		elif i == 'C':
			all.append('-.-.')
		elif i == 'D':
			all.append('-..')
		elif i == 'E':
			all.append('.')
		elif i == 'F':
			all.append('..-.')
		elif i == 'G':
			all.append('--.')
		elif i == 'H':
			all.append('....')
		elif i == 'I':
			all.append('..')
		elif i == 'J':
			all.append('.---')
		elif i == 'K':
			all.append('-.-')
		elif i == 'L':
			all.append('.-..')
		elif i == 'M':
			all.append('--')
		elif i == 'N':
			all.append('-.')
		elif i == 'O':
			all.append('---')
		elif i == 'P':
			all.append('.--.')
		elif i == 'Q':
			all.append('--.-')
		elif i == 'R':
			all.append('.-.')
		elif i == 'S':
			all.append('...')
		elif i == 'T':
			all.append('-')
		elif i == 'U':
			all.append('..-')
		elif i == 'V':
			all.append('...-')
		elif i == 'W':
			all.append('.--')
		elif i == 'X':
			all.append('-..-')
		elif i == 'Y':
			all.append('-.--')
		elif i == 'Z':
			all.append('--..')
		elif i == '0':
			all.append('-----')
		elif i == '1':
			all.append('.----')
		elif i == '2':
			all.append('..---')
		elif i == '3':
			all.append('...--')
		elif i == '4':
			all.append('....-')
		elif i == '5':
			all.append('.....')
		elif i == '6':
			all.append('-....')
		elif i == '7':
			all.append('--...')
		elif i == '8':
			all.append('---..')
		elif i == '9':
			all.append('----.')
		elif i == ':':
			all.append('---...')
		elif i == '=':
			all.append('-...-')
		elif i == '.':
			all.append('.-.-.-')
		
	print(" ".join(all))