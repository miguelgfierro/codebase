

def find_item_index(py_list, item):
    return py_list.index(item)


def get_n_first_elements(py_list, n_elements):
    return py_list[:n_elements]


def get_n_last_elements(py_list, n_elements):
    return py_list[-n_elements:]


def generate_random_numbers(min, max, number_values):
    import random
    r = random.sample(range(min, max), number_values)
    return r

if __name__ == "__main__":

    # Example of finding item index in list
    py_list = ["foo", "bar", "baz"]
    item = "bar"
    idx = find_item_index(py_list, item)
    print("Index: %d" % idx)

    # Example of getting first and last elements
    py_list = [1,2,3,4,5,6,7,8]
    py_list_first = get_n_first_elements(py_list, 2)
    py_list_last = get_n_last_elements(py_list, 2)
    print("First elements: {0}; last elements: {1}".format(py_list_first, py_list_last))