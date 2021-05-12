include_guard(DIRECTORY)

if(${CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT})
    set(
        CMAKE_INSTALL_PREFIX
        ${RAIN_REPO_DIR}/.dist
        CACHE
        PATH
        "rain install prefix"
        FORCE
    )
endif()

set(CMAKE_DEBUG_POSTFIX d)

set(
    CMAKE_CXX_STANDARD 17
    CACHE INTERNAL
    "C++ standard"
    FORCE
)
