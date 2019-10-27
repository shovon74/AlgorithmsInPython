def twoSum(nums,target):
    for i in range(len(nums)):
        k =i+1
        for j in range(k,len(nums)):
            print(j)
            if nums[i] + nums[j] == target:
                print(i,j)
                return [nums.index(nums[i]), nums.index(nums[j])]



nums = [3,3]
target = 6
print(twoSum(nums, target))