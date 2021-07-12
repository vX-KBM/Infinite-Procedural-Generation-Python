import os
from random import randint
try:
    import sys
    if sys.platform == "win32":
        os.system('color')
except:
    pass
from sty import fg, bg, ef, rs
from sty import Style, RgbFg
en = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","0","1","2","3","4","5","6","7","8","9"]
class counters:
    def __init__(self, name, v):
        self.name = name
        self.v = v
    def sum(self):
        self.v += 1
        if self.v == len(en):
            self.v = 0
            index = classes_names.index(self.name) # Get the current class name by index
            holder["c"+str(int(index-1))].sum() # Executes function sum of class_name from the index given + 1 (in reverse)
def generation():
    global classes_names, holder
    colors_rgb_fg = [fg(244, 66, 76), fg(244, 41, 44), fg(247, 51, 46), fg(248, 64, 48), fg(249, 75, 49), fg(249, 87, 51), fg(246, 100, 52), fg(245, 113, 53), fg(245, 127, 53), fg(241, 141, 55), fg(241, 156, 59), fg(244, 173, 63), fg(247, 190, 68), fg(250, 205, 72), fg(253, 219, 76), fg(252, 230, 76), fg(248, 237, 77), fg(239, 243, 78), fg(231, 246, 78), fg(220, 248, 77), fg(208, 250, 77), fg(196, 250, 77), fg(181, 250, 76), fg(166, 249, 75), fg(153, 248, 74), fg(139, 249, 74), fg(124, 249, 72), fg(112, 248, 71), fg(101, 249, 72), fg(89, 249, 70), fg(80, 250, 71), fg(72, 250, 71), fg(68, 250, 70), fg(66, 250, 73), fg(65, 250, 76), fg(64, 249, 78), fg(64, 249, 85), fg(64, 248, 92), fg(64, 248, 101), fg(64, 248, 113), fg(64, 248, 124), fg(65, 249, 136), fg(65, 248, 150), fg(65, 248, 163), fg(65, 248, 177), fg(66, 249, 192), fg(66, 250, 208), fg(66, 250, 225), fg(67, 250, 239), fg(66, 251, 248), fg(66, 250, 251), fg(66, 245, 250), fg(63, 234, 249), fg(59, 218, 248), fg(54, 200, 248), fg(51, 184, 247), fg(48, 169, 246), fg(44, 155, 246), fg(40, 141, 247), fg(37, 126, 247), fg(34, 113, 247), fg(33, 101, 247), fg(32, 91, 247), fg(33, 82, 247), fg(31, 74, 247), fg(32, 66, 246), fg(34, 61, 247), fg(35, 59, 247), fg(37, 57, 247), fg(44, 57, 248), fg(57, 57, 247), fg(70, 57, 247), fg(87, 57, 247), fg(103, 57, 247), fg(118, 57, 247), fg(133, 58, 248), fg(147, 58, 247), fg(160, 59, 247), fg(174, 60, 247), fg(188, 60, 248), fg(201, 60, 246), fg(212, 59, 243), fg(224, 59, 241), fg(233, 59, 236), fg(241, 57, 230), fg(246, 56, 222), fg(247, 55, 213), fg(247, 53, 203), fg(246, 50, 189), fg(246, 47, 174), fg(247, 45, 162), fg(246, 42, 147), fg(247, 40, 132), fg(246, 38, 119), fg(248, 36, 104), fg(248, 34, 90), fg(249, 32, 77), fg(250, 31, 67), fg(249, 30, 58), fg(248, 29, 51)]
    phrases = ["I hope you have an extra power source..."+" "*60,"Are your PC is heating enough? :3"+" "*60,"There is more chances of a zombie apocalypse happening than the generation ends..."+" "*20,"Press 'F' To Pay Respects"+" "*60,"Still 0% Complete..."+" "*70,"Generates all the possible combinations!"+" "*60,"Less than 100 lines of code!"+" "*60,"Beep boop, beep? Bop, beep bop!"+" "*60,"This is the number of combinations needed to reach length 10: 13.759.005.997.841.643"+" "*30,"Did you know that this will be endless, yeah?"+" "*60, "Trololololo lolo lolo lololo"+" "*60, "Still generating..."+" "*70,"Infinite Generator! (don't confuse with infinite power generator)"+" "*60,"Have you ever seen a generator like this before, huh?"+" "*60, "Go make some tea, it will last for too long..."+" "*60,"Please, don't close me! ;("+" "*60,"Infinite like water in the sea!"+" "*60,"Infite like stars in the sky!"+" "*60,"What do you think? Is it worth to let it continue until the end of the world?"+" "*30,"Take a walk and back in... Whatever -_- Just take a walk :3"+" "*60]
    classes_names = []
    num = 0
    name = "c"+str(num)
    classes_names.append(name)
    holder = {name: counters(name=name, v=0) for name in classes_names}
    c = 0 #counter
    color_counter = 0
    color_random = randint(0,len(colors_rgb_fg)-1)
    file_name = 0
    found = False
    Author = colors_rgb_fg[85]+"???"+fg.rs
    sys.stdout.write(f"\n\n Infinite Procedural Generation of Everything!\n")
    sys.stdout.write(f"\n\n Author {Author}\n")
    sys.stdout.write(f"\n\n Total generated: {colors_rgb_fg[color_counter]+str(c)+fg.rs}\n")
    sys.stdout.write(f" Length: {colors_rgb_fg[color_random]+str(num+1)+fg.rs}\n")
    sys.stdout.write(f"\n\n Brute Forcing the name of the Author ...\n")
    sys.stdout.write(f"\n\n {phrases[randint(0,len(phrases)-1)]}\n")
    sys.stdout.flush()
    while 1:
        word = ""
        for item in classes_names:
            word += str(en[holder[item].v])
        c += 1
        if word == "vXKBM":
            Author = colors_rgb_fg[35]+"v.X-KBM"+fg.rs
            found = True
        if c % 1000 == 0:
            color_counter += 1
            if color_counter == len(colors_rgb_fg):
                color_counter = 0
        with open(f'Dictionary_{file_name}.txt', 'a') as file:
            file.write("%s\n" % word)
        file.close()
        sys.stdout.write("\033[A"*11)
        sys.stdout.write(f" Author {Author}\n")
        sys.stdout.write(f"\n\n Total generated: {colors_rgb_fg[color_counter]+str(c)+fg.rs}\n")
        sys.stdout.write(f" Length: {colors_rgb_fg[color_random]+str(num+1)+fg.rs}\n")
        if found == False:
            sys.stdout.write(f"\n\n Brute Forcing the name of the Author ...\n")
        else:
            sys.stdout.write(f"\n\n Brute Forcing Complete! The name of the Author was found!\n")
        if c % 25000 == 0:
            sys.stdout.write(f"\n\n {phrases[randint(0,len(phrases)-1)]}\n")
        else:
            sys.stdout.write(f"\n\n\n")
        sys.stdout.flush()
        if c % 1000000 == 0: # Splits files each 1.000.000 lines
            file_name += 1
        for item in classes_names:
            if holder[item].v != len(en)-1:
                reset = False
                break
            else:
                reset = True
        if reset == True:
            num += 1
            color_random = randint(0,len(colors_rgb_fg)-1)
            name = "c"+str(num)
            classes_names.append(name)
            holder = {name: counters(name=name, v=0) for name in classes_names}
        else:
            holder[str(classes_names[-1])].sum()
generation()
