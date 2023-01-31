
# set include dir
get_filename_component(RAIN_REPO_DIR ${CMAKE_CURRENT_LIST_DIR}/../../.. ABSOLUTE)
set(RAIN_SRCS_DIR ${RAIN_REPO_DIR}/srs)
set(RAIN_PUBLIC_HEADER_DIR ${RAIN_REPO_DIR}/include)

# set sources
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
    PRIVATE
        ${RAIN_SRCS_DIR}
        ${RAIN_PUBLIC_HEADER_DIR}
)
