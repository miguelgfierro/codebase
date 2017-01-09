CMAKE_MINIMUM_REQUIRED (VERSION 2.6)
SET(KEYWORD codebase)

# Start a project
PROJECT(${KEYWORD})

# Define system type
IF(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    ADD_DEFINITIONS(-DSYSTEMTYPE_LINUX)
    set(SYSTEM_FOLDER_NAME linux)
ELSEIF(${CMAKE_SYSTEM_NAME} MATCHES "Windows")
    ADD_DEFINITIONS(-DSYSTEMTYPE_WINDOWS)
    set(SYSTEM_FOLDER_NAME windows)
ELSEIF(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    ADD_DEFINITIONS(-DSYSTEMTYPE_MAC)
    SET(SYSTEM_FOLDER_NAME mac)
ENDIF(${CMAKE_SYSTEM_NAME} MATCHES "Linux")

# Define standard paths.
set(MY_OUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/out/${SYSTEM_FOLDER_NAME})
set(MY_SRC_PATH ${CMAKE_CURRENT_SOURCE_DIR}/src)

# Search for source code.
SET (SOURCES
    playground.cpp
    log/timer.hpp
    numeric/math_constants.hpp
    numeric/math_utils.hpp
    io/read_file.cpp
    io/read_file.hpp
)

SET(MY_OUT_PATH ${CMAKE_CURRENT_SOURCE_DIR}/out/${SYSTEM_FOLDER_NAME})
SET(MY_SRC_PATH ${CMAKE_CURRENT_SOURCE_DIR}/ssm)
SET(EXECUTABLE_OUTPUT_PATH ${MY_OUT_PATH})

# Automatically add include directories if needed.
#FOREACH(header_file ${folder_header})
#  GET_FILENAME_COMPONENT(p ${header_file} PATH)
#  INCLUDE_DIRECTORIES(${p})
#ENDFOREACH(header_file ${folder_header})

# Set location for binary output
set(EXECUTABLE_OUTPUT_PATH ${MY_OUT_PATH})
ADD_EXECUTABLE(${KEYWORD} ${SOURCES})

# Set up our main executable.
#IF (folder_source)
#  ADD_EXECUTABLE(${KEYWORD} ${folder_source} ${folder_header})
#ELSE (folder_source)
#  MESSAGE(FATAL_ERROR "No source code files found. Please add something")
#ENDIF (folder_source)


