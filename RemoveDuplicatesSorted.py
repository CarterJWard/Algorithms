def RemoveDuplicatesSorted(nums):
    check = 1
    pos = 1
    bench = 0
    while(check <= (len(nums) - 1 )):
        if(nums[bench] != nums[check]):
            nums[pos] = nums[check]
            pos += 1
            bench += 1
        check += 1
        print(nums)
    return pos

nums = [0,0,1,1,2,2,4]
print(RemoveDuplicatesSorted(nums))
          
            
            
