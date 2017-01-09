
#include "read_file.hpp"


bool readFile(const std::string filename, std::vector<float>& data, std::string sep_char){
  std::ifstream file;
  std::string line;
  int npos, lpos;
  float d;
  file.open(filename.c_str(),std::ios::in);
  if(!file.is_open()) return false;
  while(getline(file,line)){
    line += sep_char;
    npos=0;
    lpos=0;
    while ((npos = (int)line.find(sep_char,lpos)) != std::string::npos){
      if (npos > lpos){
        std::istringstream iss(line.substr(lpos, npos-lpos));
        if (iss >> d){
          data.push_back(d);
        }
      }
      lpos = npos + 1;
    }
  }

  return true;
}

bool readCSVFile(const std::string filename, std::vector<float>& data){
	return readFile(filename, data, ",");
}
