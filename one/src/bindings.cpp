#include <pybind11/pybind11.h>
#include "libone/one.h"

namespace py = pybind11;

PYBIND11_MODULE(libone_bindings, m) {
    m.doc() = "Python bindings for libone";

    // Expose square separately
    m.def("square", &libone::square, "C++ square function");

    m.def("find", [](double y, long a, long b) {
        return libone::find(&libone::square, y, a, b);
    }, "Find x such that f(x) == y in range [a, b], f(x) being a square()");
}
