#include <pybind11/pybind11.h>
#include "libone/one.h"

namespace py = pybind11;

PYBIND11_MODULE(libone_bindings, m) {
    m.doc() = "Python bindings for libone";

    m.def("find", [](py::function f, double y, long a, long b) {
        auto cpp_func = [&f](long x) -> double {
            py::gil_scoped_acquire gil;
            return f(x).cast<double>();
        };
        return libone::find(cpp_func, y, a, b);
    }, "Find x in [a, b] such that f(x) == y");
}
