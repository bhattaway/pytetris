class Grid:
    def __init__(self, w=10, h=20):
        self.w = w
        self.h = h

        self.grid = []

        for i in range(h):
            self.grid.append(['a' for _ in range(w)])

    def __str__(self):
        s = ""

        for row in self.grid:
            for char in row:
                s += char

            s += '\n'

        return s

    def __repr__(self):
        s = "   "

        for i in range(self.w):
            s += "%2d" % (i)

        s += '\n'
        i = 0
        for row in self.grid:
            s += "%3d" % (i)
            i += 1
            for char in row:
                s += ' ' + char

            s += '\n'

        return s
