include_guard(DIRECTORY)

# files
file(
    GLOB
    RAIN_CORE_HEADERS
    ${RAIN_SOURCES_DIR}/*.h
)
file(
    GLOB
    RAIN_CORE_SOURCES
    ${RAIN_SOURCES_DIR}/rain/core/*.cpp
)

# targets
add_library(
    rain_core
    SHARED
        ${RAIN_CORE_HEADERS}
        ${RAIN_CORE_SOURCES}
)
target_include_directories(
    rain_core
    PUBLIC
        ${RAIN_SOURCES_DIR}
)
target_compile_definitions(
    rain_core
    PRIVATE
        -DRAIN_EXPORT
)

# aliases
add_library(
    Rain::core
    ALIAS
        rain_core
)
add_library(
    rain::core
    ALIAS
        rain_core
)

# install
install(
    TARGETS
    rain_core
)
