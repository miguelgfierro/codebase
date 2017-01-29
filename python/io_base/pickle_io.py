# Benchmark on IO performance: http://stackoverflow.com/a/41425878/5620182

try:
    import cPickle as pickle
except:
    import pickle_io


def save_file(data, filename):
    pickle.dump(data, open(filename, "wb"))


def read_file(filename):
    data = pickle.load(open(filename, "rb"))
    return data


if __name__ == "__main__":
    filename = 'file.pk'
    data = dict({'a':1, 'b':2, 'c':3})
    print("Example of save file")
    save_file(data, filename)

    print("Example of read file")
    data_read = read_file(filename)
    print(data_read)
