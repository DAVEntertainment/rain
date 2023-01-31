
# set include dir
get_filename_component(RAIN_REPO_DIR ${CMAKE_CURRENT_LIST_DIR}/../../.. ABSOLUTE)
set(RAIN_SRCS_DIR ${RAIN_REPO_DIR}/src)
set(RAIN_PUBLIC_HEADER_DIR ${RAIN_REPO_DIR}/include)

# set sources
set(RAIN_CORE_HEADERS
    ${CMAKE_CURRENT_LIST_DIR}/console.h
    ${CMAKE_CURRENT_LIST_DIR}/interpreter.h
)

set(RAIN_CORE_SOURCES
    ${CMAKE_CURRENT_LIST_DIR}/console.cpp
    ${CMAKE_CURRENT_LIST_DIR}/interpreter.cpp
)

add_library(rain_core STATIC
    ${RAIN_CORE_SOURCES}
    ${RAIN_CORE_HEADERS}
)

target_link_libraries(rain_core
    PRIVATE
        rain_logger
        rain_misc
)

target_include_directories(rain_core
    PRIVATE
        ${RAIN_SRCS_DIR}
        ${RAIN_PUBLIC_HEADER_DIR}
)
