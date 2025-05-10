cmake_minimum_required(VERSION 3.11)

# Set Python version explicitly
set(Python_FIND_VERSION 3.11)
set(Python_FIND_VERSION_MAJOR 3)
set(Python_FIND_VERSION_MINOR 11)

# Force CMake to use the Python from rez
set(Python_ROOT_DIR $ENV{PYTHON_ROOT})
set(Python_FIND_FRAMEWORK NEVER)
set(Python_FIND_REGISTRY NEVER)

project(alembic)

include(ExternalProject)

ExternalProject_Add(alembic
    URL https://github.com/alembic/alembic/archive/refs/tags/1.8.5.zip
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR> 
    -DOPENEXR_BUILD_PYTHON=ON 
    -DUSE_TESTS=OFF 
    -DUSE_HDF5=OFF
    -DALEMBIC_LIB_USES_BOOST=ON
    -DBOOST_ROOT=$ENV{REZ_BOOST_ROOT}
    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/install/ DESTINATION .)