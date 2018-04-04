
##################################################################
# Notes:                                                         #
# You can import packages when you need, such as structures.     #
# Feel free to write helper functions, but please don't use many #
# helper functions.                                              #
##################################################################


def bfs(testmap):

    def findStart(testmap):
        for y in range(len(testmap)):
            for x in range(len(testmap[0])):
                if testmap[y][x] == 2:
                    return [y, x]

    def valid(y, x):
        if y < 0 or x < 0 \
                or y >= len(testmap) or x >= len(testmap[0]) \
                or testmap[y][x] == 1 or testmap[y][x] == 4:
            return False
        return True
    y, x = findStart(testmap)
    queue = [[[y, x]]]
    while queue:
        path = queue.pop(0)
        cell = path[-1]
        y, x = cell[0], cell[1]
        # print(cell[0], cell[1])
        if testmap[y][x] == 3:
            break
        testmap[y][x] = 4
        if valid(y, x + 1):
            queue.append(path[:] + [[y, x + 1]])
        if valid(y + 1, x):
            queue.append(path[:] + [[y + 1, x]])
        if valid(y, x - 1):
            queue.append(path[:] + [[y, x - 1]])
        if valid(y - 1, x):
            queue.append(path[:] + [[y - 1, x]])
    for cell in path:
        testmap[cell[0]][cell[1]] = 5
    return testmap


def dfs(testmap):

    def findStart(testmap):
        for y in range(len(testmap)):
            for x in range(len(testmap[0])):
                if testmap[y][x] == 2:
                    return [y, x]

    def dfsRecursion(testmap, y, x):
        # print(testmap, y, x)
        if y < 0 or x < 0 \
                or y >= len(testmap) or x >= len(testmap[0]) \
                or testmap[y][x] == 1 or testmap[y][x] == 4:
            return False
        if testmap[y][x] == 3:
            testmap[y][x] = 5
            return True
        testmap[y][x] = 4
        if dfsRecursion(testmap, y, x + 1) \
                or dfsRecursion(testmap, y + 1, x) \
                or dfsRecursion(testmap, y, x - 1) \
                or dfsRecursion(testmap, y - 1, x):
            testmap[y][x] = 5
            return True
        return False

    y, x = findStart(testmap)
    dfsRecursion(testmap, y, x)
    return testmap


def a_star_search(dis_map, time_map, start, end):
    scores = {}
    # put your codes here:
    open = {}
    open[start] = 0
    closed = {}
    time = {}
    time[start] = 0
    flag = False

    while open and not flag:
        #curLocation = min(open, key=open.get)

        locations = sorted(open.items(), key=lambda a: (a[1], a[0]))
        curLocation = locations[0]
        curLocation = curLocation[0]
        curF = open.pop(curLocation)
        score = {}
        for nextLocation, nextTime in time_map[curLocation].items():
            if nextTime:
                score[nextLocation] = time[curLocation] + \
                    nextTime + dis_map[nextLocation][end]

                if nextLocation == end:
                    flag = True

                nextF = time[curLocation] + nextTime + \
                    dis_map[nextLocation][end]
                if nextLocation in open and open[nextLocation] < nextF \
                        or nextLocation in closed and closed[nextLocation] < nextF:
                    continue

                # open[nextLocation] = nextF
                time[nextLocation] = time[curLocation] + nextTime
        scores[curLocation] = score
        closed[curLocation] = curF
    return scores
