
#ifndef READ_FILE_HPP
#define READ_FILE_HPP

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>

/**
    Example:
    std::string filename = "../../../share/traj.csv";
    std::vector<float> data;
    bool flag = readCSVFile(filename, data);
    if(!flag) std::cerr << "File not read correctly" << std::endl;
    for(size_t i = 0; i < data.size(); i++){
        std::cout << data.at(i) << std::endl;
    }
 */
bool readFile(const std::string filename, std::vector<float>& data, std::string sep_char=" ");
bool readCSVFile(const std::string filename, std::vector<float>& data);


#endif //READ_FILE_HPP
