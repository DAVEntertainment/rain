
set(RAIN_MISC_HEADERS
    ${CMAKE_CURRENT_LIST_DIR}/rain_macros.h
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
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/../..
)
