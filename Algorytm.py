import math


def contain(list, x, y):
    for i in range(len(list)):
        if list[i].x == x and list[i].y == y:
            return 1
    return 0


class gridpoint:
        def __init__(self, gridvalue, gridposx, gridposy, parentg):
            self.y = gridposy
            self.x = gridposx
            self.endpos = 0
            if gridvalue == 'e':
                self.endpos = 1
            self.g = parentg
            self.h = math.sqrt(math.pow(int(self.x-19), 2) + math.pow(int(self.y)-19, 2))
            self.f = self.g + self.h


file = open('grid.txt')
grid = file.read()
file.close()
grid = grid.split("\n",)
for i in range(len(grid)):
    grid[i] = grid[i][1:]
    grid[i] = grid[i].split(" ")
grid.reverse()
grid[19][19] = "e"
gridstart = gridpoint(grid[0][0], 0, 0, 0)
open = []
close = []
open.append(gridstart)
while(1):
    current = open[0]
    for i in range(len(open)):
        if open[i].f < current.f:
            current = open[i]
    close.append(current)
    open.remove(current)
    if current.y+1 < 20 and not grid[current.y + 1][current.x] == '5' and contain(close, current.x, current.y + 1) == 0 and contain(open, current.x, current.y + 1) == 0:
        temp = gridpoint(grid[current.y+1][current.x], current.x, current.y+1, current.g+1)
        temp.parent = current
        open.append(temp)
    if current.y - 1 >= 0 and not grid[current.y - 1][current.x] == '5' and contain(close, current.x, current.y - 1) == 0 and contain(open, current.x, current.y - 1) == 0:
        temp = gridpoint(grid[current.y - 1][current.x], current.x, current.y - 1, current.g + 1)
        temp.parent = current
        open.append(temp)
    if current.x - 1 >= 0 and not grid[current.y][current.x - 1] == '5' and contain(close, current.x - 1, current.y) == 0 and contain(open, current.x - 1, current.y) == 0:
        temp = gridpoint(grid[current.y][current.x-1], current.x-1, current.y, current.g + 1)
        temp.parent = current
        open.append(temp)
    if current.x + 1 < 20 and not grid[current.y][current.x + 1] == '5' and contain(close, current.x + 1, current.y) == 0 and contain(open, current.x + 1, current.y) == 0:
        temp = gridpoint(grid[current.y][current.x+1], current.x+1, current.y, current.g + 1)
        temp.parent = current
        open.append(temp)
    if len(open) == 0:
        break
    if current.endpos == 1:
        break
last = close[len(close)-1]
if len(open) == 0 and last.endpos == 0:
    print("Brak rozwiazania.")
if len(open) > 0:
    step = 0
    while(1):
        grid[last.y][last.x] = '*'
        if last.x == 0 and last.y == 0:
            break
        last = last.parent
        step = step+1
    grid.reverse()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j] + " ", end="")
        print("")
    
    print("liczba krokow to "+str(step))
