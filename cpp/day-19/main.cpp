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
            puzzle19.molecules[key].push_back(value);
            continue;
        }else{
            puzzle19.target = line;
        }
    }

    return puzzle19;
}

std::vector<std::string> replacer(std::string &key, std::vector<std::string> replacements, std::string& candidate){
    int starting_position = candidate.find(key);
    auto key_len = key.size();
    std::vector<std::string> replaced_strings;

    while(starting_position != std::string::npos){
        for(auto& replacement: replacements){
            replaced_strings.push_back(candidate);
            replaced_strings.back().replace(starting_position, key_len, replacement);
        }

        starting_position = candidate.find(key, starting_position + key_len);
    }

    return replaced_strings;
}

std::map<std::string, bool> solution1(std::map<std::string, std::vector<std::string>>& molecules, std::string& target){
    std::map<std::string, bool> mutation_mapping;
    for(auto &pair: molecules){
        auto key = pair.first;
        auto value = pair.second;
        auto mutations = replacer(key, value, target);

        for(auto mutation: mutations){
            mutation_mapping[mutation] = true;
        }
    }

    return mutation_mapping;
}

void solve_problem_1(Puzzle19& p){
    auto resp1 = solution1(p.molecules, p.target);
    std::cout << "solution 1: " << resp1.size() << std::endl;
}

void solve_problem_2(Puzzle19& p){
    auto seeds = p.molecules["e"];
    p.molecules.erase("e");
    int mutations = 0;

    while(true){
        for(auto seed: seeds){
            
        }
        mutations++;
    }
}

int main() {
    auto puzzle_input = load_file("prod.dat");


    return 0;
}
