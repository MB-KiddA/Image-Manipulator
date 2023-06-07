from PIL import Image
import os



def Menu():
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

def Credits():
    print('Program Made by Drew Armstrong')
    print('[1] Back')
    Ans = int(input('[Input]: '))
    
    if Ans == 1:
        os.system('cls')
        Menu()
    else:
        Ans = int(input('Invaild Answer'))

def Edit():
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

def Size():
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

def Rotate():
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
    
    

def Convert():
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



def Filter():
    print('[1] B/W \n[2] Contrast \n[3] Blur \n[4] Back ')
    Ans = int(input('[Input]: '))
    if Ans == 1:
        os.system('cls')
        print()
    if Ans == 2:
        os.system('cls')
        print()
    if Ans == 3:
        os.system('cls')
        print()
    if Ans == 4:
        os.system('cls')
        Edit()

image = input('Enter Image to Edit')
os.path('cls')
Menu()