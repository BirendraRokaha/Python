# init variablse


from builtins import print

theMatrix = ""
system = ""
neo = ""
enemy = ""
inside = ""
save = ""
unplugged = ""
fight = ""

prof = ["","","",""]
adj = ["",""]

# get input form user

print("Welcome to a new world!")
print("Let's play mad libs")
neo = input("Please name yourself.\n")

print(f"hello {neo}! Are you ready")
theMatrix = input ("What is something you want to know more about")

print(f"Oooh! YOu want to know more about the {theMatrix}")
print(f"FIrst tell me what you already know about {theMatrix}")
system = input (f"what noun would tou categorize {theMatrix} as: ")

enemy = input (f"Give me an opposing noun to {system}: ")

inside = input (f"Now give me any relaxing noun (present tense): ")

print(f"Okay, now i need 4 professinos relating to {system}")

for i in range(len(prof)):
    prof[i] = input (f"profession (plural) {i+1}/ {len(prof)}: ")

save = input(f"give me hero-related verb (present tense): ")

unplugged = input (f"now give me a verb that makes you think about relief (past tense): ")

print(f"Lastly 2 distopyan adjectives")
for i in range(len(adj)):
    adj[i] = input (f"Adjective  {i+1}/ {len(adj)}: ")

fight = input(f"and a verb: ")

# Init story
madlibStory = (f"{theMatrix} is a {system}, {neo}. That {system} is our {enemy}. " +
f"But when you're {inside}, you look around, what do you see? " +
f"{prof[0]}, {prof[1]}, {prof[2]}, {prof[3]}.The very minds " +
f"of the people we are trying to {save}. But until we do, " +
f"these people are still a part of that {system} and that makes " +
f"them our {enemy}. You have to understand, most of these people " +
f"are not ready to be {unplugged}. And many of them are so {adj[0]}, " +
f"so hopelessly {adj[1]} on the {system}, that they will {fight} to protect it.")

# print story
print (madlibStory)
input()