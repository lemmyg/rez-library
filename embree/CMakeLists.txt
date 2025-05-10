CMAKE_MINIMUM_REQUIRED(VERSION 3.11)
project(embree)

include(ExternalProject)

ExternalProject_add(
    embree
    SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/src
    URL https://github.com/embree/embree/archive/refs/tags/v3.10.0.tar.gz
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR>
    -DCMAKE_BUILD_TYPE=Release
    -DEMBREE_TBB_ROOT=$ENV{REZ_TBB_ROOT}
    -DEMBREE_ISPC_SUPPORT=OFF
    -DEMBREE_TUTORIALS=ON
    BUILD_COMMAND make
    INSTALL_COMMAND make install
    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
)

# copy libs to install directory
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/install/ DESTINATION .)


# copy source code to install directory. required for tximista renderer.
install(
    DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/src
    DESTINATION .
)
