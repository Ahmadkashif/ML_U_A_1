def removeTuple(lst):
    for x in range(len(lst)):
        if len(lst[x]) == 0:
            lst = lst.remove(lst[x])
        else:
            continue

    return lst
