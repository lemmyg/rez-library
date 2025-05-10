cmake_minimum_required(VERSION 3.11)
project(openexr)

include(ExternalProject)
find_package(Pybind11 REQUIRED)

ExternalProject_Add(openexr
    URL https://github.com/AcademySoftwareFoundation/openexr/releases/download/v3.3.3/openexr-3.3.3.tar.gz
    SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/src
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR> -DOPENEXR_BUILD_PYTHON=ON
    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/install/ DESTINATION .)