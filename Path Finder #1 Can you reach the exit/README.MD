# Path Finder #1: can you reach the exit?

Task

You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return true if you can reach position [N-1, N-1] or false otherwise.

    Empty positions are marked ..
    Walls are marked W.
    Start and exit positions are empty in all test cases.

Path Finder Series:

    #1: can you reach the exit?
    #2: shortest path
    #3: the Alpinist
    #4: where are you?
    #5: there's someone here

a = "\n".join([
".W.",
".W.",
"..."
])

b = "\n".join([
".W..",
"....",
".w..",
".w..",
])

c = "\n".join([
"......",
"......",
"......",
"......",
"......",
"......"
])

d = "\n".join([
"......",
"......",
"......",
"......",
".....W",
"....W."
])

f = "\n".join([
".W...",
".W...",
".W.W.",
"...W.",
"...W.",
])

g = "\n".join([
".WWW..WW.W.........W..W.W....WW..W.......WW..W..W.",
"....W..WW.W...W.WW....WWW...........WW..W.WW.....W",
".....W..W...W.......W..WW..W......W.........W.W..W",
"W..W..W.W.W..W.W.W...W...W...W.......W....W....W..",
".W...W....W.W...WWW.WWW..W....W..W...WW......W...W",
"W.........W..W.......W..............W....WWW.W....",
"....W......W...WW........WWW...W.W.WW..W.......W..",
".W..W....W............W.W..WWWW.WW..WWW...WW......",
"......WWW........WW..W...WWW.WW...........WW.W..WW",
".WW......W....W...WWW...........W.....W...W....W.W",
"....WW...........W.........W...W..................",
".W..W....W......W...W.W.......WW...W..............",
"WWW........WW..W...W...WW.W..WW...WW.WWW...W.WWW..",
"...W...........W..W.W.W..W..W.W.WW..W.W...........",
"...........WW..W.WW.....W.....W........W.W..W.W...",
".W..W.W..................W...W.........WWWW....W..",
"....W....W........W........W.W...W.W..W.W....WW...",
".W.......W......W.......W.....W....W.W.....WW.....",
"WW.....W...W........W.W........WWWWW....W.W..W.W..",
"...WWWW........W.WW.........W........W.W.....W.W.W",
".W..W..W....W.W........W........W.........W.......",
"WW..WW......W....W....W.W...........W.....W.......",
"..W..W...WWW...W.W.........W..W..W...WW.W.......W.",
"WW.W.......WW..WW.W..W....WW............W....W....",
"W.W...W.WW..WW.W....WW........WWW....WWW.W....W...",
".......W....W.....W.W.W..W.W.........W.....W....W.",
"..WW...W.........WW....WW......W....W.......W.WWW.",
"WW.WW..W.W.WW....WW.W..WW......W.W..........W.W...",
"W..W.........W..W.........W....W......W......W....",
"....W..WW.W...W.W.W....W.......W.W...W..WW....WW..",
"......WW.........W....WW....W..W..WWW.W....W..WW..",
"W.....W.W..WWW.W...WW....W...W.........WW..W....W.",
"............W...W....W...W........W....WW...W.W...",
"............W...W.....W...W..W.W....W..WWWW......W",
"..W..W...W..............W.W...W......W...W.......W",
"....W.W...W..W..W...W..W....W.W...........W..W.W.W",
".............W...W....W....W.....W..W.......W.....",
"...WW.W..W....W....W........W.WWW..........W....WW",
"....WW..W................W..W..W.WW.WW..W....WW..W",
".....W.W......W..WW...W..WW...W.....W.W.....WW.W..",
"WW..WW.W....WW....W..W...W...WW....W.WW....W......",
"W..........W..WWWW..W..WW.WWW..W.....W..W...W...W.",
"..W................WW..WW.....W.......WW..WW...W..",
"W..W..W....W...WW.W......WWW.W.WWW.....WW...W..W.W",
".W...W.W.WWW...W.......WW........WW...W.W...W...WW",
"W..W.....W...W...W......W.WW...W..W..........W....",
"........W...W..WWW.WW.W.WW........W..W....WWW.W..W",
".......W.WW..W........W..W....W....W.W..WW........",
"..W.........WWWW...WW...W.W.W.W.WW..W....W..W.W...",
".....W.....W.....W.W.W.....WW...........WWWW...WW.",
])

class Test(unittest.TestCase):
def test_a(self):
self.assertEqual(path_finder(a), True)

    def test_b(self):
        self.assertEqual(path_finder(b), True)

    def test_c(self):
        self.assertEqual(path_finder(c), True)

    def test_d(self):
        self.assertEqual(path_finder(d), False)

    def test_f(self):
        self.assertEqual(path_finder(f), True)

    def test_g(self):
        self.assertEqual(path_finder(g), True)
