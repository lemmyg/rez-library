cmake_minimum_required(VERSION 3.11)
project(glm)

include(ExternalProject)

ExternalProject_Add(
    glm
    URL https://github.com/g-truc/glm/archive/refs/tags/1.0.1.tar.gz
    SOURCE_DIR src
    CMAKE_ARGS
        #-B ./build
        -DCMAKE_INSTALL_PREFIX=<INSTALL_DIR> 
        -DBUILD_SHARED_LIBS=ON

    BUILD_COMMAND cmake --build . --parallel 16
    INSTALL_COMMAND cmake --install . --parallel 16
    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
    BUILD_IN_SOURCE 1
)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/install/ DESTINATION .) 