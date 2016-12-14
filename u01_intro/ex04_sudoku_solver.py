#!/usr/bin/env python


class SudokuTable(object):
    TABLE_SIZE = 9

    def __init__(self, d):
        self.init_square(self.TABLE_SIZE)
        if not len(d) == self.TABLE_SIZE * self.TABLE_SIZE:
            raise ValueError('Input data must contain 81 elements')
        self.input_data(d)

    def init_square(self, size):
        sq = [[]] * size
        for i in range(size):
            sq[i] = [[]] * size
        self.t = sq

    def input_data(self, d):
        for i in range(self.TABLE_SIZE):
            for j in range(self.TABLE_SIZE):
                ind = i * self.TABLE_SIZE + j
                item = d[ind]
                try:
                    item = int(item)
                except ValueError:
                    item = ''
                self.t[i][j] = item

    def get_subsqare_ranges(self, n=None, i=None, j=None):
        if n in range(self.TABLE_SIZE):
            hor_n = n // 3
            ver_n = n % 3
            hor_range = range(3*hor_n,3*hor_n+3)
            ver_range = range(3*ver_n,3*ver_n+3)
        elif i in range(self.TABLE_SIZE) and j in range(self.TABLE_SIZE):
            hor_start = i // 3 * 3
            ver_start = j // 3 * 3
            hor_range = range(hor_start, hor_start+3)
            ver_range = range(ver_start, ver_start+3)
        else:
            raise ValueError('Neither n, nor i, nor j was provided')
        return list(hor_range), list(ver_range)

    def get_elements_of_subsquare(self, n=None, i=None, j=None):
        elements_list = []
        hor_range, ver_range = self.get_subsqare_ranges(n, i, j)
        for i in hor_range:
            for j in ver_range:
                item = self.t[i][j]
                if item:
                    elements_list.append(self.t[i][j])
        return elements_list

    def get_elements_of_raw(self, i):
        elements = [el for el in self.t[i] if el]
        return elements

    def get_elements_of_column(self, j):
        elements = [el[j] for el in self.t if el[j]]
        return elements

    def get_all_elements(self):
        out = []
        for i in range(self.TABLE_SIZE):
            for j in range(self.TABLE_SIZE):
                el = self.t[i][j]
                if el:
                    out.append(el)
        return out

    def element_can_be_placed_at_cell(self, el, i, j):
        return el not in self.get_elements_of_raw(i) and \
            el not in self.get_elements_of_column(j) and \
            el not in self.get_elements_of_subsquare(i=i, j=j)

    def get_and_process_solved_elements(self, hor_range, ver_range):
        changed = False
        solved_elements = dict()

        for i in hor_range:
            for j in ver_range:
                el = self.t[i][j]
                if not el:
                    for n in range(self.TABLE_SIZE):
                        element = n + 1
                        if self.element_can_be_placed_at_cell(element, i, j):
                            solved_elements[element] = solved_elements.get(element, [])
                            if (i,j) not in solved_elements[element]:
                                solved_elements[element].append((i,j))

        for k, v in solved_elements.items():
            if len(v) == 1:
                self.t[v[0][0]][v[0][1]] = k
                changed = True

        return changed

    def solve_subsquare(self, n):
        hor_range, ver_range = self.get_subsqare_ranges(n=n)
        changed = self.get_and_process_solved_elements(hor_range, ver_range)
        return changed

    def solve_raw(self, i):
        hor_range = range(self.TABLE_SIZE)
        ver_range = range(i, i+1)
        changed = self.get_and_process_solved_elements(hor_range, ver_range)
        return changed

    def solve_column(self, j):
        hor_range = range(j, j+1)
        ver_range = range(self.TABLE_SIZE)
        changed = self.get_and_process_solved_elements(hor_range, ver_range)
        return changed

    def solve(self):
        while True:
            changed = False

            # part 1: subsquares
            squares_dict = {}
            for n in range(self.TABLE_SIZE):
                squares_dict[n] = len(self.get_elements_of_subsquare(n=n))
            square_solving_list = sorted(squares_dict, key=squares_dict.get, reverse=True)

            for n in square_solving_list:
                if self.solve_subsquare(n):
                    changed = True

            # part 2: columns
            columns_dict = {}
            for j in range(self.TABLE_SIZE):
                columns_dict[j] = len(self.get_elements_of_column(j))
            columns_list = sorted(columns_dict, key=columns_dict.get, reverse=True)

            for j in columns_list:
                if self.solve_column(j):
                    changed = True

            # part 3: raws
            raws_dict = {}
            for i in range(self.TABLE_SIZE):
                raws_dict[i] = len(self.get_elements_of_raw(i))

            raws_list = sorted(raws_dict, key=raws_dict.get, reverse=True)
            for i in raws_list:
                if self.solve_raw(i):
                    changed = True

            print('Changed: ' + str(changed))
            if not changed:
                if len(self.get_all_elements()) == self.TABLE_SIZE ** 2:
                    print('Sudoku has been solved!')
                else:
                    print('No solution has been found :=(')
                break


if __name__ == '__main__':
    d = '       591  3 86     95   4  472  18    3    56  847  8   13     34 5  765       '
    t = SudokuTable(d)
    t.solve()
    print(t.t)
