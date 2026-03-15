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
