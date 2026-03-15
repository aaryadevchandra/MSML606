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

    