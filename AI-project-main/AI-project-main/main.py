from board import Board
import random 
from move import Move
from ai import AI

from os import system, name

STARTING_STATE_FEN = 'rheakaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RHEAKAEHR w - - 0 1'


# Helper function
def getMoveFromString(start, target, board):

	# Changing string to integer pos
	start = start.split(" ")
	target = target.split(" ")
	start_file, start_rank = int(start[0]), int(start[1])
	target_file, target_rank = int(target[0]), int(target[1])

	start = (start_file, start_rank)
	target = (target_file, target_rank)

	# Check if player's move was a capture
	# (will be trivial if player chooses moves from a list)
	if board.state[(target_rank-1)*9 + (target_file-1)] != "+":
		capture = True
	else:
		capture = False

	new_move = Move(start, target, capture)
	return new_move

# Clear screen helper function
def clear_screen():
	# For windows
	if name == 'nt':
		_ = system('cls')
 
	# For macOS and Linux (here, os.name is 'posix')
	else:
		_ = system('clear')


computer_color = ''

#human_color = input("Playing as w or b? ")

human_color = 'w'

if human_color == 'w':
	computer_color = 'b'
else:
	computer_color = 'w'




h=[]
game=[]
heuristicsALL=[]
for i in range (0,2):
	winner=0
	board = Board(STARTING_STATE_FEN, computer_color)
	board_userthreats = board.userthreats
	board_aithreats = board.aithreats
	ai = AI(human_color, board, board_userthreats, board_aithreats,[1,1,1],4) #human AI
	ai2 = AI(computer_color, board, board_userthreats, board_aithreats,[1,1,1],2)
	for i in range (0,80):
			if board.turn == human_color:
				#clear_screen()
				end, player = board.checkForEndGame()
				print(board)
				if end == True:
					winner=1
					break
				print("AI computing move...")
				move, score, time, heuristics= ai.perform_move()
				if score > 10000:
					winner=1
					break
				if score < -10000:
					winner=-1
					break
				print(heuristics)
				heuristicsALL.append(heuristics)
				board.updateBoardFromMove(move)
				#clear_screen()
				print("AI: ", move)
				print("Time taken: ", time, " seconds")
				print("Moves combinations considered: ", ai.moves_considered)
				print("CURR SCORE ", score)

			else:
				#clear_screen()
				end, player = board.checkForEndGame()
				print(board)

				if end == True:
					winner=-1
					break
				print("AI computing move...")
				move, score, time, heuristics= ai2.perform_move()
				if score > 10000:
					winner=-1
					break
				if score < -10000:
					winner=1
					break
				print(heuristics)
				board.updateBoardFromMove(move)
				#clear_screen()
				print("AI: ", move)
				print("Time taken: ", time, " seconds")
				print("Moves combinations considered: ", ai2.moves_considered)
				print("CURR SCORE ", score)
	h.append(heuristicsALL)
	game.append(winner)
print(game)
print(h)

input('Press enter to exit the game')
	
	




