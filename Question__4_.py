def Question4 (dict1, dict2):
    dL1Keys = list(dict1.items());
    dL2Keys = list(dict2.items());
    dL1Vals = list(dict1.values());
    dL2Vals = list(dict2.values());
    for x in dL2Keys:
        if dL2Keys[x] in dL1Keys:
            index = dL1Keys.index(dL2Keys[x]);
            dL1Vals[index] += dL2Vals[x];
        else:
            dL1Keys.append(dL2Keys[x]);
            dL2Vals.append(dL2Vals[x]);


