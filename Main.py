from PIL import Image, ImageFilter
import os

def Menu(): #Main Menu System
    print("[1] Image Edit \n[2] Credits \n[3] Exit")
    Ans = int(input('[Input]: '))
    if Ans == 1:
        os.system('cls')
        Edit()
    if Ans == 2:
        os.system('cls')
        Credits()
    if Ans == 3:
        os.system('cls')
        SystemExit
    else:
        Ans = input('Invaild Answer: ')

def Credits(): #Credits :)
    print('Program Made by Drew Armstrong')
    print('[1] Back')
    Ans = int(input('[Input]: '))
    
    if Ans == 1:
        os.system('cls')
        Menu()
    else:
        Ans = int(input('Invaild Answer'))



def Edit(): #Edit Menu System
    print('[1] Size \n[2] Rotate \n[3] Convert File \n[4] Filter \n[5] Back')
    Ans = int(input('[input]: '))
    if Ans == 1:
        os.system('cls')
        Size()
    if Ans == 2:
        os.system('cls')
        Rotate()     
    if Ans == 3:
        os.system('cls')
        Convert()
    if Ans == 4:
        os.system('cls')
        Filter()
    if Ans == 5:
        os.system('cls')
        Menu()
    else:
        Ans = int(input('Invalid Answer: '))

def Size(): #Change Image Size
    print('[Enter Width]: 1px Minimum')
    Width_Ans = int(input('[Input]: '))
    if Width_Ans < 1:
        Width_Ans = int(input('Too Little: '))

    print('[Enter Height]: 1px Minimum')
    Height_Ans = int(input('[Input]: '))
    if Height_Ans < 1:
        Height_Ans = int(input('Too Little: '))

    Size = (Width_Ans , Height_Ans)
    for f in os.listdir('.'):
        if f.endswith('.jpg' or '.png'):
            i = Image.open(image)
            fn, fext = os.path.splitext(f)

            i.thumbnail(Size)
            i.save('Finished/{}_Resized{}'.format(fn))

def Rotate(): #Rotates Image
    print('[Degrees]: 0 - 360')
    Degree = int(input('[Input]: '))
    if Degree > 360:
        Degree = int(input('Too Much: '))
    if Degree < 0:
        Degree = int(input('Too Little: '))
    i = Image.open(image)
    fn, fext = os.path.splitext(image)
    i.rotate(Degree)
    i.save('Finished/{}_Rotated{}'.format(fn))  

def Convert(): # Converts Image to .png or .jpg
    print('[1] Convert to png \n[2] Convert to jpg \n[3] Back')
    Ans = int(input('[input]: '))
    
    if Ans == 1:
        for f in os.listdir('.'):
            if f.endswith('.jpg'):
                i = Image.open(image)
                fn, fext = os.path.splitext(f)
                i.save('Finished/{}.png'.format(fn))

    if Ans == 2:
        for f in os.listdir('.'):
            if f.endswith('.png'):
                i = Image.open(image)
                fn, fext = os.path.splitext(f)
                i.save('Finished/{}.jpg'.format(fn))
    if Ans == 3:
        os.system('cls')
        Edit()

    else:
        Ans = int(input('Invalid Answer: '))



def Filter(): #Filter Menu System
    print('[1] Greyscale \n[2] Blur \n[3] Back ')
    Ans = int(input('[Input]: '))
    if Ans == 1:
        os.system('cls')
        Color()
    if Ans == 2:
        os.system('cls')
        Blur()
    if Ans == 3:
        os.system('cls')
        Edit()



def Color(): #Makes The Image Greyscale
    i = Image.open(image)
    fn, fext = os.path.splitext(image)
    i.convert(mode='L')
    i.save('Finished/{}_Greyscale{}'.format(fn))


def Blur(): #Blurs Image
    print('[Blur]: 0 - 100')
    blur = int(input('[Input]: '))
    if blur < 0:
        blur = int(input('Cannot Go Under 0: '))

    if blur > 100:
        blur = int(input('Cannot Go Over 100: '))

    i = Image.open(image)
    fn, fext = os.path.splitext(image)
    i.filter(ImageFilter.GaussianBlur(blur))
    i.save('Finished/{}_Blurred{}'.format(fn))


image = input('Enter Image to Edit: ')
os.system('cls') #Clears Terminal Text (Used So Terminal isn't Cluttered and Also looks Higher Quality)
Menu()