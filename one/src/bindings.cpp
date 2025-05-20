#include <pybind11/pybind11.h>
#include "libone/one.h"

namespace py = pybind11;

PYBIND11_MODULE(libone_bindings, m) {
    m.doc() = "Python bindings for libone";

    m.def("find_square", &libone::find_square,
    "Find x such that f(x) == y in [a, b], assuming f is increasing",
    py::arg("y"), py::arg("a"), py::arg("b"));
}
