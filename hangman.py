def hangman(word):
	wrong=0
	stages=["",
		"_________     ",
		"              ",
		"        |     ",
		"        0     ",
		"      / | \    ",
		"       / \     ",
		"               "]
	rieletters = list(word)
	board = ["_"] * len(word)
	print("Welcom")
	win = False
	while wrong < len(stages) - 1:
		msq = 'Input letter '
		char = input(msq)
		if char in rieletters:
			cind = rieletters.index(char)
			board[cind] = char
			rieletters[cind] = "$"
		else:
			wrong +=1
		print (' '.join(board))
		e = wrong + 1
		print('\n'.join(stages[0: e]))
		if "_" not in board:
			print ('You win')	 
			win = True
			break
	if not win:
		print('\n'.join(stages[0: e]))
		print('You lose')
hangman("Каракатица")
