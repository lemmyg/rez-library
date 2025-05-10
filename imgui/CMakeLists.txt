CMAKE_MINIMUM_REQUIRED(VERSION 3.11)

project(imgui)

# Download and extract imgui
set(IMGUI_DOWNLOAD_DIR "${CMAKE_CURRENT_SOURCE_DIR}/build")
set(IMGUI_ARCHIVE "${IMGUI_DOWNLOAD_DIR}/imgui-1.74.tar.gz")
if(NOT EXISTS "${IMGUI_DOWNLOAD_DIR}/imgui-1.74")
    execute_process(
        COMMAND curl -L https://github.com/ocornut/imgui/archive/refs/tags/v1.74.tar.gz -o ${IMGUI_ARCHIVE}
        WORKING_DIRECTORY ${IMGUI_DOWNLOAD_DIR}
    )
    
    execute_process(
        COMMAND tar -xzf ${IMGUI_ARCHIVE}
        WORKING_DIRECTORY ${IMGUI_DOWNLOAD_DIR}
    )
endif()

# Add installation targets
install(
    DIRECTORY ${IMGUI_DOWNLOAD_DIR}/imgui-1.74/
    DESTINATION .
)
