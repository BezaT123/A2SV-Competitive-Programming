def countingValleys(steps, path):
    num_valleys=0
    was_in_valley=False
    level=0
    for i in range(0,steps):
        if path[i] =='D':
            level-=1
        else:
            level+=1
        if level == 0 and was_in_valley:
                num_valleys+=1
                was_in_valley=False
        if level<0:
            was_in_valley=True