"""This program is able to solve Tower of Hanoi problem for upto 5 towers and 5 disks. For greater than that recursion depth is reached. Need to work on it in upcoming days. """
# towers = [[1,-1,-1],[3,-1,-1],[2,-1,-1]]
# towers = [[1,-1,-1],[3,-1,-1],[3,1,2]]
T_CNT = 5
temp = [[-1]*T_CNT for _ in range(T_CNT-1)]
towers = [[x+1 for x in reversed(range(T_CNT))]]
towers.extend(temp)
print(towers)
hist = []
def isEmpty(l):
    return True if l == [-1,-1,-1] else False
def otherTowers(i):
    ot = [ x for x in range(T_CNT) if x!=i ]    
    return ot
def nonEmptyTower(i):
    if not isEmpty(towers[i]):
        return i
    return False
def tTop(l):
    for i in reversed(l):
        if i != -1:
            return i
    return 999
def tTopInd(l):
    for i, v in enumerate( reversed(l)):
        if v != -1:
            return len(l) -1 - i
    return -1
def solved():
    if towers[T_CNT-1] == list(reversed([x+1 for x in range(T_CNT)])):
        return True
    return False
def getMoves(cur_st):
    moves = []
    for i in range(T_CNT):
        for j in range(T_CNT):
            if not i == j:
                if (not isEmpty(towers[i]) and isEmpty(towers[j])) or (tTop(towers[i])< tTop(towers[j]) ) :
                    print("tTops: ",tTop(towers[i]), tTop(towers[j]), "twrs", i,j)
                    moves.append([i,j])
    print("moves", moves)
    return moves
def compare_lists(list1, list2):
    # Check if the lengths of the lists are different
    if len(list1) != len(list2):
        # print("list len unequal")
        return False
    
    # Iterate over the elements of the lists
    for i in range(len(list1)):
        # If the elements are lists, recursively compare them
        # print("Instances: ", isinstance(list1[i], list) , isinstance(list2[i], list))
        if isinstance(list1[i], list) and isinstance(list2[i], list):
            if not compare_lists(list1[i], list2[i]):
                return False
        # If the elements are not lists, compare them directly
        else:
            if list1[i] != list2[i]:
                return False
    
    # All elements are equal
    return True
def print_integer_with_width(ints, width):
    num_str = ["{:>{width}}".format(num, width=width) for num in ints]
    print(" ".join(num_str))

def showTower():
    for h in list(reversed(range(T_CNT))):
        vals = [ towers[i][h] for i in range(T_CNT) ]
        print_integer_with_width(vals, 5)
def makeMove(m):
    d_top_ind = tTopInd(towers[m[1]])
    s_top_ind = tTopInd(towers[m[0]])
    print("Source index: ", s_top_ind,"Dest Ind: ", 1+d_top_ind)
    print("Source tower: ", m[0],"Dest twr: ", m[1])
    towers[m[1]][d_top_ind + 1] = towers[m[0]][s_top_ind]
    towers[m[0]][s_top_ind] = -1
def visited():
    for l in hist:
        if compare_lists(l,towers):
            return True
    return False
def backtrack(old_st):
    for i in range(T_CNT):
        for j in range(T_CNT):
            towers[i][j] = old_st[i][j]
def toh(towers):
    showTower()
    # input()
    if visited():
        print("Already visited. Returning")
        return False
    if solved():
        print("TOH solved. Congrats!")
        return True
    # old_st = [list(towers[0]), list(towers[1]), list(towers[2]) ]

    # Using a loop
    # old_st = []
    # for sublist in towers:
    #     old_st.append(list(sublist))
    old_st = [list(sublist) for sublist in towers]
    
    hist.append(old_st)
    moves = getMoves(towers)
    for m in moves:
        makeMove(m)
        if toh(towers):
            return True
        else:
            print("visited or truncated, Backtracking")
            backtrack(old_st)
            # print("oldsfsf", old_st)
            # print("towers", towers)
            # showTower()
    return False
    # print(towers)
toh(towers)

