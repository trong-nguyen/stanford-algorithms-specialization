#include <Python.h>
#include <stdexcept>
#include <iostream>
#include <vector>

std::vector<int> pyListToVector(PyObject * object) {
	std::vector<int> vec;
	if(PyList_Check(object)) {
		const int n = PyList_Size(object);
		vec.resize(n);
		for(int i = 0; i < n; ++i) {
			PyObject * value = PyList_GetItem(object, i);
			if(PyInt_Check(value)){
				vec[i] = PyInt_AsLong(value);
			} else {
				throw std::invalid_argument("Not int array\n");
			}
		}
		return vec;
	}else {
		throw std::invalid_argument("Not a pylist\n");
	}
}

PyObject * vectorToPyList(std::vector<int> & vec) {
	PyObject * list = PyList_New(vec.size());
	if(!list) {
		throw std::invalid_argument("Unnable to allow memory to pylist\n");
	}
	for(int i = 0; i < vec.size(); ++i) {
		PyObject * num = PyInt_FromLong((long int)vec[i]);
		if(!num) {
			Py_DECREF(list);
			throw std::invalid_argument("Cannot convert to pyint\n");
		}
		PyList_SET_ITEM(list, i, num);
	}
	return list;
}

int selectPivot(int s, int e) {
	return (s + e) / 2;
}

void swapElements(std::vector<int> & a, int i, int j) {
	int t = a[i];
	a[i] = a[j];
	a[j] = t;
}

int partition(std::vector<int> & a, int s, int e) {
	const int ap = a[selectPivot(s, e)];

	int i = s, j = e;
	while(i <= j){
		while(a[i] < ap) {
			i += 1;
		}
		while(a[j] > ap) {
			j -= 1;
		}
		if(i <= j){
			swapElements(a, i, j);
			i += 1;
			j -= 1;
		}
	}
	return i;
}

void quickSort(std::vector<int> & a, int start, int end) {
	// end is the index of the last element, i.e. range inclusive
	if(start >= end){
		return;
	}
	// for(int i = 0; i < a.size(); ++i) { std::cout << a[i] << " ";}
	const int pivot = partition(a, start, end);
	if(start < pivot-1){
		quickSort(a, start, pivot-1);
	}
	if(pivot < end){
		quickSort(a, pivot, end);
	}
}

static PyObject * quick_sort(PyObject * self, PyObject * args) {
	PyObject * list_obj;
	if(!PyArg_ParseTuple(args, "O!", &PyList_Type, &list_obj)) {
		throw std::invalid_argument("Invalid Python List\n");
	}

	std::vector<int> a = pyListToVector(list_obj);
	quickSort(a, 0, a.size() - 1);
	list_obj = vectorToPyList(a);

	return list_obj;
}

static PyMethodDef Methods[] = {
	{"quick_sort", quick_sort, METH_VARARGS, "Sorting using quick algorithms"},
	{NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initext(void) {
	(void) Py_InitModule("tnt.algorithms.ext", Methods);
}