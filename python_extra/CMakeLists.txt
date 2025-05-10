cmake_minimum_required(VERSION 3.11)
project(python_extra)
include(RezBuild)
include(ExternalProject)
# Find Python
#find_package(Python REQUIRED COMPONENTS Interpreter)
find_program(PYTHON ${PYTHON_VERSION})
find_program(PIP3 pip3.11)

# Check if pip3 was found
if(NOT PIP3)
    message(FATAL_ERROR "pip3.11 not found. Please ensure it is installed and in your PATH")
endif()

# Execute pip install
message(STATUS "PIP3: ${PIP3}")
execute_process(
    COMMAND ${PIP3} install PySide6==6.5.3 --force-reinstall
    RESULT_VARIABLE pip_result
)

execute_process(
    COMMAND ${Python_EXECUTABLE} -m pip install --index-url=https://download.qt.io/official_releases/QtForPython/ --trusted-host download.qt.io shiboken6_generator==6.5.3 --force-reinstall
    RESULT_VARIABLE pip_result
)

execute_process(
    COMMAND ${PIP3} install setuptools wheel numpy==1.26.4 Qt.py packaging QDarkStyle PyOpenGL PyYAML setproctitle ninja2 virtualenv  --force-reinstall
    RESULT_VARIABLE pip_result
)

if(NOT pip_result EQUAL 0)
    message(FATAL_ERROR "pip install failed with result: ${pip_result}")
endif()

# Add an empty install target to satisfy rez build system
install(CODE "message(STATUS \"PySide6 installed via pip\")")