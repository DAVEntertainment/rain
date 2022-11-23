# set include dir
get_filename_component(RAIN_REPO_DIR ${CMAKE_CURRENT_LIST_DIR}/../../.. ABSOLUTE)
set(RAIN_SRCS_DIR ${RAIN_REPO_DIR}/srcs)
set(RAIN_PUBLIC_HEADER_DIR ${RAIN_REPO_DIR}/include)

# set sources
set(RAIN_MISC_HEADERS
    ${CMAKE_CURRENT_LIST_DIR}/string_utils.h
)

set(RAIN_MISC_SOURCES
    ${CMAKE_CURRENT_LIST_DIR}/string_utils.cpp
)

add_library(rain_misc STATIC
    ${RAIN_MISC_SOURCES}
    ${RAIN_MISC_HEADERS}
)

target_include_directories(rain_misc
    PRIVATE
        ${RAIN_SRCS_DIR}
        ${RAIN_PUBLIC_HEADER_DIR}
)
