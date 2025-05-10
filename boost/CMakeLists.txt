cmake_minimum_required(VERSION 3.12)
project(boost)
include(RezBuild)
include(ExternalProject)


# Configure user-config.jam
configure_file(
    ${CMAKE_CURRENT_SOURCE_DIR}/user-config.jam.in
    ${CMAKE_CURRENT_SOURCE_DIR}/user-config.jam
    @ONLY
)

ExternalProject_Add(boost
    URL https://sourceforge.net/projects/boost/files/boost/1.82.0/boost_1_82_0.tar.gz
    CONFIGURE_COMMAND ./bootstrap.sh --prefix=<INSTALL_DIR> 
    BUILD_COMMAND ./b2 install
        --prefix=<INSTALL_DIR>
        -j16
        address-model=64
        link=shared  
        runtime-link=shared
        threading=multi
        variant=release
        cxxstd=17
        --with-atomic
        --with-regex
        --with-python
        --with-thread
        --with-filesystem
        --with-program_options
        --with-serialization
        --with-test
        --user-config=${CMAKE_CURRENT_SOURCE_DIR}/user-config.jam
    BUILD_IN_SOURCE 1
    INSTALL_COMMAND ""
    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/install/include/boost DESTINATION include)
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/install/lib/ DESTINATION lib)

rez_install_files(
    cmake/
    DESTINATION .
)
