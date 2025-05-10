cmake_minimum_required(VERSION 3.12)
project(tbb)

include(ExternalProject)

# Set compiler flags
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -Wno-unused-command-line-argument")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-unused-command-line-argument")

# Get system information
if(APPLE)
    set(TBB_PLATFORM "macos")
    set(TBB_ARCH "intel64")
elseif(UNIX)
    set(TBB_PLATFORM "linux")
    set(TBB_ARCH "intel64")
endif()

ExternalProject_Add(tbb
    URL https://github.com/oneapi-src/oneTBB/archive/refs/tags/v2020.3.tar.gz
    DOWNLOAD_DIR ${CMAKE_CURRENT_BINARY_DIR}/downloads
    SOURCE_DIR ${CMAKE_CURRENT_BINARY_DIR}/src
    BUILD_IN_SOURCE 1
    PATCH_COMMAND ""
    CONFIGURE_COMMAND ${CMAKE_COMMAND} -E echo "Configuring TBB..."
    BUILD_COMMAND make -j8
    INSTALL_COMMAND ${CMAKE_COMMAND} -E echo "Installing TBB..."
    UPDATE_COMMAND ""
)

# Find all dylib files in the build directory
file(GLOB TBB_LIBRARIES "${CMAKE_CURRENT_BINARY_DIR}/src/build/*_release/*.dylib")

# Install the built libraries and headers
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/src/include/ DESTINATION include)
install(FILES ${TBB_LIBRARIES} DESTINATION lib)
