/*
// Original Python/C API implementation
#include <Python.h>
#include <structmember.h>

// SumCalculator class definition
typedef struct {
    PyObject_HEAD
} SumCalculatorObject;

// SumCalculator methods
static PyObject* SumCalculator_sum_to_n(SumCalculatorObject* self, PyObject* args) {
    int n;
    if (!PyArg_ParseTuple(args, "i", &n)) {
        return NULL;
    }
    
    if (n < 0) {
        PyErr_SetString(PyExc_ValueError, "Parameter must be non-negative");
        return NULL;
    }
    
    long long sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    return PyLong_FromLongLong(sum);
}

// SumCalculator method definitions
static PyMethodDef SumCalculator_methods[] = {
    {"sum_to_n", (PyCFunction)SumCalculator_sum_to_n, METH_VARARGS, "Sum all integers from 1 to n"},
    {NULL}  // Sentinel
};

// SumCalculator type slots
static PyType_Slot sumcalculator_slots[] = {
    {Py_tp_methods, SumCalculator_methods},
    {Py_tp_doc, (void*)"SumCalculator object"},
    {Py_tp_new, (void*)PyType_GenericNew},
    {0, NULL}
};

// SumCalculator type specification
static PyType_Spec sumcalculator_spec = {
    "pymodule.SumCalculator",        // name
    sizeof(SumCalculatorObject),     // basicsize
    0,                               // itemsize
    Py_TPFLAGS_DEFAULT,              // flags
    sumcalculator_slots              // slots
};

// Module method definitions
static PyMethodDef ModuleMethods[] = {
    {NULL, NULL, 0, NULL}  // Sentinel
};

// Module definition
static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "pymodule",  // name of module
    "A module that provides summation calculations",  // module documentation
    -1,  // size of per-interpreter state or -1
    ModuleMethods
};

// Module initialization function
PyMODINIT_FUNC PyInit_pymodule(void) {
    PyObject* m;
    
    m = PyModule_Create(&moduledef);
    if (m == NULL)
        return NULL;

    PyObject* sumcalculator_type = PyType_FromSpec(&sumcalculator_spec);
    if (sumcalculator_type == NULL) {
        Py_DECREF(m);
        return NULL;
    }

    if (PyModule_AddObject(m, "SumCalculator", sumcalculator_type) < 0) {
        Py_DECREF(sumcalculator_type);
        Py_DECREF(m);
        return NULL;
    }

    return m;
}
*/

// Boost.Python implementation




#include <boost/python.hpp>
#include <thread>
#include <vector>
#include <numeric>

class TestCalculator {
public:
    long long sumToN(int n) {
        if (n < 0) {
            PyErr_SetString(PyExc_ValueError, "Parameter must be non-negative");
            boost::python::throw_error_already_set();
        }
        
        long long sum = 0;
        for (int i = 1; i <= n; i++) {
            sum += i;
        }
        return sum;
    }

    long long multiplyToN(int n) {
        if (n < 0) {
            PyErr_SetString(PyExc_ValueError, "Parameter must be non-negative");
            boost::python::throw_error_already_set();
        }
        
        if (n == 0) return 0;
        
        long long result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    long long sumToNThreaded(int n, int num_threads = std::thread::hardware_concurrency()) {
        if (n < 0) {
            PyErr_SetString(PyExc_ValueError, "Parameter must be non-negative");
            boost::python::throw_error_already_set();
        }

        if (n == 0) return 0;

        if (n < num_threads) {
            num_threads = n;
        }
        
        std::vector<std::thread> threads;
        std::vector<long long> partial_sums(num_threads);
        
        int chunk_size = n / num_threads;
        
        for (int i = 0; i < num_threads; ++i) {
            int start = i * chunk_size + 1;
            int end = (i == num_threads - 1) ? n : (i + 1) * chunk_size;
            
            threads.emplace_back([start, end, &partial_sums, i]() {
                long long sum = 0;
                for (int j = start; j <= end; ++j) {
                    sum += j;
                }
                partial_sums[i] = sum;
            });
        }
        
        for (auto& thread : threads) {
            thread.join();
        }
        
        return std::accumulate(partial_sums.begin(), partial_sums.end(), 0LL);
    }

    long long multiplyToNThreaded(int n, int num_threads = std::thread::hardware_concurrency()) {
        if (n < 0) {
            PyErr_SetString(PyExc_ValueError, "Parameter must be non-negative");
            boost::python::throw_error_already_set();
        }
        
        if (n == 0) return 0;
        if (n == 1) return 1;

        if (n < num_threads) {
            num_threads = n;
        }
        
        std::vector<std::thread> threads;
        std::vector<long long> partial_products(num_threads);
        
        int chunk_size = n / num_threads;
        
        for (int i = 0; i < num_threads; ++i) {
            int start = i * chunk_size + 1;
            int end = (i == num_threads - 1) ? n : (i + 1) * chunk_size;
            
            threads.emplace_back([start, end, &partial_products, i]() {
                long long product = 1;
                for (int j = start; j <= end; ++j) {
                    product *= j;
                }
                partial_products[i] = product;
            });
        }
        
        for (auto& thread : threads) {
            thread.join();
        }
        
        return std::accumulate(partial_products.begin(), partial_products.end(), 1LL, 
                             std::multiplies<long long>());
    }
};

BOOST_PYTHON_MODULE(pymodule)
{
    using namespace boost::python;
    
    class_<TestCalculator>("TestCalculator")
        .def("sum_to_n", &TestCalculator::sumToN, "Sum all integers from 1 to n")
        .def("multiply_to_n", &TestCalculator::multiplyToN, "Multiply all integers from 1 to n")
        .def("sum_to_n_threaded", &TestCalculator::sumToNThreaded, 
             (arg("n"), arg("num_threads") = std::thread::hardware_concurrency()),
             "Sum all integers from 1 to n using multiple threads")
        .def("multiply_to_n_threaded", &TestCalculator::multiplyToNThreaded,
             (arg("n"), arg("num_threads") = std::thread::hardware_concurrency()),
             "Multiply all integers from 1 to n using multiple threads");
}
