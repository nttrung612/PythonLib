# from collections import deque

# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")           # Terry arrives
# queue.append("Graham")          # Graham arrives
# print(queue)

# print(queue.popleft())                 # The first to arrive now leaves
# print(queue.popleft())                 # The second to arrive now leaves]
# print(queue)

class Complex:
    def __init__(self, realpart, imapart):
        self.r = realpart
        self.i = imapart


x = Complex(3.0, -4.5)
# print(x.r, x.i)

class Warehouse:
   purpose = 'storage'
   region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)

w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)
