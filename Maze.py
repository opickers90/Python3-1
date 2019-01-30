"""This is a python MAZE! I had a fun time making it - enjoy. If you liked 
press the one up button!"""

"""This requires a lot of inputs if
your on a mobile device and want the correct inputs to get out of the maze and claim your prize 

SCROLL ALL THE WAY TO
THE BOTTOM FOR ANSWER!!

if on a desktop copy and paste into your python program of choice - PLAY AND ENJOY dont cheat by scrolling!!"""


"""Version V1.2 - Champ"""






print(
	 "Welcome to Champ's MAZE!\n"
	 "\nYou will have to make a series of	  choices...straight, left or right"
	 "\nEach one will take you further or start you over!\n"
	 "\nHINT: #1 Draw it out on a piece of paper as you go!"
	 "\nHINT: #2 If you know your going the right way check your spelling."
	 "\nHINT: #3 EACH TIME YOU FAIL LOOK BACK AT YOUR HISTORY") 



print("\n****YOU HAVE ENTERED CHAMP'S MAZE***")
print("********CAN YOU MAKE IT OUT!******")

def beginning(): 
#begins the maze loop

	while True: 
		
		question1 = input(
						"\nYou are standing in THE  BEGINNING, which way to walk"
						" \nyou can walk straight, left or right." " ") 
						
		if question1 != "straight":
			print("\n----------------------------------")
			print("You cannot go that way, try again") 
			print("\n----------------------------------")
		
		elif question1 == "straight": 
			print("\n----------------------------------")
			print("You have chosen correctly!")
			print("----------------------------------")
			stage1()
			break

def stage1(): 
	while True: 
		
		question2 = input(
						"\nYou went straight, you can now walk straight"
						" left or right - which way?" " ")
		if question2 == "left":
			print("\n----------------------------------")
			print("\nYou went left, you can now only walk right...")
			print(
				"\nLooks like a dead end smarty...try again, you will"
				" now start over!") 
			print("\n----------------------------------")
			beginning()
			break
			
		if question2 == "right": 
			print("\n----------------------------------")
			print(
				"\nYou have come a long way... just to find a deadend" 
				" \nHere we go from the beginning!") 
			print("\n----------------------------------")
			beginning()
			break
			
			
		if question2 == "straight":
			print("\n----------------------------------")
			question3 = input("\nGood job! You may now walk straight or right. " " ")
			print("\n----------------------------------")
	
		if question3 == "straight": 
			print("\n----------------------------------")
			print(
				"\nYou fell into a firey pit of hell! Ouch!"
				"Start over...sorry..you not that good at this.")
			print("\n----------------------------------")
			beginning()
			break
		
		if question3 == "right": 
			print("\n----------------------------------")
			question4 = input(
							"\nAwesome! I knew you could do it!"
							" ...but now what?" " \nI'll give you hint"
							" what side do police officers where thier" 
							" badge on?" " ")
			print("\n----------------------------------")
							
		if question4 != "left": 
			print("\n----------------------------------")
			print("\nWell...hope you never need 911!" " Start over!") 
			print("\n----------------------------------")
			beginning()
			break
		 
		if question4 == "left": 
			print("\n----------------------------------")
			question5 = input(
							"\nYour getting close!...well kinda..."
							"\nTell me smarty, which way?" 
							"\nHINT: You just did it..." " ") 
			print("\n----------------------------------")
							
		if question5 != "left": 
			print("\n----------------------------------")
			print("\nNo...no...no...remember LEFT. Start over!")
			print("\n----------------------------------")
			beginning() 
			break
		
		if question5 == "left": 
			print("\n----------------------------------")
			question6 = input(
							"\nFast which way! Straight, left or right?" 
							" here's a hint - famous country singer... " " ")
			print("\n----------------------------------")
			
		if question6 != "straight": 
			print("\n----------------------------------")
			print(
			"\nDammit, so close...maybe get a piece of paper and draw"
			" a map!" " Start over!") 
			print("\n----------------------------------")
			beginning()
			break
			
		if question6 == "straight": 
			print("\n----------------------------------")
			question7 = input(
							"\nGenius! Yes, now - left or straight?"
							"\nIf I was a betting man I'd go left..."
							" but I am not." " ") 
			print("\n----------------------------------")
							
		if  question7 != "straight": 
			print("\n----------------------------------")
			print("\nI told you I was NOT a betting man! Start over!") 
			print("\n----------------------------------")
			beginning() 
			break
		
		if question7 == "straight": 
			print("\n----------------------------------")
			question8 = input(
							"\nI'll give it to you, you paid attention!"
							"\nSince you did, I'll give you a hint now..."
							"\n****!" " ")
			print("\n----------------------------------")
							
		if question8 != "left": 
			print("\n----------------------------------")
			print("\nSeriously? I gave you the answer!" " Start over!")
			print("\n----------------------------------")
			beginning()
			break
		
		if question8 == "left": 
			print("\n----------------------------------")
			question9 = input(
							"\nThis could be your last choice if you"
							" correctly! Left or straight?! \nHere's a" 
							" hint: Who was the most famous baseball"
							" player of all time \nnicknamed the" 
							" Great Gambino, was he right or left handed?" " ") 
			print("\n----------------------------------")
							
		if question9 != "left": 
			print("\n----------------------------------")
			print("Really?...google it! - start over!")
			print("\n----------------------------------")
			beginning() 
			break
			
		if question9 == "left": 
			
			print(
				"\n		$$$$_______________"
				"\n	   $$__$_______________"
				"\n	   $___$$______________"
				"\n	   $___$$______________"
				"\n	   $$___$$_____________"
				"\n	   $____$$____________"
				"\n		$$____$$$__________"
				"\n		 $$_____$$_________"
				"\n		 $$______$$________"
				"\n		  $_______$$_______"
				"\n	$$$$$$$________$$______"
				"\n  $$$_______________$$$$$$"
				"\n $$____$$$$____________$$$"
				"\n $___$$$__$$$____________$$"
				"\n $$________$$$____________$"
				"\n  $$____$$$$$$____________$"
				"\n  $$$$$$$____$$___________$"
				"\n  $$_______$$$$___________$"
				"\n   $$$$$$$$$__$$_________$$"
				"\n	$________$$$$_____$$$$"
				"\n	$$____$$$$$$____$$$$$$"
				"\n	 $$$$$$____$$__$$"
				"\n	   $_____$$$_$$$"
				"\n		$$$$$$$$$$")

			print("\n************GOOD JOB************\n")
			 
			print("\n********YOU*********")
			print("*******FOUND********")
			print("*******YOUR*********")
			print("********WAY*********")
			print("********OUT*********")
			print("***ANTI-CLIMATIC?****")
			print("***WELL...PLAY AGAIN!***")
			break
			  
							
			

beginning()


"""ANSWER"""

"""MOBILE USERS: To get out of the maze type the following into the pop-up input box: 
IMPORTANT EACH INPUT MUST BE A NEW LINE WITH NO SPACE AFTER THE ENTRY: 

straight
straight 
right
left
left
straight 
straight
left 
left

"""











