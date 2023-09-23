def testFunc(nums, val):
    end = len(nums) - 1
    checking = end
    k = end + 1
    while(checking >= 0):
        if(nums[checking] == val):
            nums[checking] = nums[end]
            k -= 1
            end -= 1
        checking -= 1
    print(nums)
    print(k)

arr = [0,1,2,2,3,0,4,2]
testFunc(arr, 2)
