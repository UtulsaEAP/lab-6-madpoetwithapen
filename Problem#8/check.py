def in_order(nums):
    # Type your code here.
    numlist =  []
    newlist = nums.copy

    for _ in range (0,len(newlist)):
        numlist.append(min,newlist)
        numlist.remove(min, newlist)
    if numlist == nums: 
        return(True)
    
    print(numlist)
    print(nums)

if __name__ == '__main__':
    # Test out-of-order example
    nums1 = [5, 6, 7, 8, 3]
    if in_order(nums1):
        print('In order')
    else:
        print('Not in order')
        
    # Test in-order example
    nums2 = [5, 6, 7, 8, 10]
    if in_order(nums2):
        print('In order')
    else:
        print('Not in order')
