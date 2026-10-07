import ctypes
import sys

class PyObject(ctypes.Structure):
    pass

PyObject._fields_ = [
    ("ob_refcnt", ctypes.c_ssize_t),
    ("ob_type", ctypes.c_void_p),
]

class PyLongObject(PyObject):
    _fields_ = [
        ("ob_size", ctypes.c_ssize_t),
        ("ob_digit", ctypes.c_uint32 * 1)

    ]

val = 999999999
old_id = id(val)

py_obj = PyLongObject.from_address(old_id)
print(f"1. Dastlabki ID: {old_id}")
print(f"   Xotiradagi ref_count: {py_obj.ob_refcnt}")

val = val + 1
new_id = id(val)

print(f"\n2. Yangilangan ID: {new_id}")
print(f"   ID o'zgardimi?: {old_id != new_id}")

py_obj_old = PyLongObject.from_address(old_id)
print(f"   Eski ID xotiradagi holati (ref_count): {py_obj_old.ob_refcnt}")

class SmartAttribute:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        print(f"  [Xotira signal] '{self.name}' o'zgardi -> Ob'ekt xotirada qayta yaratilmoqda...")
        instance.__dict__[self.name] = value


class ImmutableWrapper:
    data = SmartAttribute("data")

    def __init__(self, data):
        self.data = data

    def update_with_new_identity(self, new_data):
        new_instance = ImmutableWrapper(new_data)
        return new_instance


obj1 = ImmutableWrapper("A holat")
print(f"Obj1 -> Qiymat: {obj1.data} | ID: {id(obj1)}")

obj2 = obj1.update_with_new_identity("B holat")
print(f"Obj2 -> Qiymat: {obj2.data} | ID: {id(obj2)}")

print(f"ID lar farqli: {id(obj1) != id(obj2)}")

import copy

class StrictStructure:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

s1 = StrictStructure(10, 20)
print(f"Original Slot-Object ID: {id(s1)}")

s2 = copy.copy(s1)
s2.x = 99

print(f"Nusxalangan Slot-Object ID: {id(s2)}")
print(f"Xotira manzili mutlaqo boshqa: {id(s1) != id(s2)}")