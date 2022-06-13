#include <Python.h>

static PyObject* rect_rect(PyObject* self, PyObject* args)
{
	int width{}, bottom{}, top{}, left{}, right{}, i{}, height{};

	if (!PyArg_ParseTuple(args, "iiii", &width, &bottom, &i, &height))
		return NULL;

	top = bottom - height;
	left = i * width;
	right = (i + 1) * width;

	return Py_BuildValue("iii", top, left, right);
}

static PyMethodDef RectMethods[] = {
	{"rect", rect_rect, METH_VARARGS, "top, left, right return"},
	{NULL, NULL, 0, NULL}
};

static PyModuleDef rectmodule = {
	PyModuleDef_HEAD_INIT,
	"rect",
	"Make Rect Module.",
	-1, RectMethods
};

PyMODINIT_FUNC PyInit_rect(void)
{
	return PyModule_Create(&rectmodule);
}