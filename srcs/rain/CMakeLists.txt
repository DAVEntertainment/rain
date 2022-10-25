cmake_minimum_required(VERSION 3.24)

add_subdirectory(core)
add_subdirectory(logger)
add_subdirectory(misc)

set(RAIN_HEADERS
    api_macro.h
    factory.h
    rain.h
)

set(RAIN_SOURCES
    factory.cpp
)

add_library(rain SHARED
    ${RAIN_SOURCES}
    ${RAIN_HEADERS}
)

target_link_libraries(rain
    PRIVATE
        rain_core
)

target_include_directories(rain
    PRIVATE
        ${CMAKE_CURRENT_LIST_DIR}/..
)

target_include_directories(rain SYSTEM INTERFACE
    "$<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/..>"
    "$<INSTALL_INTERFACE:$<INSTALL_PREFIX>/include>"
)

target_compile_definitions(rain
    PRIVATE
        -DRAIN_EXPORT
)

set_target_properties(rain
    PROPERTIES
        PUBLIC_HEADER "${RAIN_HEADERS}"
)

install(
    TARGETS rain
    EXPORT rain
    RUNTIME DESTINATION bin
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    PUBLIC_HEADER DESTINATION include/rain
)

# install <TARGET>Targets*.cmake files
install(
    EXPORT rain
    FILE rainTargets.cmake
    NAMESPACE Rain:: # Defines namespace in XXXTargets.cmake
    DESTINATION lib/cmake/rain
)

# CMakePackageConfigHelpers provides
#   write_basic_package_version_file
#   configure_package_config_file
include(CMakePackageConfigHelpers)

# generate <TARGET>ConfigVersion.cmake file
write_basic_package_version_file(
    rainConfigVersion.cmake
    VERSION 1.0.0
    COMPATIBILITY SameMajorVersion # AnyNewerVersion|SameMajorVersion|SameMinorVersion|ExactVersion
)

# generate <TARGET>Config.cmake file
configure_package_config_file(
    rain.package.cmake.in rainConfig.cmake
    INSTALL_DESTINATION  lib/cmake/rain
)

# install <TARGET>Config.cmake and <TARGET>ConfigVersion.cmake file
install(
    FILES
        ${CMAKE_CURRENT_BINARY_DIR}/rainConfig.cmake
        ${CMAKE_CURRENT_BINARY_DIR}/rainConfigVersion.cmake
    DESTINATION lib/cmake/rain
)
