import os


# current working directory print(os.getcwd())

# list files and folders in currnet directory print(os.listdir())

# change directory os.chdir('/Users/Birendra Rokaha/Desktop/')

# make directory os.mkdir('Python')

# make multiple directories os.makedirs('Python/new')

# remove dir os.rmdir('Python')

# rename os.rename('file.txt','nFile.txt)

# print stats print(os.stat('web.py'))

#    for dirpath, dirnames, filenames in os.walk('/Users/Birendra Rokaha/Desktop/MIT/'):
#        print('Current Path:', dirpath)
#        print('Directory name:', dirnames)
#        print('File name:', filenames)
#        print()



# open file
with open('web.py','r') as f:
   f_contents = f.read()
   print(f_contents)


input()


