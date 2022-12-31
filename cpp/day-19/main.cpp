#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>

struct Puzzle19 {
    std::map<std::string, std::vector<std::string>> molecules;
    std::string target;
};

Puzzle19 load_file(std::string&& filename){
    std::ifstream file;
    file.open (filename);
    std::string line;
    Puzzle19 puzzle19;

    while (std::getline(file, line))
    {
        std::istringstream iss(line);
        std::string key, amp, value;

        if(line == ""){
            continue;
        }

        if(line.find("=>") != std::string::npos) {
            iss >> key >> amp >> value;
            std::cout << "key: " << key << " value: " << value << std::endl;
            puzzle19.molecules[key].push_back(value);
            continue;
        }else{
            puzzle19.target = line;
        }
    }

    return puzzle19;
}


std::vector<std::string> replacer(std::string &key, std::vector<std::string> replacements, std::string& candidate){
    int starting_position = candidate.find_first_of(key, 0);
    while(starting_position != std::string::npos){


        starting_position = candidate.find_first_of(key, starting_position);
    }

    for(auto& replacement: replacements){

    }
}

void solution1(Puzzle19& input, std::string& target){
    int starting_position = 0;
    for(auto &pair: input.molecules){

        auto key = pair.first;
        auto value = pair.second;


    }
}

int main() {
    std::cout << "Hello, World!" << std::endl;
    auto puzzle_input = load_file("test1.dat");

    std::cout << "size: " << puzzle_input.molecules.size() << std::endl;
    return 0;
}
