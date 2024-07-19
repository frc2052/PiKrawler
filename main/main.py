from picrawler import Picrawler
from time import sleep
import readchar

crawler = Picrawler() # [right front],[left front],[left rear],[right rear]
speed = 90

jointLen = 0
innerLegLen = 0
outerLeglen = 0

def main():
    while True:
        key = readchar.readkey()
        key = key.lower()

        x = 0 #left and right
        y = 0 #forward and back
        if key in('wsad'):
            if key == 'w':
                y = y+1
            elif key == "s":
                y = y-1
            elif key == 'a':
                x = x-1
            elif key == 'd':
                x = x+1
        elif key == readchar.key.CTRL_C:
            print("\n Quit") 
            break 
        move(x=x, y=y)
        sleep(0.2)

def move(x, y):
    if x == 0 or y== 0:
        crawler.do_step([45, 45, -75],[45, 45, -75],[45, 45, -75],[45, 45, -75]) 
        return 0
    


if __name__ == "__main__":
    main()