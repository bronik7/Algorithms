def countingSort(nums,  top ):
    arr= [0]*(top+1)
    for x in nums:
        arr[x]+=1

    current =0

    for i in range(len(arr)):
        c = 0
        while c < arr[i]:
          nums[current]=i
          current+=1
          c+=1

    print(nums)

countingSort( [0,2,2,1,3],4)

