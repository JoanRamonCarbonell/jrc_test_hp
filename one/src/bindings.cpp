#include <pybind11/pybind11.h>
#include "one.h"

namespace py = pybind11;

PYBIND11_MODULE(libone_bindings, m) {
    m.doc() = "Python bindings for libone";

    // Expose square separately
    m.def("square", &libone::square, "C++ square function");

    // m.def("find", [](double y, long a, long b) {
    //     return libone::find(&libone::square, y, a, b);
    // }, "Find x such that f(x) == y in range [a, b], f(x) being a square()");
    m.def("find", [](py::function py_f, double y, long a, long b) -> long {
        py::gil_scoped_acquire gil; // Ensure Python GIL is held

        // Direct lambda matching the signature double(long)
        auto f = [&py_f](long x) -> double {
            return py_f(x).cast<double>();
        };

        return find(f, y, a, b);
}
