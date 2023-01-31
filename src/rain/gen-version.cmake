set(RAIN_VERSION_MAJOR 0)
set(RAIN_VERSION_MINOR 0)
set(RAIN_VERSION_PATCH 0)
set(RAIN_VERSION_BUILD 0)
set(RAIN_VERSION_TAG   0)
set(RAIN_VERSION_HASH  0)

find_package(Git REQUIRED)

# get version from git and gitlab
execute_process(
    COMMAND ${GIT_EXECUTABLE} log -1 --pretty=%H
    OUTPUT_VARIABLE RAIN_VERSION_HASH
    WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR}
    OUTPUT_STRIP_TRAILING_WHITESPACE
)

# generate version file
configure_file(
    ${CMAKE_CURRENT_LIST_DIR}/version.def.h.in
    ${CMAKE_CURRENT_LIST_DIR}/version.def.h
    @ONLY
)
