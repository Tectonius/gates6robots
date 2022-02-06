import csv
from graph import Graph
import math
from astar import *
from drawPath import *
import sys, pygame



def importcsv(name):
    file = open(name)
    csvreader = csv.reader(file)
    csvrows = []
    for csvrow in csvreader:
        csvrows.append(csvrow)
    file.close()
    return csvrows


def makegraph(csv1, csv2):
    """
    :param csv1: enter name of vertex csv, "dots.csv" is default name:
    :param csv2: enter name of edges csv, "edges.csv" is default name:
    :return: = (dictionary of room numbers to corresponding (x,y), dictionary of room numbers to corresponding integers
     in matrix, the graph adjacency matrix (2D list))
    """
    dots = importcsv(csv1)
    edges = importcsv(csv2)
    roomtoint = dict()
    inttoroom = dict()
    roomtoxy = dict()
    i = 0
    for dot in dots:
        roomtoint[dot[0]] = i
        inttoroom[i]=dot[0]
        i += 1
        roomtoxy[dot[0]] = (int(dot[1]), int(dot[2]))
    gates6graph = Graph(len(dots))
    for edge in edges:
        gates6graph.add_edge(roomtoint[edge[0]], roomtoint[edge[1]], float(edge[2]))
    return roomtoxy, roomtoint, inttoroom, gates6graph

def heur1(inttoroom, roomtoxy, n1, n2):
    r1 = inttoroom[n1]
    r2 = inttoroom[n2]
    (x1, y1) = roomtoxy[r1]
    (x2, y2) = roomtoxy[r2]
    return (math.sqrt((x1-x2)**2 + (y1-y2)**2))

def pathHeur1(graph, path):
    total = 0
    curr1 = path[0]
    for i in range(1, len(path)):
        curr2 = path[i]
        total += graph.adjMatrix[curr1][curr2][1]
        curr1 = curr2
    return total

def intPtoRoomP(inttoroom, path):
    newP = []
    for p in path:
        newP.append(inttoroom[p])
    return newP

def main():
    (roomtoxy, roomtoint, inttoroom, gates6graph) = makegraph("dots.csv", "edges.csv")
    s = roomtoint["6001"]
    g = roomtoint["6721"]
    p = aStarSearch(gates6graph, inttoroom, roomtoxy, s, g, heur1, pathHeur1)
    path = intPtoRoomP(inttoroom, p)
    path.reverse()
    doAnimate(path, roomtoxy)

if __name__ == "__main__":
    main()
