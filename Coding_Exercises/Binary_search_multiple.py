from jovian.pythondsa import evaluate_test_cases

#1,2,3,4,5,6,7 target 6



def find_first_position(cards,query):
    low,high = 0,len(cards)-1

    while low<=high:
        mid = (low + high) // 2
        middleCard = cards[mid]
        print("low ",low, " high ", high, "mid ", mid , "middlecard ",middleCard)
        if middleCard == query:
            if cards[mid-1]==query:
                high= mid-1
            else:
                return mid
        elif middleCard < query:
            high = mid-1
        elif middleCard > query:
            low = mid +1
    return -1

def find_last_position(cards,query):
    low,high = 0,len(cards)-1

    while low<=high:
        mid = (low + high) // 2
        middleCard = cards[mid]
        print("low ",low, " high ", high, "mid ", mid , "middlecard ",middleCard)
        if middleCard == query:
            if cards[mid+1]==query:
                low= mid+1
            else:
                return mid
        elif middleCard < query:
            high = mid-1
        elif middleCard > query:
            low = mid +1
    return -1

#print(find_first_position([13, 11, 8, 7,  4,],7))
#print(find_last_position([8,8,8,8,8,7,7,7,7,5,4,3,2,1],7))

# tests = [{'input': {'cards': [13, 7, 4], 'query': 7}, 'output': 1}]
# tests.append({'input': {'cards': [], 'query': 7}, 'output': -1})
# tests.append({'input': {'cards': [13, 11, 8, 7,  4,], 'query': 7}, 'output': 3})
# tests.append({'input': {'cards': [13,8, 4,2, 1], 'query': 7}, 'output': -1})
# tests.append({'input': {'cards': [13,8, 4,2, 1], 'query': 13}, 'output': 0})
# tests.append({'input': {'cards': [7,7,7,7,5,4,3,2,1], 'query': 7}, 'output': 0})
# tests.append({'input': {'cards': [8,8,8,8,8,7,7,7,7,5,4,3,2,1], 'query': 7}, 'output': 5})
# #tests.append({'input': {'cards': list(range(100000000,0,-1)), 'query': 2}, 'output': 99999998})
# print(evaluate_test_cases(find_first_position, tests))
# t = [{'input': {'cards': [8,8,8,8,8,7,7,7,7,5,4,3,2,1], 'query': 7}, 'output': 8}]
# print(evaluate_test_cases(find_last_position,t))


def count_rotations(nums):
    low, high = 0,len(nums)-1

    while low <= high:
        mid = low+(high-low)//2
        midNum = nums[mid]
        if mid >=0 and nums[mid - 1] > midNum:
            return mid
        elif midNum > nums[high]:
            low = mid + 1
        elif midNum > nums[low] :
            high = mid - 1
    return 0


#print(count_rotations([5,7,8,9,10,2]))


s ="abbbabaaa"
dict = []
count = 0
if len(s) == 1: print(s)
for x in s:
    if x not in dict:
        dict.append(x)
    else:
              if dict[len(dict)-1] == x:
                  dict.pop()
              else:
                  dict.append(x)

#print("".join(dict))


import random as rand
def shuffle( vals:list ):
   print("original list", vals ,"\n")
   for i in range(len(vals)-1):
       random_value = rand.randint(0,i+1)

       temp = vals[i]

       vals[i]=vals[random_value]

       vals[random_value]=temp
   return vals


#print(shuffle([1,2,3,4]))

def find_sums(vals: list):
    if len(vals)==0: return -1
    totals=[None for k in range(len(vals))]

    totals[0]= vals[0]
    for i in range(1,len(vals)):
        totals[i]=totals[i-1]+vals[i]

    for i in range(1, len(totals)-1):
        left = totals[i-1]
        right = totals[len(totals)-1]-totals[i]
        if left==right:
            return i
    return -1

#print(find_sums([1,0,2,10,-10,-1,0]))
#1,3,13,3,2,0

def a(n):
    return n+n + "HEREE"  

print(list(map(a,"hehll")))

l =['test','black']
b =["white","zap"]
print(list(zip(l,b)))
