import turtle as ttl
import random as rand
import math
from enum import Enum
from typing import List, MutableSequence

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
    def __init__(self, direction=Direction.EAST, position=None):
        ttl.Turtle.__init__(self)
        self.ahead = direction
        self.current_position = position
        self.shape("classic")
        self.shapesize(1, 1)
    
    def goFoward(self):
        '''
        Jika hadap utara:
            pindah ke atas
        Jika hadap selatan:
            pindah ke bawah
        Jika hadap barat:
            pindah ke kiri
        Jika hadap timur:
            pindah ke kanan
        '''
        pass
    
    def turnRight(self):
        self.right(90)
    
    def turnLeft(self):
        self.left(90)
    
    def preturn(self, current, next):
        difference = (next[0] - current[0], next[0] - current[0])
        '''
        Jika jalur ke bawah:
            dan hadap ke timur:
                belokKanan()
            atau hadap ke barat:
                belokKiri()
        jika jalur ke atas:
            dan hadap ke timur:
                belokKiri()
            atau hadap ke barat:
                belokKanan()
        jika jalur ke kanan:
            dan hadap ke utara:
                belokKiri()
            atau hadap ke selatan:
                belokKanan()
        jika jalur ke kiri:
        jika jalur berlawanan:

        '''
        pass

    def go(self, route, destination):
        '''
        Jika sampai pada tujuan, hadap ke tujuan
        Jika belum, preturn dan maju
        '''
        pass

class Street(ttl.Turtle):
    def __init__(self):
        ttl.Turtle.__init__(self)
        self.shape("square")
        self.color("WHITE")
        self.penup()

class Ruko(ttl.Turtle):
    def __init__(self):
        ttl.Turtle.__init__(self)
        self.shape("square")
        self.color("GRAY")
        self.penup()

class Destination(ttl.Turtle):
    def __init__(self, position=None):
        ttl.Turtle.__init__(self)
        self.shape("triangle")
        self.position = position
        self.area = (   (position[0], position[1] + 1),
                        (position[0], position[1] - 1),
                        (position[0] + 1, position[1]),
                        (position[0] - 1, position[1]), )

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
            # jalur dari node tersebut

            if best_node == end_node:
                path = []
                node = best_node
                while node is not None:
                    path.append(node.position)
                    node = node.parent
                path.reverse()
                return path

            # Jika bukan, maka buat penerus dari node terbaik dan cek
            # apakah penerus bagian dari open list dan close list

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
    

def placeDestination(maze):
    dest = None
    while dest == None or maze[dest[0]][dest[1]] == 0:
        dest = [math.floor(rand.random() * len(maze)), math.floor(rand.random() * len(maze))]
    return Destination(dest)

def drawMaze(maze):
    for x in maze:
        for y in x:
            pass

def main():
    win = ttl.Screen()
    win.title("Smart Courrier")
    win.setup(1280, 720)
    

    # 1. Siapkan kurir, jalan, dan bangunan
    #kurir = Courrier()

    #kurir.turnLeft() ### coba
    #kurir.turnRight() ### coba
    ttl.penup() ### coba
    ttl.goto(90,100) ### coba
    ttl.shape("square") ### coba

    # 2. Buat list jalur dan maze
    jalur = []
                #0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 
    maze = [    [0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1], # 0
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], # 1
                [0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0], # 2
                [0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1], # 3
                [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1], # 4
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], # 5
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 6
                [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1], # 7
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1], # 8
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1], # 9
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1], # 10
                [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1], # 11
                [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0], # 12
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0], # 13
                [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1], # 14
            ]
    drawMaze(maze)
    start_pos = placeStart(maze)
    destination_pos_area = placeDestination(maze).area
    
    print(start_pos) ### coba
    print(destination_pos_area) ### coba

    # 3. Cari jalur yang sampai di sekitar tujuan
    route = []
    for des_pos in destination_pos_area:
        if des_pos[0] in range(len(maze)) and des_pos[1] in range(len(maze)) and maze[des_pos[0]][des_pos[1]] == 0:
            route.append(searchDestination(maze, start_pos, des_pos))

    short_way = searchShortest(route)

    for i in route:
        print(i)
    print("Shortest:", short_way)

    # 4. Gerakkan kurir ke sekitar tujuan dan hadapi ke tujuan
    #       Jika tidak sampai, maka print pesan kesalahan

    win.exitonclick()

if __name__ == '__main__':
    main()