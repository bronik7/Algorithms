import csv

# class Hash_Table:
#     def __init__(self):
#         self.data = [[] for i in range(100)]
#     def read_csv(self):
#
#         with open("weather.csv") as csvfile:
#             text = csv.reader(csvfile,delimiter=",")
#             row_count=0
#             for row in text:
#                 if row_count!=0:
#                     self.add(row[0],row[1])
#                 if row_count==2:
#                     break
#                 row_count += 1
#
#     def add(self,key,value):
#         local_key=0
#         for i in key:
#            local_key += ord(i)
#
#
#         print(local_key)
#         local_key = local_key % 100
#
#
#         found=False
#         for i,v in enumerate(self.data[local_key]):
#
#             if len(v)==2 and v[0]==key:
#                 print(self.data[local_key][i])
#                 self.data[local_key][i]=(key,value)
#                 found =True
#         if not found:
#              self.data[local_key].append ((key, value))
#
#       #  print(self.data)
#
# c = Hash_Table()
# #c.read_csv()
# c.add('march 6',7)
# c.add('march 17',22)
# print(c.data)

class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]

t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 6"] = 314
t["march 17"] = 63457
t["march 17"] = 4457
print(t.arr)

