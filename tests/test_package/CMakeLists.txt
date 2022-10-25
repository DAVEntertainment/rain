cmake_minimum_required(VERSION 3.24)

# find_package(Rain CONFIG REQUIRED COMPONENTS rain)
find_package(Rain CONFIG REQUIRED)

add_executable(test_package
    test.cpp
)

target_link_libraries(test_package
    PRIVATE
        Rain::rain
)

install(
    TARGETS
        test_package
)
