include_guard(DIRECTORY)

# targets
add_executable(
    rain
        ${RAIN_SOURCES_DIR}/entry/main.cpp
)
target_link_libraries(
    rain
    PRIVATE
        rain::core
)

# aliases
add_executable(
    rain::rain
    ALIAS
        rain
)

# install
install(
    TARGETS
    rain
)
