def question1(str):
    count = 0;
    vov = ['a','e','i','o','u'];
    for x in range(len(str)):
        if str[x] in vov:
            count+=1;
        else:
            continue;
    return count;
