def removeTuple(lst):
    length = len(lst)
    for x in range(len(lst)):
        if x == length:
            continue;
        elif len(lst[x]) == 0:
            lst = lst.remove(lst[x])
        else:
            continue;
    return lst[x]
