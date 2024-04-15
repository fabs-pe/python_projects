import sys, random, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pupi.org/project/Bext/')
    print('pip3 install bext')

WIDTH, HEIGHT = bext.size()

# for windows
WIDTH -= 1

NUMBER_OF_LOGOS = 5 # can be anything 1-100
PAUSE_AMOUNT = 0.2 # can be changed to 1.0 or 0.0

COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT ='ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT) 

# Key names for logo dict
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    # generate some logos
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS) })
        if logos[-1][X] % 2 == 1:
            # X needs to be even s it can hit the corner
            logos [-1][X] -= 1

    cornerBounces = 0 
    while True:
        for logo in logos:
            # erase the logos current location
            bext.goto(logo[X], logo[Y])
            print('  ', end='')

            oringinalDirection = logo[DIR]

            # see if the logo bounces off the corners
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT -1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo [Y] == 0:
                logo[DIR] == DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH -3 and logo [Y] == HEIGHT -1:
                logo[DIR] = UP_LEFT
                cornerBounces += 1

            #  see if the logo bounces off the left edge
            elif logo[X] == 0 and logo [DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # see if the logo bounces off the right. -3 cause DVD has 3 letters
            elif logo[X] == WIDTH -3 and logo [DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] ==WIDTH -3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # see if the logo bounces off the top edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo [Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT
            
            # see if the logo bounces off the bottom edge
            elif logo[Y] == -1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == -1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != oringinalDirection:
                logo[COLOR] = random.choice(COLORS) #change color on bounce

            # Move the logo. 
            # (X moves by 2 because the terminal char are twice as tall as they are wide)
            if logo [DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] +=1
        
        # Display number of corner bounces:
        bext.goto(5, 0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces, end='')

        for logo in logos:
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0, 0)

        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)

#  if this programswas run(instead of imported), run the game:

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo') 
        sys.ext()



