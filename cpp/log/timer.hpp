
#ifndef TIMER_HPP
#define TIMER_HPP

#include "time.h"

class Timer
{
public:
  void startTimer() { m_start = clock();}
  void stopTimer() { m_end = clock();}
  double getTimeInSec(){
    m_elapsed_time_sec = (double)(m_end-m_start)/CLOCKS_PER_SEC;
    std::cout << "Time required for execution: " << m_elapsed_time_sec << " seconds" << std::endl;
    return m_elapsed_time_sec;
  }
  double getTimeInMiliSec(){
    m_elapsed_time_sec = (double)(m_end-m_start)/CLOCKS_PER_SEC;
    std::cout << "Time required for execution: " << m_elapsed_time_sec*1000 << " miliseconds" << std::endl;
    return m_elapsed_time_sec*1000;
  }

private:
  clock_t m_start;
  clock_t m_end;
  double m_elapsed_time_sec;
};




#endif //TIMER_HPP

