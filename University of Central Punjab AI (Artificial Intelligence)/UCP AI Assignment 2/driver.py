#M.Adil Shahzad L1f17bscs0187
#Abdullah Ameen L1f17bscs0233
#Hafiz Husnain Amir L1f17bscs0643
#Muhammad Shoail Khan L1f17bscs0458
#Muhammad Nabeel L1f16bscs0526

import argparse
import pickle
from collections import defaultdict
import pickle
from collections import defaultdict


class File_Error(Exception):
    pass


class User_Error(Exception):
    print(
        f" Something Wents Wrong.Use this as an Example python driver.py --startrow 1 2 3 8 0 4 7 6 5 --goalrow 2 8 1 0 4 3 7 6 5 ")
    print('    ')


#Arr = []


class Simple_DlsDiagram:

    def __init__(self, point):
        self.point = point
        self.diagram = defaultdict(list)

    def drawanedgebetweenpoints(self, pointstart, pointend):
        self.diagram[pointstart].append(pointend)

    def Print(self):
        print(self.diagram)

    def depthlimitedsearchprocess(self, start, goal, limit):

        Arr = []
        NewArr = []
        NewArr.append(start)
        if start == goal:
            return True
        if limit <= 0:
            return False
        else:
            for i in self.diagram[start]:
                Arr.append(i)
                print(i)
                if (self.depthlimitedsearchprocess(i, goal, limit - 1)):
                    return True
            return False

    def dls(self, start, goal, limit):
        for i in range(limit):
            if self.depthlimitedsearchprocess(start, goal, i):
                return True
        return False


class BoxPattern:

    def __init__(self, pattern, end, move='start'):  # Initilized Majic Modules for Classes

        self.pattern = pattern

        self.end = end

        self.move = move

        for (row, i) in zip(pattern, range(3)):  # Zip is use to Add two range values

            if 0 in row:
                self.data = [i, row.index(0)]

    def __eq__(self, no_value):  # Majic Module is use to check equality in box

        if no_value == None:
            return False

        if isinstance(no_value,
                      BoxPattern) != True:  # isinstance() function returns True if the specified object is of the specified type, otherwise False

            raise (TypeError, File_Error)

        for i in range(3):

            for j in range(3):

                if self.pattern[i][j] != no_value.pattern[i][j]:
                    return False

        return True

    def __getitem__(self, key):

        if isinstance(key,
                      tuple) != True:  # isinstance() function returns True if the specified object is of the specified type, otherwise False

            raise (TypeError, File_Error)

        if len(key) != 2:
            raise KeyError

        return self.pattern[key[0]][key[1]]

    def calc_end_fun(self, goal):

        self.end_fun = 0

        for i in range(3):

            for j in range(3):

                if self.pattern[i][j] != goal.pattern[i][j]:
                    self.end_fun += 1

        if self.data != goal.data:
            self.end_fun -= 1  # Remove one counter if the blank location is displaced because it overestimates the goal

        self.result = self.end_fun + self.end

        return self.end_fun, self.end, self.result

    # ----- Fucntion to move the blank tile left if possible -----#
    def moveleft(self):

        if self.data[1] == 0:
            return None

        left = [[self.pattern[i][j] for j in range(3)] for i in range(3)]

        left[self.data[0]][self.data[1]] = left[self.data[0]][self.data[1] - 1]

        left[self.data[0]][self.data[1] - 1] = 0

        return BoxPattern(left, self.end + 1, 'Uber Driver Found at left: ')

    # ----- Fucntion to move the blank tile right if possible -----#
    def moveright(self):

        if self.data[1] == 2:
            return None

        right = [[self.pattern[i][j] for j in range(3)] for i in range(3)]

        right[self.data[0]][self.data[1]] = right[self.data[0]][self.data[1] + 1]

        right[self.data[0]][self.data[1] + 1] = 0

        return BoxPattern(right, self.end + 1, 'Uber Driver Found at right: ')

    # ----- Fucntion to move the blank tile up if possible -----#
    def moveup(self):

        if self.data[0] == 0:
            return None

        up = [[self.pattern[i][j] for j in range(3)] for i in range(3)]

        up[self.data[0]][self.data[1]] = up[self.data[0] - 1][self.data[1]]

        up[self.data[0] - 1][self.data[1]] = 0

        return BoxPattern(up, self.end + 1, 'Uber Driver Found at up: ')

    # ----- Fucntion to move the blank tile down if possible -----#
    def movedown(self):

        if self.data[0] == 2:
            return None

        down = [[self.pattern[i][j] for j in range(3)] for i in range(3)]

        down[self.data[0]][self.data[1]] = down[self.data[0] + 1][self.data[1]]

        down[self.data[0] + 1][self.data[1]] = 0

        return BoxPattern(down, self.end + 1, 'Uber Driver Found at down: ')

    # ----- Fucntion to check and perform all the moves according to possiblity and weather the next move is closed or not -----#
    # ----- Close this node and all the new nodes to open list -----#
    def moveall(self, uber_driver):

        left = self.moveleft()

        left = None if uber_driver.isclosed(left) else left

        right = self.moveright()

        right = None if uber_driver.isclosed(right) else right

        up = self.moveup()

        up = None if uber_driver.isclosed(up) else up
        down = self.movedown()
        down = None if uber_driver.isclosed(down) else down

        uber_driver.closeGrid(self)
        uber_driver.openGrid(left)
        uber_driver.openGrid(right)
        uber_driver.openGrid(up)
        uber_driver.openGrid(down)

        return left, right, up, down

    # ----- Fucntion to print the array in beautifed format -----#
    def print(self):
        print(self.move + str(self.end))
        print(self.pattern[0])
        print(self.pattern[1])
        print(self.pattern[2])


class DlsDiagram:

    def __init__(self, start, goal):

        self.start = start
        self.goal = goal
        self.open = {}
        self.closed = {}
        _, _, result = self.start.calc_end_fun(self.goal)
        self.open[result] = [start]

    # ---- Fucntion to check weather a node is in closed node or not ----#
    def isclosed(self, node):

        if node == None:
            return True

        end_fun, _, _ = node.calc_end_fun(self.goal)  # calculate hfucntion to check in that list of the hash table

        if end_fun in self.closed:

            for x in self.closed[end_fun]:

                if x == node:
                    return True

        return False

    # ---- Function to add a node to the closed list and remove it from the open nodes list ----#
    def closeGrid(self, node):

        if node == None:
            # return back if no node
            return True

        end_fun, _, result = node.calc_end_fun(self.goal)

        self.open[result].remove(node)  # remove from the list of the resulttion of the hash table for open nodes

        if len(self.open[result]) == 0:
            del self.open[result]  # remove the attribute for a resulttion if its list is empty

        if end_fun in self.closed:

            self.closed[end_fun].append(node)

        else:

            self.closed[end_fun] = [node]

        return True

    # ---- Function to add a node to the open list after its initilaized ----#
    def openGrid(self, node):

        if node == None:
            return True

        _, _, result = node.calc_end_fun(
            self.goal)  # Calculate ffucntion to add the node to the list of that ffucntion in hash table

        if result in self.open:

            self.open[result].append(node)

        else:

            self.open[result] = [node]

        return

    # ---- Function to solve the uber_driver using A star algorithm ----#
    def solve(self):

        final_result = None

        while (final_result != self.goal):
            i = 0
            while i not in self.open:
                i += 1  # Check for the list with least 'resulttion' to pick a node from that list
            final_result = self.open[i][-1]
            final_result.moveall(self)  # Expand that node for next possible moves

        # ---- Print the solution in reverse direction i.e. from goal to start----#
        while final_result.move != 'start':
            final_result.print()
            # do reverse move that what was done to reach the state to backtrack along the solution
            if final_result.move == 'Uber Driver Found at up: ':
                final_result = final_result.movedown()

            elif final_result.move == 'Uber Driver Found at down: ':
                final_result = final_result.moveup()
            elif final_result.move == 'Uber Driver Found at right: ':
                final_result = final_result.moveleft()
            elif final_result.move == 'Uber Driver Found at left: ':
                final_result = final_result.moveright()

            end_fun, _, _ = final_result.calc_end_fun(self.goal)
            for j in self.closed[end_fun]:
                if j == final_result:
                    final_result = j

        return i


if __name__ == '__main__':
    # Parser are used here so the user follow the guidelines of code . this will help the user to provide better experiences.

    User_Error()
    # if user have any error then print out with help else show the outputs

    parser = argparse.ArgumentParser()

    parser.add_argument("--startrow",
                        help='Enter the numbers in sequence for starting arangement starting from row 1 to row 3 space separated (put 0 for blank area).',
                        type=int, nargs=9, metavar=(
        'row1col1', 'row1col2', 'row1col3', 'row2col1', 'row2col2', 'row2col3', 'row3col1', 'row3col2', 'row3col3'),
                        required=True)

    parser.add_argument("--goalrow",
                        help='Enter the numbers in sequence for goal arangement starting from row 1 to row 3 space sepearted (put 0 for blank area).',
                        type=int, nargs=9, metavar=(
        'row1col1', 'row1col2', 'row1col3', 'row2col1', 'row2col2', 'row2col3', 'row3col1', 'row3col2', 'row3col3'),
                        required=True)

    args = parser.parse_args()

    x = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    # ----- Assert if Input is correct -----#

    assert set(x) == set(args.startrow)
    assert set(x) == set(args.goalrow)

    #
    # Python's assert statement is a debugging aid that tests a condition.
    # If the condition is true, it does nothing and your program just continues to execute.
    # But if the assert condition evaluates to false, it raises an AssertionError exception with an optional error message.
    #
    # ----- Reformat Input -----#

    startloc = [args.startrow[0:3], args.startrow[3:6], args.startrow[6:]]
    goalloc = [args.goalrow[0:3], args.goalrow[3:6], args.goalrow[6:]]
    # The special syntax *args in function definitions in python is used to pass a variable number of arguments to a function

    # ----- Initalize start and end node -----#

    start = BoxPattern(startloc, 0)
    goal = BoxPattern(goalloc, 0, 'goal')

    # ----- Initilaize DlsDiagram -----#

    uber_driver = DlsDiagram(start, goal)
    Res=uber_driver.solve()
    print("Uber Driver Found at " ,Res)

    file1 = open('output.txt', 'a')

    # Saving file and w is to write everytime in the file so if the file is closed no data will be removed.

    Elements = Simple_DlsDiagram(7)
    Elements.drawanedgebetweenpoints('A', 'B')
    Elements.drawanedgebetweenpoints('A', 'C')
    Elements.drawanedgebetweenpoints('B', 'D')
    Elements.drawanedgebetweenpoints('B', 'E')
    Elements.drawanedgebetweenpoints('C', 'F')
    Elements.drawanedgebetweenpoints('C', 'G')
    Elements.Print()
    start = 'A'
    goal = 'F'
    limit = 3

    print("Start is ", start)

    Res1 = Elements.dls(start, goal, limit)

    print(Res1)

    file1.close()
