"""Assignment 2 functions."""

from typing import List


THREE_BY_THREE = [[1, 2, 1],
                  [4, 6, 5],
                  [7, 8, 9]]

FOUR_BY_FOUR = [[1, 2, 6, 5],
                [4, 5, 3, 2],
                [7, 9, 8, 1],
                [1, 2, 1, 4]]

UNIQUE_3X3 = [[1, 2, 3],
              [9, 8, 7],
              [4, 5, 6]]

UNIQUE_4X4 = [[10, 2, 3, 30],
              [9, 8, 7, 11],
              [4, 5, 6, 12],
              [13, 14, 15, 16]]


def compare_elevations_within_row(elevation_map: List[List[int]], map_row: int,
                                  level: int) -> List[int]: #DONE
    """Return a new list containing the three counts: the number of
    elevations from row number map_row of elevation map elevation_map
    that are less than, equal to, and greater than elevation level.

    Precondition: elevation_map is a valid elevation map.
                  0 <= map_row < len(elevation_map).

    >>> compare_elevations_within_row(THREE_BY_THREE, 1, 5)
    [1, 1, 1]
    >>> compare_elevations_within_row(FOUR_BY_FOUR, 1, 2)
    [0, 1, 3]

    """
    new_list = [0, 0, 0]
    sl = elevation_map[map_row]
    for i in sl:
        if i < level:
            new_list[0] = new_list[0] + 1
        elif i == level:
            new_list[1] = new_list[1] + 1
        elif i > level:
            new_list[2] = new_list[2] + 1
    
    return new_list

def update_elevation(elevation_map: List[List[int]], start: List[int],
                     stop: List[int], delta: int) -> None: #DONE
    """Modify elevation map elevation_map so that the elevation of each
    cell between cells start and stop, inclusive, changes by amount
    delta.

    Precondition: elevation_map is a valid elevation map.
                  start and stop are valid cells in elevation_map.
                  start and stop are in the same row or column or both.
                  If start and stop are in the same row,
                      start's column <=  stop's column.
                  If start and stop are in the same column,
                      start's row <=  stop's row.
                  elevation_map[i, j] + delta >= 1
                      for each cell [i, j] that will change.

    >>> THREE_BY_THREE_COPY = [[1, 2, 1],
    ...                        [4, 6, 5],
    ...                        [7, 8, 9]]
    >>> update_elevation(THREE_BY_THREE_COPY, [1, 0], [1, 1], -2)
    >>> THREE_BY_THREE_COPY
    [[1, 2, 1], [2, 4, 5], [7, 8, 9]]
    >>> FOUR_BY_FOUR_COPY = [[1, 2, 6, 5],
    ...                      [4, 5, 3, 2],
    ...                      [7, 9, 8, 1],
    ...                      [1, 2, 1, 4]]
    >>> update_elevation(FOUR_BY_FOUR_COPY, [1, 2], [3, 2], 1)
    >>> FOUR_BY_FOUR_COPY
    [[1, 2, 6, 5], [4, 5, 4, 2], [7, 9, 9, 1], [1, 2, 2, 4]]

    """
    a = start[0]
    b = start[1]
    i = stop[0]
    j = stop[1]
    e = elevation_map
    if a == i:
        for x in range(b, j+1):
            e[a][x] = e[a][x] + delta
    elif b == j: #same column
        for y in range(a, i+1):
            e[y][b] = e[y][j] + delta
            
    elevation_map = e

def get_average_elevation(elevation_map: List[List[int]]) -> float: #DONE
    """Return the average elevation across all cells in the elevation map
    elevation_map.

    Precondition: elevation_map is a valid elevation map.

    >>> get_average_elevation(UNIQUE_3X3)
    5.0
    >>> get_average_elevation(FOUR_BY_FOUR)
    3.8125
    """
    length = len(elevation_map)
    s = 0
    nv = (len(elevation_map))**2
    for i in range(length):
        for j in range(length):
            s = s + elevation_map[i][j]
    return s/nv

def find_peak(elevation_map: List[List[int]]) -> List[int]: #DONE
    """Return the cell that is the highest point in the elevation map
    elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  Every elevation value in elevation_map is unique.

    >>> find_peak(UNIQUE_3X3)
    [1, 0]
    >>> find_peak(UNIQUE_4X4)
    [0, 3]
    """
    g = 0
    g_location = [0, 0]
    length = len(elevation_map)
    for i in range(length):
        for j in range(length):
            if elevation_map[i][j] > g:
                g = elevation_map[i][j]
                g_location[0] = i
                g_location[1] = j
    return g_location

def is_sink(elevation_map: List[List[int]], cell: List[int]) -> bool: #DONE
    """Return True if and only if cell exists in the elevation map
    elevation_map and cell is a sink.

    Precondition: elevation_map is a valid elevation map.
                  cell is a 2-element list.

    >>> is_sink(THREE_BY_THREE, [0, 5])
    False
    >>> is_sink(THREE_BY_THREE, [0, 2])
    True
    >>> is_sink(THREE_BY_THREE, [1, 1])
    False
    >>> is_sink(FOUR_BY_FOUR, [2, 3])
    True
    >>> is_sink(FOUR_BY_FOUR, [3, 2])
    True
    >>> is_sink(FOUR_BY_FOUR, [1, 3])
    False
    """ 
    a = cell[0]
    b = cell[1]
    e = elevation_map
    if a+1 > len(e) or b + 1 > len(e):
        return False
    
    if not re_c(e, cell):
        return False
        
    if not re_c_d(e, cell):
        return False
        
    return True

def find_local_sink(elevation_map: List[List[int]],
                    cell: List[int]) -> List[int]:
    """Return the local sink of cell cell in elevation map elevation_map.

    Precondition: elevation_map is a valid elevation map.
                  elevation_map contains no duplicate elevation values.
                  cell is a valid cell in elevation_map.

    >>> find_local_sink(UNIQUE_3X3, [1, 1])
    [0, 0]
    >>> find_local_sink(UNIQUE_3X3, [2, 0])
    [2, 0]
    >>> find_local_sink(UNIQUE_4X4, [1, 3])
    [0, 2]
    >>> find_local_sink(UNIQUE_4X4, [2, 2])
    [2, 1]
    """
    l = [cell[0], cell[1]]
    e = elevation_map
    [a, b] = [cell[0], cell[1]]
    if ceup(a-1, b, l[0], l[1], e):
        l = [a-1, b]
    if cedown(a+1, b, l[0], l[1], e):
        l = [a+1, b]
    if celeft(a, b-1, l[0], l[1], e):
        l = [a, b-1]
    if ceright(a, b+1, l[0], l[1], e):
        l = [a, b+1]
    if ceul(a-1, b-1, l[0], l[1], e):
        l = [a-1, b-1]
    if ceur(a-1, b+1, l[0], l[1], e):
        l = [a-1, b+1]    
    if cedl(a+1, b-1, l[0], l[1], e):
        l = [a+1, b-1]    
    if cedr(a+1, b+1, l[0], l[1], e):
        l = [a+1, b+1] 
    return l

def can_hike_to(elevation_map: List[List[int]], start: List[int],
                dest: List[int], supplies: int) -> bool:
    """Return True if and only if a hiker can go from start to dest in
    elevation_map without running out of supplies.

    Precondition: elevation_map is a valid elevation map.
                  start and dest are valid cells in elevation_map.
                  dest is North-West of start.
                  supplies >= 0

    >>> map = [[1, 6, 5, 6],
    ...        [2, 5, 6, 8],
    ...        [7, 2, 8, 1],
    ...        [4, 4, 7, 3]]
    >>> can_hike_to(map, [3, 3], [2, 2], 10)
    True
    >>> can_hike_to(map, [3, 3], [2, 2], 8)
    False
    >>> can_hike_to(map, [3, 3], [3, 0], 7)
    True
    >>> can_hike_to(map, [3, 3], [3, 0], 6)
    False
    >>> can_hike_to(map, [3, 3], [0, 0], 18)
    True
    >>> can_hike_to(map, [3, 3], [0, 0], 17)
    False
    """
    low = 0
    e = elevation_map
    while True:
        if start[0] - 1 < 0:
            if start[0] == dest[0] and start[1]-1 == dest[1]: 
                return north_off(start[0], start[1], e, supplies) 
            low = abs(e[start[0]][start[1]-1] - e[start[0]][start[1]])
            [start[0], start[1]] = [start[0], start[1]-1]
        elif start[1] - 1 < 0:
            if start[0] - 1 == dest[0] and start[1] == dest[1]:
                return west_off(start[0], start[1], e, supplies)
            low = abs(e[start[0]-1][start[1]] - e[start[0]][start[1]])
            [start[0], start[1]] = [start[0]-1, start[1]]
        else:
            if start[0] - 1 == dest[0] and start[1] == dest[1]:
                n = abs(e[start[0]][start[1]] - e[dest[0]][dest[1]])
                return check_supplies(supplies, n)
            elif start[0] == dest[0] and start[1] - 1 == dest[1]:
                w = abs(e[start[0]][start[1]] - e[dest[0]][dest[1]])
                return check_supplies(supplies, w)
            n = abs(e[start[0]-1][start[1]] - e[start[0]][start[1]])
            w = abs(e[start[0]][start[1]-1] - e[start[0]][start[1]])
            if start[0] == dest[0]:
                low = w
                [start[0], start[1]] = [start[0], start[1]-1]
            elif start[1] == dest[1]:
                low = n
                [start[0], start[1]] = [start[0]-1, start[1]]
            else:
                low = min(n, w)
                if n == w:
                    [start[0], start[1]] = [start[0]-1, start[1]]
                elif low == n:
                    [start[0], start[1]] = [start[0]-1, start[1]]
                elif low == w:
                    [start[0], start[1]] = [start[0], start[1]-1]
        supplies = supplies - low

def get_lower_resolution(elevation_map: List[List[int]]) -> List[List[int]]:
    """Return a new elevation map, which is constructed from the values
    of elevation_map by decreasing the number of elevation points
    within it.

    Precondition: elevation_map is a valid elevation map.

    >>> get_lower_resolution(
    ...     [[1, 6, 5, 6],
    ...      [2, 5, 6, 8],
    ...      [7, 2, 8, 1],
    ...      [4, 4, 7, 3]])
    [[3, 6], [4, 4]]
    >>> get_lower_resolution(
    ...     [[7, 9, 1],
    ...      [4, 2, 1],
    ...      [3, 2, 3]])
    [[5, 1], [2, 3]]

    """
    a = elevation_map[0][0]
    b = elevation_map[0][1]
    c = elevation_map[1][0]
    d = elevation_map[1][1]
    x = (a + b + c + d) // 4    
    if len(elevation_map) == 2:
        new_ele = [0]
        new_ele[0] = x
    if len(elevation_map) == 3:
        new_ele = [[0, 0], [0, 0]]
        new_ele[0][0] = x
        a = elevation_map[0][2]
        b = elevation_map[1][2]
        new_ele[0][1] = (a + b) // 2
        a = elevation_map[2][0]
        b = elevation_map[2][1]
        new_ele[1][0] = (a + b) // 2
        new_ele[1][1] = elevation_map[2][2]
    if len(elevation_map) == 4:
        new_ele = [[0, 0], [0, 0]]
        new_ele[0][0] = x
        a = elevation_map[0][2]
        b = elevation_map[1][2]
        c = elevation_map[0][3]
        d = elevation_map[1][3]
        new_ele[0][1] = (a + b + c + d) // 4
        a = elevation_map[2][0]
        b = elevation_map[2][1]
        c = elevation_map[3][0]
        d = elevation_map[3][1]        
        new_ele[1][0] = (a + b + c + d) // 4
        a = elevation_map[2][2]
        b = elevation_map[2][3]
        c = elevation_map[3][2]
        d = elevation_map[3][3]        
        new_ele[1][1] = (a + b + c + d) // 4    
        
    return new_ele

def north_off(a: int, b: int, e_map: List[List[int]], supplies: int) -> bool:
    """Return True if north of row a and column b is off e_map, 
    west is the destination and supplies is greater or equal to 0. 
    Return False if north is off e_map, west is the destination and 
    supplies is less than 0.
    
    Precondition: e_map is a valid map
    
    >>> north_off(0, 1, THREE_BY_THREE, 6)
    True
    >>> north_off(0, 1, THREE_BY_THREE, 0)
    False
    """
    w = abs(e_map[a][b-1] - e_map[a][b])
    return check_supplies(supplies, w)

def west_off(a: int, b: int, e_map: List[List[int]], supplies: int) -> bool:
    """Return True if west of row a and column b is off e_map, 
    north is the destination and supplies is greater or equal to 0. 
    Return False if west is off e_map, north is the destination and 
    supplies is less than 0.
    
    Precondition: e_map is a valid map
    
    >>> west_off(1, 0, THREE_BY_THREE, 2)
    False
    >>> west_off(1, 0, THREE_BY_THREE, 6)
    True
    """
    n = abs(e_map[a-1][b] - e_map[a][b])
    return check_supplies(supplies, n)

def check_supplies(supplies: int, delta: int) -> bool:
    """Return True if supplies minus delta, the number of 
    supplies needed to move to a different elevation, is greater or
    equal to 0.
    
    >>>check_supplies(7, 3)
    True
    >>> check_supplies(4, 5)
    False
    """
    if supplies - delta >= 0:
        return True
    return False
    
def ceup(x: int, y: int, i: int, j: int, e_map: List[List[int]]) -> bool:
    """Return True if the elevation in the row x and column y in e_map is 
    less than the elevation in the row i and column j in e_map 
    and it is a valid point in e_map. Return False if it does not.
    Checks for the elevation above the current point.

    Precondition: e_map is a valid elevation map.

    >>> ceup(0, 1, 1, 1, THREE_BY_THREE)
    True
    >>> ceup(0, 2, 1, 2, FOUR_BY_FOUR)
    False
    """    
    if x >= 0:
        if e_map[x][y] < e_map[i][j]:
            return True
    return False
        
def cedown(x: int, y: int, i: int, j: int, e_map: List[List[int]]) -> bool:
    """Return True if the elevation in the row x and column y in e_map 
    is less than the elevation in the row i and column j in e_map 
    and it is a valid point in e_map. Return False if it does not.
    Checks for the elevation below the current point.

    Precondition: e_map is a valid elevation map.

    >>> cedown(-1, 1, 1, 1, THREE_BY_THREE)
    False
    >>> cedown(1, 2, 0, 2, FOUR_BY_FOUR)
    True
    """        
    if x < len(e_map):
        if e_map[x][y] < e_map[i][j]:
            return True
    return False

def ceright(x: int, y: int, i: int, j: int, e_map: List[List[int]]) -> bool:
    """Return True if the elevation in the row x and column y in e_map 
    is less than the elevation in the row i and column j in e_map
    and it is a valid point in e_map. Return False if it does not.
    Checks for the elevation to the right of the current point.

    Precondition: e_map is a valid elevation map.

    >>> ceright(0, 0, 0, 1, THREE_BY_THREE)
    True
    >>> ceright(0, 3, 0, 2, FOUR_BY_FOUR)
    True
    """        
    if y < len(e_map):
        if e_map[x][y] < e_map[i][j]:
            return True
    return False
        
def celeft(x: int, y: int, i: int, j: int, e_map: List[List[int]]) -> bool:
    """Return True if the elevation in the row x and column y in e_map
    is less than the elevation in the row i and column j in e_map 
    and it is a valid point in e_map. Return False if it does not.
    Checks for the elevation to the left of the current point.

    Precondition: e_map is a valid elevation map.

    >>> celeft(0, 0, 0, 1, THREE_BY_THREE)
    True
    >>> celeft(0, -1, 0, 2, FOUR_BY_FOUR)
    False
    """            
    if y >= 0:
        if e_map[x][y] < e_map[i][j]:
            return True
    return False

def ceul(x: int, y: int, i: int, j: int, e_map: List[List[int]]) -> bool:
    """Return True if the elevation in the row x and column y in e_map 
    is less than the elevation in the row i and column j in e_map 
    and it is a valid point in e_map. Return False if it does not.
    Checks for the elevation above and to the left of the current point.

    Precondition: e_map is a valid elevation map.

    >>> ceul(0, 0, 1, 1, THREE_BY_THREE)
    True
    >>> ceul(0, 2, 1, 3, FOUR_BY_FOUR)
    False
    """            
    if x >= 0 and y >= 0:
        if e_map[x][y] < e_map[i][j]:
            return True
    return False
        
def ceur(x: int, y: int, i: int, j: int, e_map: List[List[int]]) -> bool:
    """Return True if the elevation in the row x and column y in e_map
    is less than the elevation in the row i and column j in e_map 
    and it is a valid point in e_map. Return False if it does not.
    Checks for the elevation above andto the right of the current
    point.

    Precondition: e_map is a valid elevation map.

    >>> ceur(0, 2, 1, 1, THREE_BY_THREE)
    True
    >>> ceur(0, 3, 1, 2, FOUR_BY_FOUR)
    False
    """                
    if x >= 0 and y < len(e_map):
        if e_map[x][y] < e_map[i][j]:
            return True
    return False
        
def cedl(x: int, y: int, i: int, j: int, e_map: List[List[int]]) -> bool:
    """Return True if the elevation in the row x and column y in e_map 
    is less than the elevation in the row i and column j in e_map
    and it is a valid point in e_map. Return False if it does not.
    Checks for the elevation below and to the left of the current point.

    Precondition: e_map is a valid elevation map.

    >>> cedl(1, 0, 0, 1, THREE_BY_THREE)
    False
    >>> cedl(5, 3, 1, 2, FOUR_BY_FOUR)
    False
    """           
    if x < len(e_map) and y >= 0:
        if e_map[x][y] < e_map[i][j]:
            return True
    return False
        
def cedr(x: int, y: int, i: int, j: int, e: List[List[int]]) -> bool:
    """Return True if the elevation in the row x and column y in e 
    is less than the elevation in the row i and column j in e 
    and it is a valid point in e. Return False if it does not.
    Checks for the elevation below andto the right 
    of the current point.

    Precondition: e is a valid elevation map.

    >>> cedr(2, 2, 1, 1, THREE_BY_THREE)
    False
    >>> cedr(3, 3, 2, 2, FOUR_BY_FOUR)
    True
    """           
    if x < len(e) and y < len(e):
        if e[x][y] < e[i][j]:
            return True
    return False

def re_c(e: List[List[int]], cell: List[int]) -> bool:
    """Return False if the elevation in cell in e is greater 
    than the elevations above, below, to the left, 
    or to the right of the cell. Return True if all elevations 
    above, below, to the left, and to the right of the cell
    is less than the elevation in cell.

    Precondition: e is a valid elevation map and cell is a valid
    elevation in e

    >>> re_c(THREE_BY_THREE, [2, 2])
    False
    >>> re_c(FOUR_BY_FOUR, [0, 0])
    True
    """           
    a = cell[0]
    b = cell[1]
    if ceup(a-1, b, a, b, e):
        return False
    if cedown(a+1, b, a, b, e):
        return False
    if celeft(a, b-1, a, b, e):
        return False
    if ceright(a, b+1, a, b, e):
        return False    
    return True

def re_c_d(elevation_map: List[List[int]], cell: List[int]) -> bool:
    """Return False if the elevation in cell in elevation_map 
    is greater than any of the elevations diagonally to the cell.  
    Return True if all elevations diagonally to the cell
    is less than the elevation in cell.

    Precondition: elevation_map is a valid elevation map and cell is a valid
    elevation in elevation_map

    >>> re_c_d(THREE_BY_THREE, [1, 1])
    False
    >>> re_c_d(FOUR_BY_FOUR, [0, 0])
    True
    """           
    a = cell[0]
    b = cell[1]
    e = elevation_map
    if ceul(a-1, b-1, a, b, e):
        return False
    if ceur(a-1, b+1, a, b, e):
        return False
    if cedl(a+1, b-1, a, b, e):
        return False
    if cedr(a+1, b+1, a, b, e):
        return False    
    return True