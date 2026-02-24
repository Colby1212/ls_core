#1. input is number of blocks remaining
#2. current layer = 1
#3. blocks required per layer is current layer number squared

#4. check if the blocks required is greater than or equal to remaining blocks. 
    #if blocks required is less than blocks remaining subtract number of blocks required from remaining blocks
        #increment the current layer by 1
    #if blocks required is greater than blocks remaining than the remaining blocks is # of blocks remaining
        #return remaining blocks
#5. repeat 4 until blocks required is greater than or equal to blocks remaining (hints at a loop)



def leftover_blocks(n):
    remaining_blocks = n
    current_layer = 1
    while True:
        blocks_required = current_layer**2
        if blocks_required <= remaining_blocks:
            remaining_blocks -= blocks_required
            current_layer += 1
        else:
            return abs(remaining_blocks)

print(leftover_blocks(-100))