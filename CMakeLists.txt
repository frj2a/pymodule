cmake_minimum_required(VERSION 3.10)
project(pymodule)

# Find Python
find_package(Python3 COMPONENTS Interpreter Development REQUIRED)

# Find Boost with Python component
find_package(Boost COMPONENTS python REQUIRED)

# Add the module
add_library(pymodule MODULE src/module.cpp)

# Set the output name to match Python's requirements
set_target_properties(pymodule PROPERTIES PREFIX "")

# Include Python and Boost headers
target_include_directories(pymodule PRIVATE 
    ${Python3_INCLUDE_DIRS}
    ${Boost_INCLUDE_DIRS}
)

# Link against Python and Boost libraries
target_link_libraries(pymodule PRIVATE 
    ${Python3_LIBRARIES}
    ${Boost_LIBRARIES}
)

# Get Python site-packages directory for installation
execute_process(
    COMMAND ${Python3_EXECUTABLE} -c "import site; print(site.getsitepackages()[0])"
    OUTPUT_VARIABLE PYTHON_SITE_PACKAGES
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

# Installation rules
install(TARGETS pymodule
    LIBRARY DESTINATION ${PYTHON_SITE_PACKAGES}
)

# Add uninstall target
if(NOT TARGET uninstall)
    configure_file(
        "${CMAKE_CURRENT_SOURCE_DIR}/cmake/cmake_uninstall.cmake.in"
        "${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake"
        IMMEDIATE @ONLY)

    add_custom_target(uninstall
        COMMAND ${CMAKE_COMMAND} -P ${CMAKE_CURRENT_BINARY_DIR}/cmake_uninstall.cmake)
endif()