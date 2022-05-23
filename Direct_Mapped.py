import math
import time
from hexConvertor import hex_to_binary

def direct_mapped(memory, addressSize, blockSize, cacheCapacity):
    #Size Variables
    offsetSize = int(math.log2(blockSize))
    lines = 2**(int(math.log2(cacheCapacity)) - offsetSize)
    lineBits = int(math.log2(lines))
    tagSize = addressSize - offsetSize - lineBits
    #Data variables
    misses = 0
    hits = 0
    #Cache Variables
    cacheSize= 0
    cache = {}

    length = len(memory)
    start_time = time.time()
    for ii in range(0,length): 
        current = hex_to_binary(memory[ii])
        tag = current[0:tagSize]
        lineNumber = current[tagSize:(tagSize+lineBits)]
        lineNumber.reverse()
        lineLength = len(lineNumber)
        key = 0
        for jj in range(0,lineLength):
            key += lineNumber[jj]* (10**jj)

        if cache.get(key) == None:
            misses += 1
            cache[key] = tag
        else:
           if(cache[key] == tag):
               hits += 1
           else:
               misses += 1
               cache[key] = tag
    end_time = time.time()
    total_time = end_time - start_time
    results = [hits,misses, total_time]
    hit_rate = 100*(hits/(hits+misses))
    return hit_rate
