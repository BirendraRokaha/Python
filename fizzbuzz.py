
#THis prints fizzfuzz
for i in range(1,100):
    output = ""
    if i % 3 == 0: output = output + "Fizz"
    if i % 5 == 0: output = output + "Buzz"
    if output == "": print(i)     
    else: print(output)
       
