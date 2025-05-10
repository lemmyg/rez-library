CMAKE_MINIMUM_REQUIRED(VERSION 3.11)

include(RezBuild)
include(ExternalProject)

ExternalProject_add(
    glew
    URL https://downloads.sourceforge.net/project/glew/glew/2.1.0/glew-2.1.0.tgz
    PREFIX glew
    PATCH_COMMAND ""
    CONFIGURE_COMMAND ""
    BUILD_COMMAND ""
    INSTALL_COMMAND make install GLEW_DEST="${CMAKE_INSTALL_PREFIX}"
    ALWAYS 1
    BUILD_IN_SOURCE 1
)


# Add an empty install target to satisfy rez build system
install(CODE "message(STATUS \"Glew installed via ExternalProject\")")