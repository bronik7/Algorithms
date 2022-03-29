# import sys
# sys.setrecursionlimit(2000)
# def test2(n):
#     if n != 0:
#         print(n)
#         return f'{n}, {test2(n - 1)}'
#     else:
#         print("equals 0")
#         return f"equals 0"


# test2(100)


# def akk(m, n):
#     if m == 0:
#         return n + 1
#     elif m > 0 and n == 0:
#         return akk(m - 1, 1)
#     else:
#         return akk(m - 1, akk(m, n - 1))


#print(akk(2, 8))


def gcd(m,n):
    while m!=n:
        if m>n:
            m-=n
            print("printing m ", m)
        else:
            n-=m
            print("printing n ", n)

    return m
#print(gcd(9,21))

def gcd1(m,n):
      if  n==0:
          return m

      print(m%n)
      return gcd1(n,m % n)


#print(gcd1(9,21))


def gcd2(m,n):
    while n!=0:
        m,n=n,m%n
    return m

print(gcd2(54,24))