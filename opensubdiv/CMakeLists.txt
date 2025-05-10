CMAKE_MINIMUM_REQUIRED(VERSION 3.11)

include(RezBuild)
include(ExternalProject)

ExternalProject_add(
    opensubdiv
    URL https://github.com/PixarAnimationStudios/OpenSubdiv/archive/v3_1_1.tar.gz
    PREFIX opensubdiv
    CMAKE_ARGS -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
    -DNO_EXAMPLES=OFF
    -DNO_TUTORIALS=OFF
    -DNO_DOC=ON
    -DNO_OMP=ON
    -DNO_DX=ON
    -DNO_TESTS=OFF
    -DNO_CUDA=OFF
    -DNO_OPENCL=ON
    -DNO_GLEW=OFF
    -DNO_GLFW=ON
    -DNO_TBB=ON
    #-DTBB_LOCATION=$ENV{REZ_TBB_ROOT}
    #INSTALL_COMMAND ${CMAKE_COMMAND}
    # ALWAYS 1
)

# Add an empty install target to satisfy rez build system
install(CODE "message(STATUS \"OpenSubdiv installed via ExternalProject\")")


