CMAKE_MINIMUM_REQUIRED(VERSION 3.11)
project(openSubdiv)
include(ExternalProject)

ExternalProject_add(
    openSubdiv
    URL https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v3_6_0.tar.gz
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DNO_EXAMPLES=1
    -DNO_TUTORIALS=1
    -DNO_DOC=ON
    -DNO_OMP=ON
    -DNO_DX=ON
    -DNO_TESTS=1
    -DNO_CUDA=1
    -DNO_OPENCL=1
    -DNO_GLEW=OFF
    -DNO_GLFW=ON
    -DNO_TBB=ON
    #-DTBB_LOCATION=$ENV{REZ_TBB_ROOT}
    #INSTALL_COMMAND ${CMAKE_COMMAND}
    # ALWAYS 1
)

# Add an empty install target to satisfy rez build system
install(CODE "message(STATUS \"OpenSubdiv installed via ExternalProject\")")


