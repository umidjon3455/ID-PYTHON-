# 🧠 Python `id()` Function & Memory Management Mechanics

> **Repository:** [umidjon3455/ID-PYTHON-](https://github.com/umidjon3455/ID-PYTHON-)

This repository is dedicated to demonstrating how Python manages memory addresses using the built-in `id()` function. It spans from basic variable references to advanced CPython internals, memory reallocation, and descriptor mechanics.

---

## 📖 Tushuntirish / Explanation (O'zbek tilida)

Python'da har bir yaratilgan qiymat (son, matn, ro'yxat, ob'ekt) **operativ xotirada (RAM)** o'z o'rniga ega bo'ladi. `id()` funksiyasi ushbu ob'ektning xotiradagi **unikal manzilini (pointer)** qaytaradi.

### Asosiy Tushunchalar:
1. **Immutable (O'zgarmas) tiplar (`int`, `str`, `tuple`):**
   - Qiymat o'zgarganda Python xotiradan **yangi joy** ajratadi.
   - Natijada `id()` manzili **o'zgaradi**.

2. **Mutable (O'zgaruvchan) tiplar (`list`, `dict`, `set`):**
   - Ichidagi elementlar o'zgarganda ham ob'ektning o'zi xotiradagi joyini saqlab qoladi.
   - Natijada `id()` manzili **o'zgarmaydi**.

3. **CPython C-API (`ctypes`):**
   - Python ob'ektlari pastki darajada C dilidagi `PyObject` strukturasidir. `ctypes` kutubxonasi orqali to'g'ridan-to'g'ri xotira manzillarini o'qish mumkin.

---

## 🚀 Features & Topics Covered

- 🔹 **Basic `id()` usage:** Line-by-line memory address inspection.
- 🔹 **Mutable vs. Immutable types:** Identity persistence vs. reallocation behavior.
- 🔹 **Custom Classes & Identity:** Keeping a persistent ID across internal attribute mutations.
- 🔹 **CPython Memory Internals:** Low-level pointer inspection using `ctypes`.
- 🔹 **Metaprogramming:** Forcing identity shifts using Python Descriptors and Metaclasses.

---

## 💻 Code Examples / Kod Misollari

### 1. Basic Variable Identity
```python
a = 100
print(f"Value: {a} | Memory ID: {id(a)}")

a = a + 1
print(f"New Value: {a} | New Memory ID: {id(a)}") # ID changes because int is immutable
