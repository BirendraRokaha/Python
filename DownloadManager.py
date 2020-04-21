import os,os.path,shutil


#Change current working directory to Downloads
os.chdir('/Users/Birendra Rokaha/Downloads')
print(os.getcwd())

def mkDir(dirName):
    os.mkdir(dirName)

doc =( ".doc",".docx",".txt",".pdf",".rtf",".csv")
ppt =( ".ppt", ".pptx")
oth = ( ".*" , ".zip",".iso",".scss",".dart" )
img =(".jpg",".jpeg",".png",".svg")



sourcePath='/Users/Birendra Rokaha/Downloads'
files = [f for f in os.listdir('.') if os.path.isfile(f)]
sourcefiles = os.listdir(sourcePath)
for file in files:
    if file.endswith(tuple(ppt)):
        destinationPath = '/Users/Birendra Rokaha/Downloads/PowerPoint'
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath,file))
    elif file.endswith(tuple(doc)):
        destinationPath = '/Users/Birendra Rokaha/Downloads/Documents'
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath,file))
    elif file.endswith(tuple(img)):
        destinationPath = '/Users/Birendra Rokaha/Downloads/Images'
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath,file))
    elif file.endswith('.exe'):
        destinationPath = '/Users/Birendra Rokaha/Downloads/Applications'
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath,file))
    else:
        destinationPath = '/Users/Birendra Rokaha/Downloads/Others'
        shutil.move(os.path.join(sourcePath,file), os.path.join(destinationPath,file))

