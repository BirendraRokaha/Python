import os

import shutil

# current working directory print(os.getcwd())

# change dir os.chdir('/Users/Birendra Rokaha/Desktop/Tut/Python/New/')

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
#with open('Madlibs.py','r') as f:
#   f_con = f.read()
#   print(f_con)

print(os.getcwd())


# moving files in python shutil.move('/Users/Birendra Rokaha/Desktop/Tut/Python/New/MadLibs.py', '/Users/Birendra Rokaha/Desktop/Tut/Python/MadLibs.py')

# moving Multiple files

#files = ['fizzbuzz.py', 'web.py', 'MadLibs.py']
#for f in files:
#    shutil.move(f, '/Users/Birendra Rokaha/Desktop/Tut/Python/')



sourcePath='/Users/Birendra Rokaha/Desktop/Tut/Python/New/'
sourcefiles = os.listdir(sourcePath)
destinationPath = '/Users/Birendra Rokaha/Desktop/Tut/Python/'
for file in sourcefiles:
    if file.endswith('.md'):
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath,file))


sourcePath='/Users/Birendra Rokaha/Downloads'
sourcefiles = os.listdir(sourcePath)
destinationPath = '/Users/Birendra Rokaha/Downloads/PowerPoint'
for file in sourcefiles:
    if file.endswith('.pptx','.ppt'):
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath,file))