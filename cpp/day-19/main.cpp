#include <iostream>
#include <fstream>
#include <sstream>
#include <map>
#include <vector>
#include <unordered_map>
#include <algorithm>

using Molecules = std::unordered_map<std::string, std::vector<std::string>>;
using Mutation = std::unordered_map<std::string, bool>;

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

Mutation solution1(Molecules& molecules, std::string& target){
    Mutation mutation_mapping;
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
    Mutation mutations = solution1(p.molecules, p.target);
    std::cout << "solution 1: " << mutations.size() << std::endl;
}

int get_max_len(Molecules& molecules){
    int _max = -1;

    for(auto& molecule: molecules){
        int n = molecule.first.size();
        _max = std::max(_max, n);
    }

    return _max;
}

int get_progress(std::string& candidate, std::string& target){
    int limit = std::min((int) candidate.size(), (int) target.size());
    int progress_counter = 0;
    for(progress_counter=0; progress_counter<limit; progress_counter++){
        if(candidate[progress_counter] != target[progress_counter]){
            return progress_counter;
        }
    }
    return progress_counter;
}

std::vector<std::string> remove_repeated(std::vector<std::string> &samples){
    std::vector<std::string> ret;
    Mutation muts;
    for(auto &sample: samples){
        if(muts.find(sample) == muts.end()){
            ret.push_back(sample);
            muts[sample] = true;
        }
    }
    return ret;
}

std::vector<std::string> remove_low_performing(std::vector<std::string> &samples, std::string target, int max_progress, double delta){
    std::vector<std::string> ret;

    for(auto &sample: samples){
        if(get_progress(sample, target) >= (max_progress*delta)){
            ret.push_back(sample);
        }
    }
    return ret;
}


int solve_problem_2(Puzzle19& p){
    auto seeds = p.molecules["e"];
    p.molecules.erase("e");
    int cycles = 2;
    Mutation molecules_states;
    int padding = get_max_len(p.molecules);
    int max_progress = -1;
    std::cout << "padding -> " << padding << std::endl;
    std::vector<std::string> samples;

    while(true){
        for(auto seed: seeds){
            int progress = get_progress(seed, p.target);
            int from = progress - padding;
            max_progress = std::max(max_progress, progress);

            from = (from > 0)? from : 0;

            //ORnPBPMgAr
            //if(progress >= 4){
            if(seed == "Ca"){
                std::cout << "dbg";
            }

            std::string in = seed.substr(from, 6);
            molecules_states = solution1(p.molecules, in);

            for(auto &mol: molecules_states){
                std::string w = mol.first;
                std::string base = seed;
                std::string _smpl = base.replace(from, 6, w);

                samples.push_back(_smpl);
            }
        }

        samples = remove_repeated(samples);
        if(max_progress > 6 && max_progress < 80) {
            samples = remove_low_performing(samples, p.target, max_progress, 0.9);
        }

        if(max_progress >= 80) {
            samples = remove_low_performing(samples, p.target, max_progress, 0.98);
        }


        seeds.clear();
        for(auto &sample: samples){
            //if(get_progress(sample, p.target) == p.target.size()){
            if(sample == p.target){
                std::cout << "target -> " << sample << std::endl;
                std::cout << "steps -> " << cycles << std::endl;
                std::cout << "size: " << samples.size() << std::endl;
                return cycles;
            }

            seeds.push_back(sample);
        }

        samples.clear();
        cycles++;
    }
}

int main() {
    auto puzzle_input = load_file("prod.dat");
    //solve_problem_1(puzzle_input);
    solve_problem_2(puzzle_input);

    return 0;
}
