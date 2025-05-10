cmake_minimum_required(VERSION 3.11)
project(pybind11)

include(ExternalProject)

set(PYTHON_VERSION_MAJOR 3)
set(PYTHON_VERSION_MINOR 11)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
message(STATUS "Python3_EXECUTABLE: ${Python3_EXECUTABLE}")

ExternalProject_Add(pybind
    URL https://github.com/pybind/pybind11/archive/refs/tags/v2.10.4.tar.gz
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/install/ DESTINATION .)