import sys

x = 100
y = 100
print(f"x va y bir xil manzilga ega: {id(x) == id(y)}")  # True (bir xil ID)

a = 1000000
print(f"1. Asosiy 'a' -> Qiymat: {a} | ID: {id(a)}")


for i in range(1, 4):
    a = a + i
    print(f"2.{i}. O'zgargan 'a' -> Qiymat: {a} | ID: {id(a)} (Manzil o'zgardi)")

print("-" * 50)

tup = (1, 2)
old_id = id(tup)
print(f"Dastlabki Tuple ID: {old_id}")

tup += (3, 4)
new_id = id(tup)
print(f"Yangi Tuple ID:     {new_id}")
print(f"ID o'zgardimi? {old_id != new_id}")

print("-" * 50)

b = 9999999
b_id = id(b)
print(f"Eski 'b' ID: {b_id}")

del b

c = 8888888
print(f"Yangi 'c' ID: {id(c)}")