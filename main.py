import csv
from graph import Graph


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
    :return: = (dictionary of room numbers to corresponding integers in matrix, the graph adjacency matrix (2D list))
    """
    dots = importcsv(csv1)
    edges = importcsv(csv2)
    roomtoint = dict()
    i = 0
    for dot in dots:
        roomtoint[dot[0]] = i
        i += 1
    print(roomtoint)
    print('\n')
    print(len(dots))
    gates6graph = Graph(len(dots))
    for edge in edges:
        gates6graph.add_edge(roomtoint[edge[0]], roomtoint[edge[1]], float(edge[2]))
    return roomtoint, gates6graph



