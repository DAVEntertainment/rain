cmake_minimum_required(VERSION 3.24)

add_executable(rain_entry
    entry.cpp
)

target_link_libraries(rain_entry
    PRIVATE
        rain
)

set_target_properties(rain_entry
    PROPERTIES
        OUTPUT_NAME rain
)

install(
    TARGETS
        rain_entry
)
