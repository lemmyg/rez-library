CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

include(RezBuild)
include(ExternalProject)


ExternalProject_add(
    python
    URL https://www.python.org/ftp/python/3.11.11/Python-3.11.11.tgz
    SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/src
    CONFIGURE_COMMAND ./configure 
    --prefix=${CMAKE_INSTALL_PREFIX} 
    --enable-shared
    --enable-optimizations
    --disable-test-modules
    BUILD_IN_SOURCE 1
    BUILD_COMMAND make
    INSTALL_COMMAND make install
)

install(CODE "message(STATUS \"Python installed via ExternalProject\")")




