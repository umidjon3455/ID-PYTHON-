def compare_objects(obj1, obj2, name1="obj1", name2="obj2"):
    """Ikkita obyektni solishtirish funksiyasi"""
    print(f"\n{'='*50}")
    print(f"{name1}: {obj1} | ID: {id(obj1)}")
    print(f"{name2}: {obj2} | ID: {id(obj2)}")
    print(f"{name1} == {name2}: {obj1 == obj2}")
    print(f"{name1} is {name2}: {obj1 is obj2}")
    print(f"{'='*50}")


# Butun sonlar (immutable)
a, b = 10, 10
c = 10
compare_objects(a, b, "a", "b")
compare_objects(a, c, "a", "c")


# Satrlar (immutable)
s1 = "salom"
s2 = "salom"
compare_objects(s1, s2, "s1", "s2")


# Ro'yxatlar (mutable)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
compare_objects(list1, list2, "list1", "list2")
compare_objects(list1, list3, "list1", "list3")


# Lug'atlar (mutable)
d1 = {"name": "Ali", "age": 25}
d2 = {"name": "Ali", "age": 25}
compare_objects(d1, d2, "d1", "d2")


# Tuple (immutable)
t1 = (1, 2, 3)
t2 = (1, 2, 3)
compare_objects(t1, t2, "t1", "t2")


# Obyektlar
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __repr__(self):
        return f"Student({self.name}, {self.age})"
    
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

st1 = Student("Ali", 20)
st2 = Student("Ali", 20)
st3 = st1
compare_objects(st1, st2, "st1", "st2")
compare_objects(st1, st3, "st1", "st3")


# Mutable o'zgarishi
print(f"\n{'='*50}")
print("Mutable o'zgarishi:")
print(f"{'='*50}")
nums = [1, 2, 3]
nums_ref = nums
print(f"nums: {nums} | ID: {id(nums)}")
print(f"nums_ref: {nums_ref} | ID: {id(nums_ref)}")

nums.append(4)
print(f"\nnums.append(4) dan keyin:")
print(f"nums: {nums} | ID: {id(nums)}")
print(f"nums_ref: {nums_ref} | ID: {id(nums_ref)}")


# Immutable o'zgarishi
print(f"\n{'='*50}")
print("Immutable o'zgarishi:")
print(f"{'='*50}")
x = 100
x_ref = x
print(f"x: {x} | ID: {id(x)}")
print(f"x_ref: {x_ref} | ID: {id(x_ref)}")

x = 200
print(f"\nx = 200 dan keyin:")
print(f"x: {x} | ID: {id(x)}")
print(f"x_ref: {x_ref} | ID: {id(x_ref)}")


# Deep copy vs Shallow copy
print(f"\n{'='*50}")
print("Deep copy vs Shallow copy:")
print(f"{'='*50}")
import copy

nested = [1, [2, 3], 4]
shallow = copy.copy(nested)
deep = copy.deepcopy(nested)

print(f"original: {nested} | ID: {id(nested)}")
print(f"shallow: {shallow} | ID: {id(shallow)}")
print(f"deep: {deep} | ID: {id(deep)}")

nested[1].append(99)
print(f"\nnested[1].append(99) dan keyin:")
print(f"original: {nested}")
print(f"shallow: {shallow}")
print(f"deep: {deep}")
