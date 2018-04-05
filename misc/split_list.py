'''
http://stackoverflow.com/questions/2130016/splitting-a-list-of-arbitrary-size-into-only-roughly-n-equal-parts
http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python/312464#312464
'''
import numpy as np

def chunks0(seq, num):
    avg = float(len(seq)) / float(num)
    print(avg)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

def chunks1(l, n):
    """
    Yield successive n-sized chunks from l.
    """
    out = []
    for i in xrange(0, len(l), n):
        out.append(l[i:i+n])
    return out

def chunks2(l,n):
    split = []
    start = 0
    end = len(l)
    step = (end-start)//n + 1
    for i in range(n):
        starti = start + i * step
        endi = min(start + (i + 1) * step, end)
        split.append(l[starti:endi])
    return split

if __name__ == "__main__":
    l = range(124*17)
    n = 48*2
    c = chunks2(l, n)
    print np.array(c)