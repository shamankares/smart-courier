import turtle as ttl
import random as rand
import math
from enum import Enum
from typing import List, MutableSequence

size_per_grid = 35

class Direction(Enum):
        NORTH = 90
        SOUTH = 270
        WEST = 180
        EAST = 0

class Node():
    def __init__(self, parent=None, position=None):
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = parent
        self.position = position
    
    def __eq__(self, other):
        return self.position == other.position

class NodeList(MutableSequence):
    def __init__(self):
        self.list = list()
    def __contains__(self, value):
        for item in self.list:
            if value.position == item.position:
                return True
        return False
    def __delitem__(self, idx):
        del self.list[idx]
    def __getitem__(self, idx):
        return self.list[idx]
    def __len__(self):
        return len(self.list)
    def __setitem__(self, idx, value):
        self.list[idx] = value
    def insert(self, idx, value):
        self.list.insert(idx, value)

class Courrier(ttl.Turtle):
    def __init__(self, position=None):
        ttl.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.position = position
        self.shape("classic")
        self.speed("slowest")
        self.shapesize(1.5, 1.5)
    
    def turnRight(self):
        self.right(90)
    
    def turnLeft(self):
        self.left(90)
    
    def preturn(self, current, next):
        difference = (next[0] - current[0], next[1] - current[1])
        if difference == (-1, 0):
            self.settiltangle(Direction.NORTH.value)
        elif difference == (0, -1):
            self.settiltangle(Direction.WEST.value)
        elif difference == (1, 0):
            self.settiltangle(Direction.SOUTH.value)
        elif difference == (0, 1):
            self.settiltangle(Direction.EAST.value)

    def go(self, route, destination):
        for idx, position in enumerate(route):
            self.goto(position[1] * size_per_grid, position[0] * size_per_grid)
            if idx + 1 < len(route):
                self.preturn(position, route[idx + 1])
            self.position = position
        
        self.preturn(self.position, destination.position)

class Street(ttl.Turtle):
    def __init__(self):
        ttl.Turtle.__init__(self)
        self.hideturtle()
        self.shape("square")
        self.shapesize(1.5, 1.5)
        self.color("#dddddd")
        self.penup()
        self.speed("fastest")

class Ruko(ttl.Turtle):
    def __init__(self):
        ttl.Turtle.__init__(self)
        self.hideturtle()
        self.shape("square")
        self.shapesize(1.5, 1.5)
        self.color("GRAY")
        self.penup()
        self.speed("fastest")

class Destination(ttl.Turtle):
    def __init__(self, position=None, color="yellow"):
        ttl.Turtle.__init__(self)
        self.hideturtle()
        self.shape("triangle")
        self.position = position
        self.area = (   (position[0], position[1] + 1),
                        (position[0], position[1] - 1),
                        (position[0] + 1, position[1]),
                        (position[0] - 1, position[1]), )
        self.color(color)
        self.penup()
        self.speed("fastest")

class TextCursor(ttl.Turtle):
    def __init__(self):
        ttl.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed("fastest")


def searchDestination(maze, start, destination):

        # Siapkan open list, close list, node start, dan node
        # sekitar end. Kemudian, tambahkan node start ke dalam
        # open list.

        open_list = NodeList()
        close_list = NodeList()

        start_node = Node(None, start)
        end_node = Node(None, destination)

        open_list.append(start_node)

        while open_list:
 
            # Selama open list tidak kosong, cari node terbaik
            # dalam open list dan masukkan ke dalam close list
            # jika ada.
 
            best_node = open_list[0]
            for node in open_list:
                if node.f < best_node.f:
                    best_node = node
            
            close_list.append(best_node)
            open_list.remove(best_node)

            # Jika node terbaik adalah node sekitar end, kembalikan
            # jalur dari node tersebut.

            if best_node == end_node:
                path = []
                node = best_node
                while node is not None:
                    path.append(node.position)
                    node = node.parent
                path.reverse()
                return path

            # Jika bukan, maka buat penerus dari node terbaik dan cek
            # apakah penerus bagian dari open list dan close list. Jika
            # ada, periksa nilai g-nya.

            successors = []
            for new_position in [(1, 0), (0, 1), (0, -1), (-1, 0)]:
                node_position = (best_node.position[0] + new_position[0], best_node.position[1] + new_position[1])
                
                if node_position[0] > (len(maze) - 1) or node_position[1] > (len(maze) - 1):
                    continue
                if node_position[0] < 0 or node_position[1] < 0:
                    continue
                
                if maze[node_position[0]][node_position[1]] != 0:
                    continue
                
                new_node = Node(best_node, node_position)
                successors.append(new_node)

            for cadidate in successors:
                cadidate.g = best_node.g + 1
                cadidate.h = math.fabs(cadidate.position[0] - end_node.position[0]) + math.fabs(cadidate.position[1] - end_node.position[1])    # Manhattan distance heuiristics
                cadidate.f = cadidate.g + cadidate.h

                if cadidate in open_list:
                    open_node = open_list[open_list.index(cadidate)]
                    if open_node.g < cadidate.g:
                        open_node.parent = best_node
                        open_node.g = best_node.g + 1
                        open_node.f = open_node.g + open_node.h
                        continue
                            
                if cadidate in close_list:
                    close_node = close_list[close_list.index(cadidate)]
                    if close_node.g < cadidate.g:
                        continue

                open_list.append(cadidate)
        
        print("There's no way to the destination.")
        return None

def searchShortest(list):
    shortest = list[0]
    for item in list:
        if len(item) < len(shortest):
            shortest = item
    return shortest

def placeStart(maze):
    start = None
    while start == None or maze[start[0]][start[1]] == 1:
        start = (math.floor(rand.random() * len(maze)), math.floor(rand.random() * len(maze)))
    return start
    
def placeDestination(maze, color="yellow"):
    dest = None
    while dest == None or maze[dest[0]][dest[1]] == 0:
        dest = [math.floor(rand.random() * len(maze)), math.floor(rand.random() * len(maze))]
    return Destination(dest, color)

def drawMaze(maze, start, source, end):
    jalan = Street()
    bangunan = Ruko()

    for y, row in enumerate(maze):
        for x, place in enumerate(row):
            current_x = x * size_per_grid
            current_y = y * size_per_grid

            if place == 0:
                jalan.goto(current_x, current_y)
                jalan.stamp()
            elif place == 1:
                bangunan.goto(current_x, current_y)
                bangunan.stamp()
            
            if start.position[0] == y and start.position[1] == x:
                start.goto(current_x, current_y)
                start.showturtle()
            if source.position[0] == y and source.position[1] == x:
                source.goto(current_x, current_y)
                source.showturtle()
            if end.position[0] == y and end.position[1] == x:
                end.goto(current_x, current_y)
                end.stamp()

def go_to_flag(maze, courrier, start_pos, des_pos, des_pos_area, txtcursor):
    route = []
    msg(txtcursor, "Searching for shortest route...")
    for pos in des_pos_area:
        if pos[0] in range(len(maze)) and pos[1] in range(len(maze)) and maze[pos[0]][pos[1]] == 0:
            route.append(searchDestination(maze, start_pos, pos))
    if route:
        msg(txtcursor, "Found the route! Walking to the destination...")
        short_way = searchShortest(route)
        #print("Shortest:", short_way)
        courrier.go(short_way, des_pos)
        return short_way[-1]
    else:
        msg(txtcursor, "Weird, they should have at least a route...")
        txtcursor.delay(100)
        return None

def msg(txtcursor, string):
    txtcursor.clear()
    txtcursor.write(string, False, "left", ("Helvetica", 16, "normal"))


def main():
    win = ttl.Screen()
    win.title("Smart Courrier")
    win.setup(510, 550)
    win.mode("world")
    win.setworldcoordinates(0,550,510,0)

    txt = TextCursor()
    txt.sety(550)

    jalur = []
                #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 
    maze = [    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], # 0
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0], # 2
                [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1], # 3
                [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1], # 4
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], # 5
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 6
                [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1], # 7
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1], # 8
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1], # 9
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1], # 10
                [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1], # 11
                [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], # 12
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 13
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], # 14
            ]
    start_pos = placeStart(maze)
    source = placeDestination(maze, "white")
    source_pos_area = source.area
    destination = placeDestination(maze)
    destination_pos_area = destination.area
    kurir = Courrier(start_pos)

    msg(txt, "Drawing the maze...")
    drawMaze(maze, kurir, source, destination)

    last_pos = go_to_flag(maze, kurir, start_pos, source, source_pos_area, txt)
    if last_pos:
        go_to_flag(maze, kurir, last_pos, destination, destination_pos_area, txt)
    
    
    msg(txt, "Done! Click to exit the program.")
    win.exitonclick()

if __name__ == '__main__':
    main()