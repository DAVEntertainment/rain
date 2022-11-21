cmake_minimum_required(VERSION 3.24)

add_subdirectory(core)
add_subdirectory(logger)
add_subdirectory(misc)

##################################################################
# library properties
##################################################################
get_filename_component(RAIN_REPO_DIR ${CMAKE_CURRENT_LIST_DIR}/../.. ABSOLUTE)
set(RAIN_SRCS_DIR ${RAIN_REPO_DIR}/srcs)
set(RAIN_PUBLIC_HEADER_DIR ${RAIN_REPO_DIR}/include)
set(RAIN_INCLUDES ${RAIN_SRCS_DIR} ${RAIN_PUBLIC_HEADER_DIR})

set(RAIN_HEADERS # files in rain/include
    ${RAIN_PUBLIC_HEADER_DIR}/rain/factory.h
    ${RAIN_PUBLIC_HEADER_DIR}/rain/rain_api.h
    ${RAIN_PUBLIC_HEADER_DIR}/rain/rain.h
)

set(RAIN_SOURCES
    factory.cpp
)

add_library(rain SHARED
    ${RAIN_HEADERS}
    ${RAIN_SOURCES}
)

target_link_libraries(rain
    PRIVATE
        rain_core
)

target_include_directories(rain
    PRIVATE
        ${RAIN_INCLUDES}
)

target_include_directories(rain SYSTEM INTERFACE
    "$<BUILD_INTERFACE:${RAIN_INCLUDES}>"
    "$<INSTALL_INTERFACE:$<INSTALL_PREFIX>/include>"
)

target_compile_definitions(rain
    PRIVATE
        -DRAIN_EXPORTS=1
)

##################################################################
# install
##################################################################
install(
    TARGETS rain
    EXPORT rain
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
    COMPATIBILITY ExactVersion # SameMajorVersion|AnyNewerVersion|SameMajorVersion|SameMinorVersion|ExactVersion
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

# install headers
install(
    DIRECTORY ${RAIN_PUBLIC_HEADER_DIR}/rain
    DESTINATION include
)
