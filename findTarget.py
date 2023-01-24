def findTargetIndex(nums,target):
    print(nums.sort())
    start = 0
    end = len(nums)-1
    if(target==0 or target < 0):
        return "target {} is at index {} sorted arr-> {}".format(target,nums.index(target),nums)
    while start<=end:
        mid = (start+end)//2
        if target == nums[mid]:
            return "Sorted Array is {} \nTarget {} found at index {}".format(nums,target,mid)
        elif start > nums[mid]:
            end = nums[mid]-1
        elif end > nums[mid]:
            start  = nums[mid]+1
        else:
            return -1
print(findTargetIndex([1,4,0,-1,6,3,2],-1))
print(findTargetIndex([1,4,0,-1,6,3,2],0))