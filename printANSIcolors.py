# https://stackabuse.com/how-to-print-colored-text-in-python/

# https://www.ditig.com/256-colors-cheat-sheet

styles = ["norm","bold","lite","ital","under","blink"]
# blink doesn't
# lite is same as norm
# can't combine styles

colors = ["blk","red","grn","ylw","blu","mgn","cya","wht"]
# when you use a background, the forground 
# bold black is grey
# tabs do not get background but spaces do

# if you use background color, foreground may vary 

for style in [0,1,3,4]: #range(0,4): # 5 styles
    for back in range(40,41): # 8 background colors
        print("\033["+str(style) + ";" + str(back) +"m", 
        style, styles[style], back, colors[back-40], "bg", end = '\t')
        for fore in range(30,38): # 8 foreground colors
            print("\033["+ str(fore) + ";" + str(back) + "m", fore, end = '')
        print("\033[0;0;0m")


print("\033[0;1m\n") # reset and bold and line
print("grayscale background")
for gry in range(232,256): #
    xtermBG="48;5;" + str(gry) + "m"
    print("\033[" + xtermBG, f'{gry:d}', end="")

print("\033[0;1m\n") # reset and bold and line
print("basic colors and bright basic")
for color in range(0,0x10): #
    xtermBG="48;5;" + str(color) + "m"
    if color==8: print()
    print(f"\033[{xtermBG} {color:02d} \033[0m", end="")

print("\033[0;1m\n") # reset and bold and line
print("216 Xterm color blends, 6x6x6 RGB cube")
print("16 to 51 is a face having: blk, blu, grn, cyan")
print("196 to 231 is oposite face: red, magenta, ylw, wht")
# others 6x6s are intermediate slices of the cube
for red in range(6): # 6 levels of red
    for grn in range(6): #
        for blu in range(6): #
            xterm = 16 + blu + 6*grn + 36*red
            ANSIbg="\033[48;5;" + str(xterm) + "m"
            print(f"{ANSIbg} {xterm:03} \033[0m", end="")
            if xterm %6 == 3: print() # newline every 6

print("\033[0;1m\n") # reset and bold and line


