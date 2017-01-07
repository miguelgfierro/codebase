/**
  * Based on https://github.com/rgbdemo/nestk/blob/master/ntk/numeric/utils.h
  */

#ifndef MATH_UTILS_HPP
#define MATH_UTILS_HPP

inline double rad_to_deg(double rad_angle) { return (rad_angle*180.0)/M_PI; }
inline double deg_to_rad(double deg_angle) { return (deg_angle*M_PI)/180.0; }

template <class T, class U>
inline bool in_range(T lower, U data, T upper){
    return (data >= lower) && (data <= upper);
}

inline bool equal_float (float lhs, float rhs,
      float epsilon = std::numeric_limits<float>::epsilon()){
    return std::abs(lhs - rhs) <= epsilon;
}

inline bool less_or_equal_float (float lhs, float rhs,
       float epsilon = std::numeric_limits<float>::epsilon()){
    return lhs <= (rhs+epsilon);
}

inline bool greater_or_equal_float (float lhs, float rhs,
       float epsilon = std::numeric_limits<float>::epsilon()){
    return (lhs+epsilon) >= rhs;
}

inline bool iseven(int num){
    if (num % 2 == 0) return true;
    else return false;
}

inline bool isodd(int num){
    if (num % 2 == 0) return false;
    else return true;
}

#endif //MATH_UTILS_HPP
