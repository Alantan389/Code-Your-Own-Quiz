# Here are the questions and answers which have been storaged in the libabery.
easy_question="A _1_ is a device that can be _2_ to carry out arbitrary sequences of arihmetic or _3_ operations automatically."
medium_question="The human brain is the central _1_ of the human _2_ system,and with the _3_ _4_ makes up the central nervous system."
hard_question="Is the Human Brain Different from a Computer? The Brain's _1_ Are Very Slow. But It's _2_ _3_.The _4_ Rewires Itself. Most of teh Details in the Brain Are _5_."

easy_answer=["computer","instructed","logical"]
medium_answer=["organ","nervous","spinal","cord"]
hard_answer=["Circuits","Massively","Parallel","Brain","Random"]


# I have set up 3 levels of difficulty. I also put the noted on it to remind user how to input the
# the slecting characters correctly in order to retrieve the corresponding level.
def level():
	easy = ["e"]
	medium = ["m"]
	hard = ["h"]
	user_input = raw_input("\nSelect your level of difficulty: easy / medium / hard /\n     Notice: easy = e   medium = m   hard = h\n")
        if user_input in easy:
		print "\n" + easy_question
		return quiz_processor (easy_question, easy_answer)
	elif user_input in medium:
		print "\n" + medium_question
		return quiz_processor (medium_question, medium_answer)
	elif user_input in hard:
		print "\n" + hard_question
		return quiz_processor (hard_question, hard_answer)
	else:
		print "\n\n Oop! Looks like you have input some incorrect characters, please refer to the criteria on the Notice and try again, Thanks !\n\n"


#  The generator will bring up different level of question base on the characters user has inputted.
#  The generator includes score system and counting system. It will present to user that which section of questions they have answered.
#  Scores system will score positative 25 when user has inputted a correct answer;By the same logic, it will score minus 25 if user has inputted it wrong.
def quiz_processor(question,answers):
	scores = 0
	index  = 0
	while index != len(answers):
		user_input = raw_input("\n\nWhat is the answer to _" + repr(index + 1) + "_  ?" + "\n")
		if user_input.lower() == answers[index].lower():
			index += 1
			print "Good work!,you have successfully answered question:",index,"\n"
			question = question.replace("_" + repr(index) + "_", user_input.upper())
			print question
			scores = scores+25
			print "\nYour Scores:",scores,"\n""\n"
		else:
			print "\nIncorrect,please try again.\n\n" + question
			scores = scores-25
			print "Your Scores:",scores,"\n","\n"

# when user has successfully answered all questions,here is the prompt for customer to continue or end the game.
# The prompt includes reminder to remind user how to input the correct character to excute the order.
# If user has inputted an incorrect character, the prompt will provides one more changce for user to try again.
def play():
	level()
	yes = ['y']
	no  = ['n']
	user_input = raw_input("\nPlay Again?: yes = y, no = n\n")
	if user_input in yes:
		play()
	elif user_input not in yes:
            print "\n\n Oop! Looks like you have input some incorrect characters, please refer to the criteria on the Notice and try again, Thanks !"
            user_input= raw_input("\nTo continue,please input small letter y\n")
            if user_input in yes:
                play()
            else:
                print"\nYou got locked due to too many error attempts,please restart this program!"
        else:
		    print "\n\nThank you, See you again!"
play()
