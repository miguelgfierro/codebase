/**
  * Based on https://github.com/rgbdemo/nestk/blob/master/ntk/numeric/utils.h
  */

#ifndef MATH_UTILS_HPP
#define MATH_UTILS_HPP

#include <algorithm>
#include "math_constants.hpp"

inline double radToDeg(double rad_angle) { return (rad_angle*180.0)/math::pi; }
inline double degToRad(double deg_angle) { return (deg_angle*math::pi)/180.0; }

template <class T, class U>
inline bool inRange(T lower, U data, T upper){
    return (data >= lower) && (data <= upper);
}

inline bool equalFloat (float lhs, float rhs,
      float epsilon = std::numeric_limits<float>::epsilon()){
    return std::abs(lhs - rhs) <= epsilon;
}

inline bool lessOrEqualFloat(float lhs, float rhs,
       float epsilon = std::numeric_limits<float>::epsilon()){
    return lhs <= (rhs+epsilon);
}

inline bool greaterOrEqualFloat(float lhs, float rhs,
       float epsilon = std::numeric_limits<float>::epsilon()){
    return (lhs+epsilon) >= rhs;
}

inline bool isEven(int num){
    if (num % 2 == 0) return true;
    else return false;
}

inline bool isOdd(int num){
    if (num % 2 == 0) return false;
    else return true;
}

#endif //MATH_UTILS_HPP
