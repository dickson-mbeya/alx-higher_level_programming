#include <Python.h>

void print_python_list(PyObject *p) {
    Py_ssize_t size = PyList_Size(p);
    printf("Python List Info:\n");
    printf("Size: %ld\n", size);
    printf("Elements:\n");

    for (Py_ssize_t i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        PyObject *item_str = PyObject_Str(item);
        const char *item_cstr = PyUnicode_AsUTF8(item_str);
        printf("- %s\n", item_cstr);
        Py_XDECREF(item_str);
    }
}

#include <Python.h>

void print_python_bytes_(PyObject *p) {
    Py_ssize_t size = PyBytes_Size(p);
    const char *data = PyBytes_AsString(p);
    printf("Python Bytes Object Info:\n");
    printf("Size: %ld\n", size);
    printf("Data: %s\n", data);
}