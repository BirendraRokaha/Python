# # Software Design

# # Sample program 1


# word_list = ["Hello","My","name","is","Birendra","Rokaha"]


# '''
# #solution 1
# #print(word_list[0]+ "," + word_list[1]+ "," + word_list[2]+ "," + word_list[3]+ "," + word_list[4]+ "," + word_list[5]+ "," )

# Problems
# 1. Not flexible
# 2. Not designed to incorporate new word
# 3. Not designed to change dileminator
# '''

# ''' solution 2
# outPrint =""
# for f in range(len(word_list)):
#     outPrint += word_list[f]
#     if f !=  (len(word_list)-1):
#         outPrint += ","
# print(outPrint)
# Problems
# 1. Not flexible
# 2. Large code base
# '''

# #solution 3 : solves all the problems above
# #print(",".join(word_list))
# # improves speed and optimizes work flow    
# SEPERATOR = ","
# print(SEPERATOR.join(word_list))


# '''
# 1. Make code flexile and scalable.
# 2. Reduce redundancy for mor optimized speed and workflow.
# '''


# Program 2 Guess the number
NUM = 50 # first change

# guess = 1
# while True:
#     num = input("Please guess number between 0-100: ")
#     try:
#         num = int(num)
#     except:
#         print("Invalid number, please guess again.")
#         continue
#     if num < NUM:
#         print("Guess is under.")
#     elif num > NUM:
#         print("Guess is over.")
#     else:
#         break
#     guess += 1
# print(f"You took {guess} times to guess.")

# Problems:
# Not flexible and not sclable


class GNum:
    def __init__(self,number,min,max):
        self.number = number
        self.guesses = 0
        self.min = min
        self.max = max
    
    def get_guess(self):
        guess = input (f"Please guess a number {(self.min)}-{(self.max)}: ")
        if self.valid_number(guess):
            return int(guess)
        else:
            print("Enter a valid number")
            return self.get_guess()

    def valid_number(self, str_number):
        try:
            number = int(str_number)
        except:
            return False

        return self.min <= number <= self.max

    def play(self):
        while True:
            self.guesses += 1

            guess = self.get_guess()

            if guess < self.number:
                print("Guess is under")
            elif guess > self.number:
                print ("Guess is over")
            else:
                break
        print(f"You guessed the number in {(self.guesses)} tries.")


game = GNum(50,10,90)
game.play()
            

