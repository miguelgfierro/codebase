# Benchmark on IO performance: http://stackoverflow.com/a/41425878/5620182

import numpy as np


def save_file(data, filename):
    np.save(filename, data) # save the file as "filename.npy"


def read_file(filename):
    data = np.load(filename)
    return data

if __name__ == "__main__":
    a = np.ones(1000)
    save_file(a, 'file')
    b = read_file('file.npy')
    print(a == b)

