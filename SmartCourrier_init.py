import turtle as ttl
import random as rand
import math
from enum import Enum

class Direction(Enum):
        NORTH = 90
        SOUTH = 270
        WEST = 180
        EAST = 0

class Node():
    def __init__(self, parent=None, position=None):
        self.f, self.g, self.h = 0
        self.parent = parent
        self.position = None

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

    def go():
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
 
        open_list = []
        close_list = []

        start_node = Node(None, start)
        end_node = Node(None, destination.position)
        end_area_nodes = []
        for pos in destination.area:
            end_area_nodes.append(Node(None, pos))

        open_list.append(start)

        while len(open_list) > 0:
 
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

            if best_node in end_area_nodes:
                path = []
                node = best_node
                while node is not None:
                    path.append(node.position)
                    node = node.parent
                path.reverse()
                return path

            # Jika bukan, maka buat penerus dari node terbaik

            pass
        
        print("There's no way to the destination.")
        return None

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
    maze = [    [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], # 0
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], # 1
                [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1], # 2
                [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1], # 3
                [1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1], # 4
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], # 5
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 6
                [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1], # 7
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1], # 8
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1], # 9
                [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1], # 10
                [1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1], # 11
                [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1], # 12
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], # 13
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0], # 14
            ]
    drawMaze(maze)
    start_pos = placeStart(maze)
    destination_pos = placeDestination(maze).area
    
    print(start_pos) ### coba
    print(destination_pos) ### coba

    # 3. Cari jalur yang sampai di sekitar tujuan

    # 4. Gerakkan kurir ke sekitar tujuan dan hadapi ke tujuan
    #       Jika tidak sampai, maka print pesan kesalahan

    win.exitonclick()

if __name__ == '__main__':
    main()