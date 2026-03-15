import random
import time
import matplotlib.pyplot as plt


class HashTable:
    def __init__(self, size, method="division"):
        self.size = size
        self.method = method
        self.data = []
        for i in range(size):
            self.data.append([])

    def key_to_num(self, key):
        if type(key) == int:
            return abs(key)
        elif type(key) == float:
            return abs(int(key * 1000))
        else:
            str1 = str(key)
            total = 0
            for i in range(len(str1)):
                total = total + ord(str1[i])
            return abs(total)

    def hash_division(self, key):
        x = self.key_to_num(key)
        return x % self.size

    def hash_multiplication(self, key):
        x = self.key_to_num(key)
        a = 0.56487389
        temp = x * a
        temp = temp - int(temp)
        return int(self.size * temp)

    def get_index(self, key):
        if self.method == "division":
            return self.hash_division(key)
        else:
            return self.hash_multiplication(key)

    def insert(self, key, value):
        idx = self.get_index(key)

        for i in range(len(self.data[idx])):
            if self.data[idx][i][0] == key:
                self.data[idx][i] = (key, value)
                return

        self.data[idx].append((key, value))

    def search(self, key):
        idx = self.get_index(key)

        for i in range(len(self.data[idx])):
            if self.data[idx][i][0] == key:
                return self.data[idx][i][1]

        return None

    def delete(self, key):
        idx = self.get_index(key)

        for i in range(len(self.data[idx])):
            if self.data[idx][i][0] == key:
                del self.data[idx][i]
                return True

        return False

    def count_items(self):
        total = 0
        for i in range(len(self.data)):
            total = total + len(self.data[i])
        return total

    def get_load_factor(self):
        return self.count_items() / self.size

    def average_chain_length(self):
        total = 0
        for i in range(len(self.data)):
            total = total + len(self.data[i])
        return total / self.size

    def max_chain_length(self):
        m = 0
        for i in range(len(self.data)):
            if len(self.data[i]) > m:
                m = len(self.data[i])
        return m

print("PROBLEM 1")
print()

x = HashTable(10, "division")

x.insert("apple", 10)
x.insert("banana", 20)
x.insert("orange", 30)

print("apple =", x.search("apple"))
print("banana =", x.search("banana"))
print("orange =", x.search("orange"))
print("grape =", x.search("grape"))
print()

x.insert("apple", 99)
print("apple after update =", x.search("apple"))
print()

print("delete banana =", x.delete("banana"))
print("banana now =", x.search("banana"))
print("delete grape =", x.delete("grape"))
print()

print("load factor =", x.get_load_factor())
print("avg chain length =", x.average_chain_length())
print("max chain length =", x.max_chain_length())
print()


table_sizes = [101, 503, 1009]
load_factors = [0.25, 0.50, 0.75, 1.00, 1.25, 1.50]

all_success = {}
all_unsuccess = {}

for s in table_sizes:
    success_times = []
    unsuccess_times = []

    for lf in load_factors:
        num_items = int(s * lf)

        keys = []
        for i in range(num_items):
            keys.append(random.randint(0, 1000000))

        h = HashTable(s, "division")

        for i in range(len(keys)):
            h.insert(keys[i], "val" + str(keys[i]))

        total1 = 0.0
        for i in range(1000):
            key = random.choice(keys)
            start = time.perf_counter()
            h.search(key)
            end = time.perf_counter()
            total1 = total1 + (end - start)

        avg1 = total1 / 1000

        key_set = set(keys)
        total2 = 0.0
        count = 0
        while count < 1000:
            key = random.randint(1000001, 3000000)
            if key not in key_set:
                start = time.perf_counter()
                h.search(key)
                end = time.perf_counter()
                total2 = total2 + (end - start)
                count = count + 1

        avg2 = total2 / 1000

        success_times.append(avg1)
        unsuccess_times.append(avg2)

        print("size", s, "load factor", lf)
        print("successful", avg1)
        print("unsuccessful", avg2)
        print("avg chain", h.average_chain_length())
        print("max chain", h.max_chain_length())
        print()

    all_success[s] = success_times
    all_unsuccess[s] = unsuccess_times

plt.figure(figsize=(8, 5))
for s in table_sizes:
    plt.plot(load_factors, all_success[s], marker="o", label="size=" + str(s))
plt.xlabel("Load Factor")
plt.ylabel("Average Successful Search Time")
plt.title("Load Factor vs Successful Search Time")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
for s in table_sizes:
    plt.plot(load_factors, all_unsuccess[s], marker="o", label="size=" + str(s))
plt.xlabel("Load Factor")
plt.ylabel("Average Unsuccessful Search Time")
plt.title("Load Factor vs Unsuccessful Search Time")
plt.legend()
plt.grid(True)
plt.show()


names = ["Uniform", "Skewed", "Sequential"]
success_result = []
unsuccess_result = []
avg_chain_result = []
max_chain_result = []

table_size = 1009
num_items = table_size

for z in range(3):
    keys = []

    if z == 0:
        for i in range(num_items):
            keys.append(random.randint(0, 1000000))

    elif z == 1:
        for i in range(num_items):
            r = random.random()
            keys.append(int((r ** 3) * 1000000))

    else:
        for i in range(num_items):
            keys.append(i)

    h = HashTable(table_size, "multiplication")

    for i in range(len(keys)):
        h.insert(keys[i], "val" + str(keys[i]))

    total1 = 0.0
    for i in range(1000):
        key = random.choice(keys)
        start = time.perf_counter()
        h.search(key)
        end = time.perf_counter()
        total1 = total1 + (end - start)

    avg1 = total1 / 1000

    key_set = set(keys)
    total2 = 0.0
    count = 0
    while count < 1000:
        key = random.randint(1000001, 3000000)
        if key not in key_set:
            start = time.perf_counter()
            h.search(key)
            end = time.perf_counter()
            total2 = total2 + (end - start)
            count = count + 1

    avg2 = total2 / 1000

    success_result.append(avg1)
    unsuccess_result.append(avg2)
    avg_chain_result.append(h.average_chain_length())
    max_chain_result.append(h.max_chain_length())

    print(names[z])
    print("successful", avg1)
    print("unsuccessful", avg2)
    print("avg chain", h.average_chain_length())
    print("max chain", h.max_chain_length())
    print()


plt.figure(figsize=(8, 5))
plt.bar(names, success_result)
plt.xlabel("Key Distribution")
plt.ylabel("Average Successful Search Time")
plt.title("Successful Search Time by Distribution")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(names, unsuccess_result)
plt.xlabel("Key Distribution")
plt.ylabel("Average Unsuccessful Search Time")
plt.title("Unsuccessful Search Time by Distribution")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(names, avg_chain_result)
plt.xlabel("Key Distribution")
plt.ylabel("Average Chain Length")
plt.title("Average Chain Length by Distribution")
plt.show()

plt.figure(figsize=(8, 5))
plt.bar(names, max_chain_result)
plt.xlabel("Key Distribution")
plt.ylabel("Maximum Chain Length")
plt.title("Maximum Chain Length by Distribution")
plt.show()