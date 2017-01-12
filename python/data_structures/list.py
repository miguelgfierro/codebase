
def find_item_index_in_list(py_list, item):
	return py_list.index(item)


if __name__ == "__main__":

	#Example of finding item index in list 
	py_list = ["foo", "bar", "baz"]
	item = "bar"
	idx = find_item_index_in_list(py_list, item)
	print(idx)
