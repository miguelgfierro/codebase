/**
  * Based on https://github.com/rgbdemo/nestk/blob/master/ntk/numeric/utils.h
  */

#ifndef MATH_CONSTANTS_HPP
#define MATH_CONSTANTS_HPP

namespace math
  {
    //: pi, e and all that
    static  const double e               =2.7182818284590452354;
    static  const double log2e           =1.4426950408889634074;
    static  const double log10e          =0.43429448190325182765;
    static  const double ln2             =0.69314718055994530942;
    static  const double ln10            =2.30258509299404568402;
    static  const double pi              =3.14159265358979323846;
    static  const double pi_over_2       =1.57079632679489661923;
    static  const double pi_over_4       =0.78539816339744830962;
    static  const double one_over_pi     =0.31830988618379067154;
    static  const double two_over_pi     =0.63661977236758134308;
    static  const double two_over_sqrtpi =1.12837916709551257390;
    static  const double sqrt2           =1.41421356237309504880;
    static  const double sqrt1_2         =0.70710678118654752440;

    //: IEEE double machine precision
    static  const double eps             =2.2204460492503131e-16;
    static  const double sqrteps         =1.490116119384766e-08;
    //: IEEE single machine precision
    static  const float float_eps        =1.192092896e-07f;
    static  const float float_sqrteps    =3.4526698307e-4f;

	// isnan does not exist with Visual Studio
#ifdef _MSC_VER
	inline bool isnan(float x) { return _isnan(x) != 0; }
	inline bool isnan(double x) { return _isnan(x) != 0; }
#else
    inline bool isnan(float x) { return std::isnan(x); }
    inline bool isnan(double x) { return std::isnan(x); }
#endif

    // rnd (rounding; 0.5 rounds up)
    // Use C99 functions, which GCC implements as an intrinsic
    // Or in simpler terms - is at least 3 times faster.
#ifdef _MSC_VER
	inline int rnd(float  x) { return floor(x + 0.5f); }
    inline int rnd(double x) { return floor(x + 0.5); }
#else
	inline int rnd(float  x) { return lroundf(x); }
    inline int rnd(double x) { return lround(x); }
#endif

    // floor -- round towards minus infinity
    inline int floor(float  x) { return static_cast<int>(x>=0.f?x:(x==static_cast<int>(x)?x:x-1.f)); }
    inline int floor(double x) { return static_cast<int>(x>=0.0?x:(x==static_cast<int>(x)?x:x-1.0)); }
    inline int floor(int x) { return x; }

    // ceil -- round towards plus infinity
    inline int ceil(float  x) { return static_cast<int>(x<0.f?x:(x==static_cast<int>(x)?x:x+1.f)); }
    inline int ceil(double x) { return static_cast<int>(x<0.0?x:(x==static_cast<int>(x)?x:x+1.0)); }
    inline int ceil(int x) { return x; }

    // abs
    inline bool           abs(bool x)          { return x; }
    inline unsigned char  abs(unsigned char x) { return x; }
    inline unsigned char  abs(signed char x)   { return x < 0 ? -x : x; }
    inline unsigned char  abs(char x)          { return (unsigned char)x; }
    inline unsigned short abs(short x)         { return x < 0 ? -x : x; }
    inline unsigned short abs(unsigned short x){ return x; }
    inline unsigned int   abs(int x)           { return x < 0 ? -x : x; }
    inline unsigned int   abs(unsigned int x)  { return x; }
    inline unsigned long  abs(long x)          { return x < 0L ? -x : x; }
    inline unsigned long  abs(unsigned long x) { return x; }
    inline float          abs(float x)         { return x < 0.0f ? -x : x; }
    inline double         abs(double x)        { return x < 0.0 ? -x : x; }
    inline long double    abs(long double x)   { return x < 0.0 ? -x : x; }

    // max
    inline int           max(int x, int y)                     { return (x > y) ? x : y; }
    inline unsigned int  max(unsigned int x, unsigned int y)   { return (x > y) ? x : y; }
    inline long          max(long x, long y)                   { return (x > y) ? x : y; }
    inline unsigned long max(unsigned long x, unsigned long y) { return (x > y) ? x : y;}
    inline float         max(float x, float y)                 { return (x < y) ? y : x; }
    inline double        max(double x, double y)               { return (x < y) ? y : x; }
    template <class T> T max(const std::vector<T> &t)          { return *std::max_element(t.begin(), t.end()); }

    // min
    inline int           min(int x, int y)                     { return (x < y) ? x : y; }
    inline unsigned int  min(unsigned int x, unsigned int y)   { return (x < y) ? x : y; }
    inline long          min(long x, long y)                   { return (x < y) ? x : y; }
    inline unsigned long min(unsigned long x, unsigned long y) { return (x < y) ? x : y;}
    inline float         min(float x, float y)                 { return (x > y) ? y : x; }
    inline double        min(double x, double y)               { return (x > y) ? y : x; }
    template <class T> T min(const std::vector<T> &t)          { return *std::min_element(t.begin(), t.end()); }


    // sqr (square)
    inline bool          sqr(bool x)          { return x; }
    inline int           sqr(int x)           { return x*x; }
    inline unsigned int  sqr(unsigned int x)  { return x*x; }
    inline long          sqr(long x)          { return x*x; }
    inline unsigned long sqr(unsigned long x) { return x*x; }
    inline float         sqr(float x)         { return x*x; }
    inline double        sqr(double x)        { return x*x; }

    // cube
    inline bool          cube(bool x)          { return x; }
    inline int           cube(int x)           { return x*x*x; }
    inline unsigned int  cube(unsigned int x)  { return x*x*x; }
    inline long          cube(long x)          { return x*x*x; }
    inline unsigned long cube(unsigned long x) { return x*x*x; }
    inline float         cube(float x)         { return x*x*x; }
    inline double        cube(double x)        { return x*x*x; }

	inline double		 log2(double x)        { return log(x)/log2e; }
} // end of math

#endif //MATH_CONSTANTS_HPP