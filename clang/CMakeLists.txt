cmake_minimum_required(VERSION 3.11)
project(clang)

# Include ExternalProject module
include(ExternalProject)

ExternalProject_Add(clang
    URL https://download.qt.io/development_releases/prebuilt/libclang/libclang-release_16.0.2-based-macos-universal.7z
    SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/src
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND ""
)

# Install the extracted files to the final install location
install(
    DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/src/
    DESTINATION .
)