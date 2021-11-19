import cv2
import numpy as np
import math

highThresh = 0.4
lowThresh = 0.1
imgFileLst = "Resors/lena.jpg"

def sobel (img):
	opImgx = cv2.Sobel(img, cv2. CV_8U, 0, 1, ksize=3)
	opImgy = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=3)
	return cv2.bitwise_or(opImgx,opImgy)


def dis(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2)**2)**0.5


def getRound(img):
    r = min(X,Y) / 2 - 1
    for i in range(X):
        for j in range(Y):
            k = dis(i, j, X / 2, Y / 2)
            if k > r:
                img[i][j] = 0
    return img


class Node:
    def __init__(self, x, y, idd):
        self.x = x
        self.y = y
        self.id = idd


def plot(cor, img):
    x, y = cor
    #img[x % X][y % Y] = 0
    a = img[y][x]
    return 255 - a


def getLinePix(start, end, img):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end

    >>> points1 = get_line((0, 0), (3, 4))
    >>> points2 = get_line((3, 4), (0, 0))
    >>> assert(set(points1) == set(points2))
    >>> print points1
    [(0, 0), (1, 1), (1, 2), (2, 3), (3, 4)]
    >>> print points2
    [(3, 4), (2, 3), (1, 2), (1, 1), (0, 0)]
    """
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1

    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)

    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    # Swap start and end points if necessary and store swap state
    swapped = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1

    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1

    # Iterate over bounding box generating points between start and end
    y = y1
    points = []
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)
        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()
    sol = 0
    for x in points:
        sol += plot(x, img)
    return sol

class Graph:
    def __init__(self, nodes, edges, img):
        self.nodes = nodes
        self.edges = edges
        self.img = img

    def plot(self):
        for nod in self.nodes:
            cv2.circle(self.img, (round(nod.x), round(nod.y)), 10, (0, 0, 0))

        for ed in self.edges:
            q = input()
            cv2.line(self.img, (round(self.nodes[ed[0]].x), round(self.nodes[ed[0]].y)),
                             (round(self.nodes[ed[1]].x), round(self.nodes[ed[1]].y)),
                             (255, 0, 0,), 1)

    def lin(self):
        sol = []
        for ed in self.edges:
            sol.append([getLinePix((round(self.nodes[ed[0]].x), round(self.nodes[ed[0]].y)),
            (round(self.nodes[ed[1]].x), round(self.nodes[ed[1]].y)),
            self.img), ed[0], ed[1]])
        #print(sol)
        sol.sort()
        sol = sol[::-1]
        sol = sol[0: 2400]
        pr = []
        for i in sol:
            pr.append([i[1], i[2]])
        print(pr)

        for ed in sol:
            cv2.line(graph, (round(self.nodes[ed[1]].x), round(self.nodes[ed[1]].y)),
                     (round(self.nodes[ed[2]].x), round(self.nodes[ed[2]].y)),
                     (255, 0, 100, 0.5), 1)

def getNodes(numNodes, radius):
    nodes = []
    radius -= 1
    for i in range(numNodes):
        al = i * math.pi * 2 / numNodes
        x = math.cos(al) * radius
        y = math.sin(al) * radius
        nodes.append(Node(x + Y / 2, y + X / 2, i))

    return nodes


if __name__ == '__main__':
    opImg = cv2.imread("Resors/D.jpg")

    opImg = cv2.cvtColor(opImg, cv2.COLOR_BGR2GRAY)
    X, Y = opImg.shape
    #opImg = cv2.Canny(opImg, 200, 225)
    #opImg = sobel(opImg)
    opImg = getRound(opImg)
    #opImg = 255 - opImg


    N = 100
    graph = np.zeros((X, Y, 3), np.uint8)
    graph = 255 - graph
    nodes = getNodes(N, min(X, Y) / 2)

    e = []
    for i in range(N):
        for j in range(i + 1, N):
            e.append([i, j])

    gr = Graph(nodes, e, graph)
    #gr.plot()
    gr.lin()

    #cv2.imshow("Lena", opImg)
    cv2.imshow("Lena_line", graph)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

