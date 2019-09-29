from PIL import Image
import os
from pathlib import Path
#rotate file
def rotateImages(rotationAmt):
  for image in os.listdir(os.getcwd()):
    if(Path(image).suffix=='.py'):
        continue    
    img = Image.open(image)
    img.rotate(rotationAmt).save(image)
    img.close()

    #rename file

def rename(name):
    i=0
    for filename in os.listdir(os.getcwd()):
        if(Path(filename).suffix=='.py'):
            continue
        dst =name + str(i) + ".jpeg"
        src =os.getcwd()+"\\"+filename 
        dst =os.getcwd()+"\\"+dst           
        os.rename(src, dst) 
        i += 1

print("Would you like rotate or rename file? Type rotate or rename to move forward")
inp=input().lower()
if(inp=='rotate'):
    print("Enter rotation amount")
    s = int(input())    
    for image in os.listdir(os.getcwd()):
        rotateImages(s)
elif(inp=='rename'):
    print("Enter some name for your new files")
    name=input().lower()
    rename(name)
