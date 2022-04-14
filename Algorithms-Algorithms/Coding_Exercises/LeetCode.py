from urllib3.connectionpool import xrange


def twoSum( nums: list[int], target: int) -> list[int]:
    hashtable={}
    for key,value in enumerate(nums):
        remainder= target-nums[key]
        if remainder in hashtable:
            return [key,hashtable[remainder]]

        hashtable[value]=key




#print(twoSum([3,2,3],6))

#my_dict = {'fruit':'apple','colour':'blue','meat':'beef'}
# print ([key for key, value in my_dict.items() if value == 'apple'])



def longestCommonPrefix( strs: list[str]) -> str:
    if len(strs) == 0:
        return ''
    res = ''
    strs = sorted(strs)



    for i in strs[0]:

        if strs[-1].startswith(res + i):
            res += i
        else:
            break
    print(res)

#longestCommonPrefix(["flower","flow","flight","wwue"])
#longestCommonPrefix(["ab","a"])


def countAndSay( n: int):
    count =[]
    value =[]
    counter =0


    for x in  str(n):
        if counter !=x:
            count.append(x)
            value.append(1)
            counter=x
        else:

            index = count.index(x)
            value[index] += 1

    z = list(map(str,count))
    v = list(map(str,value))
    print(z)
    print(v)
    b = 45


    x=  f"{''.join([str(b) + str(a) for a,b in zip(list(map(str,count)),list(map(str,value)))])}"
    print(x)


#countAndSay(33453)

class Solution:
    def say(self, num: str) -> str:
        n = len(num)
        if n == 1:
            return '1'+num
        ans = ''
        count = 1
        for i in range(1, n):
            if num[i] != num[i-1]:
                ans += str(count)+num[i-1]
                count = 0
            count += 1
        ans += str(count)+num[n-1]

        return ans

    def countAndSay(self, n: int) -> str:
        ans = '1'
        for i in range(1, n):
            ans = self.say(ans)

        return ans

s = Solution()
#print(s.countAndSay(4))

def romanToInt( s: str) -> int:
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    number = 0
    if len(s) == 1: return number

    index=1
    number=symbols.get(s[0])
    while index < len(s):

       if symbols.get(s[index-1]) < symbols.get(s[index]):
          value = symbols.get(s[index])-symbols.get(s[index-1])-symbols.get(s[index-1])
          number +=value
       else:
          number += symbols.get(s[index])



       index +=1

    return number



from python_dict_wrapper import wrap, unwrap
def test(fn):
    def wrapper(*args,**kwargs):
         print("inside wrapper")
         fn(args,*kwargs)
    return wrapper




@test
def Convert(lst):

    d ={}
    for a in range(0,len(lst),2):
         d[lst[a]]=lst[a+1]

    print(d)
    #res_dct = {lst[i]: lst[i+1] for i in range(0, len(lst))}
    #print(res_dct)
    #return res_dct


# Driver code
lst = ['a', 1, 'b', 2, 'c', 3]

Convert(lst)



