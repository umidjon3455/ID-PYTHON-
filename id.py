a = 1
print(f"1-qator -> Son: {a}, ID: {id(a)}")

a = 2
print(f"2-qator -> Son: {a}, ID: {id(a)}")

a = 3
print(f"3-qator -> Son: {a}, ID: {id(a)}")

print("-------------------------------------------------")

a = [10]
print(f"1-chi holat -> Qiymat: {a}, ID: {id(a)}")

a[0] = 20
print(f"2-chi holat -> Qiymat: {a}, ID: {id(a)}")

a[0] = 30
print(f"3-chi holat -> Qiymat: {a}, ID: {id(a)}")

print("-------------------------------------------------")

a = {"son": 1}
print(f"1-chi holat -> Qiymat: {a}, ID: {id(a)}")

a["son"] = 2
print(f"2-chi holat -> Qiymat: {a}, ID: {id(a)}")

print("-------------------------------------------------")

class Konteyner:
    def __init__(self, qiymat):
        self.qiymat = qiymat

a = Konteyner(10)
print(f"1. Qiymat: {a.qiymat} | ID: {id(a)}")

a.qiymat = 999
print(f"2. Qiymat: {a.qiymat} | ID: {id(a)}")

a.qiymat = "Endi matn"
print(f"3. Qiymat: {a.qiymat} | ID: {id(a)}")

print("-------------------------------------------------")

