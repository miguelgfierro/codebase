import pandas as pd


def save_file(data, filename):
    data.to_csv(filename, index=False, header=False)


def read_file(filename):
    data = pd.read_csv(filename, header=None, names=['time','q1','q2'], sep=',', usecols=[0,1,2])
    return data


if __name__ == "__main__":
    filename = '../../share/traj.csv'

    print("Example of read file")
    data_read = read_file(filename)
    print(data_read)

    filename = 'file.csv'
    print("Example of save file")
    save_file(data_read, filename)