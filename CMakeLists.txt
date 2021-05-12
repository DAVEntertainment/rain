cmake_minimum_required(VERSION 3.16.6)
project(rain)

include(${CMAKE_CURRENT_LIST_DIR}/cmake/path.cmake)

include(${RAIN_CMAKE_DIR}/config.cmake)

include(${RAIN_TARGETS_DIR}/core.cmake)
include(${RAIN_TARGETS_DIR}/rain.cmake)

enable_testing()
include(${RAIN_TARGETS_DIR}/test-scripts.cmake)
