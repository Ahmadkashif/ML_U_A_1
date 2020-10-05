def question4(dict1, dict2):
    dL1Keys = list(dict1.keys());
    dL2Keys = list(dict2.keys());
    dL1Vals = list(dict1.values());
    dL2Vals = list(dict2.values());
    for x in range(len(dL2Keys)):
        if dL2Keys[x] in dL1Keys:
            index = dL1Keys.index(dL2Keys[x]);
            dL1Vals[index] += dL2Vals[x];
        else:
            dL1Keys.append(dL2Keys[x]);
            dL1Vals.append(dL2Vals[x]);

    for x in range(len(dL1Keys)):
            dict1[dL1Keys[x]] = dL1Vals[x];

    return  dict1;





