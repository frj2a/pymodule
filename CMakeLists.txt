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