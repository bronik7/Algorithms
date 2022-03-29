def twoSum( nums: list[int], target: int) -> list[int]:
    hashtable={}
    for key,value in enumerate(nums):
        remainder= target-nums[key]
        if remainder in hashtable:
            return [key,hashtable[remainder]]

        hashtable[value]=key




print(twoSum([3,2,3],6))

# my_dict = {'fruit':'apple','colour':'blue','meat':'beef'}
# print ([key for key, value in my_dict.items() if value == 'apple'])
