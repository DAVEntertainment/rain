
set(RAIN_LOGGER_HEADERS
    ${CMAKE_CURRENT_LIST_DIR}/logger.h
)

set(RAIN_LOGGER_SOURCES
    ${CMAKE_CURRENT_LIST_DIR}/logger.cpp
)

add_library(rain_logger STATIC
    ${RAIN_LOGGER_SOURCES}
    ${RAIN_LOGGER_HEADERS}
)

target_include_directories(rain_logger
    PUBLIC
        ${CMAKE_CURRENT_LIST_DIR}/../..
)
