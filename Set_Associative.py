from hexConvertor import hex_to_binary
import math
import time 
import copy

class Cache_Node:
    def __init__(self, value):
        self.tag = value
        self.next_val = None
        self.prev_val = None 

class Cache_List:
     def __init__(self):
         self.head = None
         self.tail = None
         self.size = 0

     def insert_element(self,value):
        new_node = Cache_Node(value)
           
        new_node.next_val = self.head
        new_node.prev_val = None

        if(self.head != None):
            self.head.prev_val = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.size += 1

     def move_to_front(self,node):
       if(self.head == node):
           return
       elif(self.tail == node):
          temp = node.tag
          self.tail.tag = self.head.tag
          self.head.tag = temp
       else:
           temp = node.tag
           node.tag = self.head.tag
           self.head.tag = temp

     def pop(self):
         temp = self.tail
         self.tail = self.tail.prev_val
         self.tail.next_val = None
         temp = None 
         self.size -= 1

def N_way_set_associative_FIFO(memory, addressSize, blockSize, cacheCapacity, setCapacity):
    #Size Variables
    offsetSize = int(math.log2(blockSize))
    lines = 2**(int(math.log2(cacheCapacity)) - offsetSize)
    numSets = 2**(int(math.log2(lines)) - int(math.log2(setCapacity)))
    setBits = int(math.log2(numSets))
    tagSize = addressSize - offsetSize - setBits
    #Data variables
    misses = 0
    hits = 0
    #Cache Variables
    cache = {}

    length = len(memory)
    start_time = time.time()
    for ii in range(0,length): 
        current = hex_to_binary(memory[ii])
        tag = current[0:tagSize]
        setNumber = current[tagSize:(tagSize+setBits)]
        setNumber.reverse()
        setLength = len(setNumber)
        key = 0
        for jj in range(0,setLength):
            key += setNumber[jj]* (10**jj)

        if cache.get(key) == None:
            misses += 1
            set_container = Cache_List()
            set_container.insert_element(tag)
            cache[key] = set_container

        else:
            temp = cache[key].head
            bool = 0
            while(temp != None and temp.next_val != None):
                if(tag == temp.tag):
                    bool = 1
                    hits += 1
                    break
                temp = temp.next_val

            if(bool == 0 and cache[key].size != 0):
                if(tag == temp.tag):
                    bool = 1
                    hits += 1

            if(bool == 0):
                misses += 1
                if(cache[key].size != setCapacity):
                    cache[key].insert_element(tag)
                else:
                    cache[key].pop()
                    cache[key].insert_element(tag)

    end_time = time.time()
    total_time = end_time - start_time
    results = [hits,misses, total_time]
    hit_rate = 100*(hits/(hits+misses))
    return hit_rate


def N_way_set_associative_LRU(memory, addressSize, blockSize, cacheCapacity, setCapacity):
    #Size Variables
    offsetSize = int(math.log2(blockSize))
    lines = 2**(int(math.log2(cacheCapacity)) - offsetSize)
    numSets = 2**(int(math.log2(lines)) - int(math.log2(setCapacity)))
    setBits = int(math.log2(numSets))
    tagSize = addressSize - offsetSize - setBits
    #Data variables
    misses = 0
    hits = 0
    #Cache Variables
    cache = {}

    length = len(memory)
    start_time = time.time()
    for ii in range(0,length): 
        current = hex_to_binary(memory[ii])
        tag = current[0:tagSize]
        setNumber = current[tagSize:(tagSize+setBits)]
        setNumber.reverse()
        setLength = len(setNumber)
        key = 0
        for jj in range(0,setLength):
            key += setNumber[jj]* (10**jj)

        if cache.get(key) == None:
            misses += 1
            set_container = Cache_List()
            set_container.insert_element(tag)
            cache[key] = set_container

        else:
            temp = cache[key].head
            bool = 0
            while(temp != None and temp.next_val != None):
                if(tag == temp.tag):
                    cache[key].move_to_front(temp)
                    bool = 1
                    hits += 1
                    break
                temp = temp.next_val

            if(bool == 0 and cache[key].size != 0):
                if(tag == temp.tag):
                    cache[key].move_to_front(temp)
                    bool = 1
                    hits += 1

            if(bool == 0):
                misses += 1
                if(cache[key].size != setCapacity):
                    cache[key].insert_element(tag)
                else:
                    cache[key].pop()
                    cache[key].insert_element(tag)

    end_time = time.time()
    total_time = end_time - start_time
    results = [hits,misses, total_time]
    hit_rate = 100*(hits/(hits+misses))
    return hit_rate
