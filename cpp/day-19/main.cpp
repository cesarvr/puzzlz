#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>

using Molecules = std::map<std::string, std::vector<std::string>>;
using Mutation = std::map<std::string, bool>;

struct Puzzle19 {
    Molecules molecules;
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

void solution1(Molecules& molecules, std::string& target, Mutation& mutation_mapping){
    for(auto &pair: molecules){
        auto key = pair.first;
        auto value = pair.second;
        auto mutations = replacer(key, value, target);

        for(auto mutation: mutations){
            mutation_mapping[mutation] = true;
        }
    }
}

void solve_problem_1(Puzzle19& p){
    Mutation mutations;
    solution1(p.molecules, p.target, mutations);
    std::cout << "solution 1: " << mutations.size() << std::endl;
}

int cmp(std::string& s1, std::string& s2){
    int limit = std::min(s1.size(), s2.size());
    for(int i=0; i<limit; i++){
        if(s1[i] !== s2[i])
    }
}

int solve_problem_2(Puzzle19& p){
    auto seeds = p.molecules["e"];
    p.molecules.erase("e");
    int cycles = 2;
    Mutation molecules_states;


    while(true){
        for(auto seed: seeds){
            solution1(p.molecules, seed, molecules_states);
        }

        if(molecules_states[p.target]){
            std::cout << "target -> " << p.target << std::endl;
            std::cout << "steps -> " << cycles << std::endl;
            return cycles;
        }

        seeds.clear();
        for(auto& kv: molecules_states){
            seeds.push_back(kv.first);
        }

        molecules_states.clear();
        cycles++;
    }
}

int main() {
    auto puzzle_input = load_file("test3_2.dat");
    //solve_problem_1(puzzle_input);
    solve_problem_2(puzzle_input);

    return 0;
}
