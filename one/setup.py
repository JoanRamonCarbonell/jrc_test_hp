from setuptools import setup, Extension
import sys
import os

# Determine the path where CMake will place the shared object file
build_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'build')

# Ensure the path to libone_bindings.so or libone_bindings.pyd is correct based on your platform
module_name = 'libone_bindings'
library_path = os.path.join(build_dir, 'lib' + module_name + '.so')  # Adjust if necessary (e.g., for Windows: .pyd)

# Setup
setup(
    name=module_name,
    ext_modules=[
        Extension(
            module_name,
            [library_path],  # Path to the shared library
            libraries=[module_name],  # Link against the library (libone_bindings)
            library_dirs=[build_dir],  # Make sure to link against the shared library
        )
    ],
    zip_safe=False
)
