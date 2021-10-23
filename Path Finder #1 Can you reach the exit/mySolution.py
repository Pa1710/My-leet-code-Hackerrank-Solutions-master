
def path_finder(maze):
    l = list()
    l1 = list()
    for i in maze:
        if i == '\n':

            l.append(l1)
            l1 = list()
            continue

        l1.append(i)
    l.append(l1)
    l1 = list()
    visitableNodes = list()
    visitableNodes.append((0, 0))
    rng = len(l) - 1
    marked = 'x'
    while visitableNodes:
        row, column = visitableNodes.pop(-1)
        r = int(row)
        c = int(column)
        print(row, column)
        if row == rng and column == rng:
            return True
        if l[r][c] == marked:
            continue
        # look up
        if r - 1 >= 0 and l[r - 1][c] != marked and l[r - 1][c] != 'W':
            visitableNodes = [(r - 1, c)] + visitableNodes
        # look down
        if r + 1 <= rng and l[r + 1][c] != marked and l[r + 1][c] != 'W':
            visitableNodes = [(r + 1, c)] + visitableNodes
        # look right
        if c + 1 <= rng and l[r][c + 1] != marked and l[r][c + 1] != 'W':
            visitableNodes = [(r, c + 1)] + visitableNodes
        # look left
        if c - 1 >= 0 and l[r][c - 1] != marked and l[r][c - 1] != 'W':
            visitableNodes = [(r, c - 1)] + visitableNodes
        l[r][c] = marked
    return False
