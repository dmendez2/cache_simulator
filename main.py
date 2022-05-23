import numpy as np
import math
import matplotlib.pyplot as plt 
from hexConvertor import hex_to_binary
from binaryConvertor import binary_to_hex
from Fully_Associative import fully_associative_FIFO
from Fully_Associative import fully_associative_LRU
from Direct_Mapped import direct_mapped
from Set_Associative import N_way_set_associative_FIFO
from Set_Associative import N_way_set_associative_LRU
from readFile import read

main_memory = read("swim")
addressSize = 32
cacheSize = 2048
#blockSize = 8
direct = []
fa_FIFO = []
fa_LRU = []
two_way_FIFO = []
two_way_LRU = []
four_way_FIFO = []
four_way_LRU = []
block_size_data = []

N = 2;
while(N < 10):
    block_size_data.append(N)
    blockSize = 2**N
    direct.append(direct_mapped(main_memory,addressSize,blockSize,cacheSize))
    print("Directly Mapped Trial ", N, " Complete")
    fa_FIFO.append(fully_associative_FIFO(main_memory,addressSize,blockSize,cacheSize))
    print("Fully Associative FIFO Trial ", N, " Complete")
    fa_LRU.append(fully_associative_LRU(main_memory,addressSize,blockSize,cacheSize))
    print("Fully Associative LRU Trial ", N, " Complete")
    two_way_FIFO.append(N_way_set_associative_FIFO(main_memory, addressSize, blockSize, cacheSize, 2))
    print("Two Way Set Associative FIFO Trial ", N, " Complete")
    two_way_LRU.append(N_way_set_associative_LRU(main_memory, addressSize, blockSize, cacheSize, 2))
    print("Two Way Set Associative LRU Trial ", N, " Complete")
    four_way_FIFO.append(N_way_set_associative_FIFO(main_memory, addressSize, blockSize, cacheSize, 4))
    print("Four Way Set Associative FIFO Trial ", N, " Complete")
    four_way_LRU.append(N_way_set_associative_LRU(main_memory, addressSize, blockSize, cacheSize, 4))
    print("Four Way Set Associative LRU Trial ", N, " Complete")
    N += 1

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(block_size_data, direct, color = 'k', label = 'Directly Mapped')
ax.plot(block_size_data, fa_FIFO, color = 'b', label = 'Fully Associative FIFO')
ax.plot(block_size_data, fa_LRU, color = 'r', label = 'Fully Associative LRU')
ax.plot(block_size_data, two_way_FIFO, color = 'c', label = 'Two Way Set Associative FIFO')
ax.plot(block_size_data, two_way_LRU, color = 'y', label = 'Two Way Set Associative LRU')
ax.plot(block_size_data, four_way_FIFO, color = 'm', label = 'Four Way Set Associative FIFO')
ax.plot(block_size_data, four_way_LRU, color = 'g', label = 'Four Way Set Associative LRU')
ax.set_xlabel("Block Size (Power of 2)")
ax.set_ylabel("Hit Rate (%)")
ax.set_title("Effect of Changing Block Size with Cache Size Constant at 2048 Bytes")
ax.legend()
fig.savefig("figures/Changing_Block_Size.png")


#eight_way_FIFO = []
#eight_way_LRU = []
#sixteen_way_FIFO = []
#sixteen_way_LRU = []

#two_way_LRU.append(N_way_set_associative_LRU(main_memory,addressSize,blockSize,cacheSize,2))
#two_way_FIFO.append(N_way_set_associative_FIFO(main_memory,addressSize,blockSize,cacheSize,2))
#four_way_LRU.append(N_way_set_associative_LRU(main_memory,addressSize,blockSize,cacheSize,4))
#four_way_FIFO.append(N_way_set_associative_FIFO(main_memory,addressSize,blockSize,cacheSize,4))
#eight_way_LRU.append(N_way_set_associative_LRU(main_memory,addressSize,blockSize,cacheSize,8))
#eight_way_FIFO.append(N_way_set_associative_FIFO(main_memory,addressSize,blockSize,cacheSize,8))
#sixteen_way_LRU.append(N_way_set_associative_LRU(main_memory,addressSize,blockSize,cacheSize,16))
#sixteen_way_FIFO.append(N_way_set_associative_FIFO(main_memory,addressSize,blockSize,cacheSize,16))

#mainMemory2 = read("gcc")
#direct.append(direct_mapped(mainMemory2,addressSize,blockSize,cacheSize))
#fa_FIFO.append(fully_associative_FIFO(mainMemory2,addressSize,blockSize,cacheSize))
#fa_LRU.append(fully_associative_LRU(mainMemory2,addressSize,blockSize,cacheSize))
#two_way_LRU.append(N_way_set_associative_LRU(mainMemory2,addressSize,blockSize,cacheSize,2))
#two_way_FIFO.append(N_way_set_associative_FIFO(mainMemory2,addressSize,blockSize,cacheSize,2))                                                                                                  
#four_way_LRU.append(N_way_set_associative_LRU(mainMemory2,addressSize,blockSize,cacheSize,4))                                                                                                   
#four_way_FIFO.append(N_way_set_associative_FIFO(mainMemory2,addressSize,blockSize,cacheSize,4))                                                                                                 
#eight_way_LRU.append(N_way_set_associative_LRU(mainMemory2,addressSize,blockSize,cacheSize,8))                                                                                                  
#eight_way_FIFO.append(N_way_set_associative_FIFO(mainMemory2,addressSize,blockSize,cacheSize,8))                                                                                                
#sixteen_way_LRU.append(N_way_set_associative_LRU(mainMemory2,addressSize,blockSize,cacheSize,16))                                                                                               
#sixteen_way_FIFO.append(N_way_set_associative_FIFO(mainMemory2,addressSize,blockSize,cacheSize,16))    

#barWidth = 0.1
#fig = plt.figure()
#ax = fig.add_subplot(111)
#traceFile = ['gcc', 'swim']
#br1 = np.arange(len(two_way_FIFO))
#br2 = [x+barWidth for x in br1]
#br3 = [x+barWidth for x in br2]
#br4 = [x+barWidth for x in br3]

#ax.bar(br1, two_way_FIFO, color ='r', width = barWidth,edgecolor ='grey', label ='Two_Way_FIFO')
#ax.bar(br2, four_way_FIFO, color ='b', width = barWidth,edgecolor ='grey', label ='Four_Way_FIFO')
#ax.bar(br3, eight_way_FIFO, color ='m', width = barWidth,edgecolor ='grey', label ='Eight_Way_FIFO')
#ax.bar(br4, sixteen_way_FIFO, color ='g', width = barWidth,edgecolor ='grey', label ='Sixteen_Way_FIFO')

#ax.set_xlabel("Trace File Run")
#ax.set_ylabel("Hit Rate (%)")
#plt.xticks([r + barWidth for r in range(len(two_way_FIFO))],traceFile)
#ax.legend()
#fig.savefig("Figure_12.png")

#barWidth = 0.1
#fig2 = plt.figure()
#ax2 = fig2.add_subplot(111)
#traceFile = ['gcc', 'swim']
#br5 = np.arange(len(two_way_FIFO))
#br6 = [x+barWidth for x in br5]
#br7 = [x+barWidth for x in br6]
#br8 = [x+barWidth for x in br7]

#ax2.bar(br5, two_way_LRU, color ='r', width = barWidth,edgecolor ='grey', label ='Two_Way_LRU')
#ax2.bar(br6, four_way_LRU, color ='b', width = barWidth,edgecolor ='grey', label ='Four_Way_LRU')
#ax2.bar(br7, eight_way_LRU, color ='m', width = barWidth,edgecolor ='grey', label ='Eight_Way_LRU')
#ax2.bar(br8, sixteen_way_LRU, color ='g', width = barWidth,edgecolor ='grey', label ='Sixteen_Way_LRU')

#ax2.set_xlabel("Trace File Run")
#ax2.set_ylabel("Hit Rate (%)")
#plt.xticks([r + barWidth for r in range(len(two_way_LRU))],traceFile)
#ax2.legend()
#fig2.savefig("Figure_13.png")

#barWidth = 0.1
#fig3 = plt.figure()
#ax3 = fig3.add_subplot(111)
#traceFile = ['gcc', 'swim']
#br9 = np.arange(len(direct))
#br10 = [x+barWidth for x in br9]
#br11 = [x+barWidth for x in br10]

#ax3.bar(br9, direct, color ='r', width = barWidth,edgecolor ='grey', label ='Directly_Mapped')
#ax3.bar(br10, fa_FIFO, color ='b', width = barWidth,edgecolor ='grey', label ='Fully_Associative_FIFO')
#ax3.bar(br11, fa_LRU, color ='m', width = barWidth,edgecolor ='grey', label ='Fully_Associative_LRU')

#ax3.set_xlabel("Trace File Run")
#ax3.set_ylabel("Hit Rate (%)")
#plt.xticks([r + barWidth for r in range(len(direct))],traceFile)
#ax3.legend()
#fig3.savefig("Figure_14.png")

