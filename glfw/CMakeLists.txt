CMAKE_MINIMUM_REQUIRED(VERSION 3.11)

include(RezBuild)
include(ExternalProject)

ExternalProject_add(
    glfw
    URL https://github.com/glfw/glfw/archive/3.3.8.tar.gz
    PREFIX glfw
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DGLFW_BUILD_TESTS=OFF
    -DGLFW_BUILD_EXAMPLES=OFF
    -DGLFW_BUILD_DOCS=OFF
    -DBUILD_SHARED_LIBS=ON
    -DCMAKE_BUILD_TYPE=Release
)



# Add an empty install target to satisfy rez build system
install(CODE "message(STATUS \"Glfw installed via ExternalProject\")")