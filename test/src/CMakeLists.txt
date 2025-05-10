CMAKE_MINIMUM_REQUIRED(VERSION 3.11)

project(test)

set(CMAKE_BUILD_TYPE Release)

set(CMAKE_VERBOSE_MAKEFILE ON)
# Set CPP standard to C++ minimum.
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
#set(CMAKE_CXX_FLAGS "-Wno-deprecated -Wno-return-type ${CMAKE_CXX_FLAGS}")

set(BUILD_SHARED_LIBS ON)
# 2.Configuration
#add_compile_options(-Wno-deprecated)
set(CMAKE_EXPORT_COMPILE_COMMANDS ON) 

set(CMAKE_MODULE_PATH $ENV{CMAKE_MODULE_PATH})

# Find required packages
find_package(OpenImageIO REQUIRED)
find_package(TBB REQUIRED)

message(STATUS "Found OpenImageIO version: ${OpenImageIO_VERSION}")
message(STATUS "OpenImageIO include dirs: ${OpenImageIO_INCLUDES}")
message(STATUS "OpenImageIO libraries: ${OpenImageIO_LIBRARIES}")

# OpenImageIO test
add_executable(test main.cpp)
target_include_directories(test PRIVATE ${OpenImageIO_INCLUDES})
target_link_libraries(test PRIVATE OpenImageIO::OpenImageIO)

# USD test
find_package(pxr REQUIRED)
message(STATUS "Found USD version: ${PXR_VERSION}")
message(STATUS "USD include dirs: ${PXR_INCLUDE_DIRS}")
message(STATUS "USD libraries: ${PXR_LIBRARIES}")
add_executable(usd_test usd.cpp)
target_include_directories(usd_test PRIVATE 
    ${OpenImageIO_INCLUDES}
    ${PXR_INCLUDE_DIRS}
    ${TBB_INCLUDE_DIRS}
)
target_link_libraries(usd_test PRIVATE 
    OpenImageIO::OpenImageIO
    ${PXR_LIBRARIES}
    TBB::tbb
)

# Install targets
install(TARGETS test usd_test RUNTIME DESTINATION bin)
