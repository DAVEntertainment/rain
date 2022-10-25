
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
