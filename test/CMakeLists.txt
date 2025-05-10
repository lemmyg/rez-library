CMAKE_MINIMUM_REQUIRED(VERSION 3.11)

include(ExternalProject)

# Set RPATH settings before any ExternalProject_add calls
set(CMAKE_SKIP_BUILD_RPATH FALSE)
set(CMAKE_BUILD_WITH_INSTALL_RPATH TRUE)
set(CMAKE_INSTALL_RPATH "@executable_path")
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

find_package(Python3 REQUIRED COMPONENTS Interpreter)

ExternalProject_add(
    test
    SOURCE_DIR "${CMAKE_SOURCE_DIR}/src" 
    CMAKE_ARGS 
    -DCMAKE_INSTALL_PREFIX=${CMAKE_CURRENT_BINARY_DIR}/install
    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
)

#ExternalProject_add(
#    moduleBinding
#    SOURCE_DIR "${CMAKE_SOURCE_DIR}/src/moduleBinding" 
#    CMAKE_ARGS 
#    -DCMAKE_INSTALL_PREFIX=${CMAKE_CURRENT_BINARY_DIR}/install
#    -Dpython_interpreter=${Python3_EXECUTABLE}
#    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
#)

ExternalProject_add(
    widgetBinding
    SOURCE_DIR "${CMAKE_SOURCE_DIR}/src/widgetbinding" 
    CMAKE_ARGS
    -DCMAKE_INSTALL_PREFIX=${CMAKE_CURRENT_BINARY_DIR}/install
    -Dpython_interpreter=${Python3_EXECUTABLE}
    -DCMAKE_SKIP_BUILD_RPATH=FALSE
    -DCMAKE_BUILD_WITH_INSTALL_RPATH=TRUE
    -DCMAKE_INSTALL_RPATH="@executable_path"
    -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=TRUE
    INSTALL_DIR ${CMAKE_CURRENT_BINARY_DIR}/install
)

install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/install/ DESTINATION .)

install(DIRECTORY ${CMAKE_SOURCE_DIR}/src/widgetbinding/ DESTINATION bin)