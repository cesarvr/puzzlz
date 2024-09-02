//  day8.cpp
//
//  Created by Cesar on 18/10/2023.
//

#include <iostream>
#include <vector>
#include <sstream>

const char * payload = R""""(
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 6
rect 1x1
rotate row y=0 by 5
rect 1x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 5
rect 2x1
rotate row y=0 by 2
rect 1x1
rotate row y=0 by 4
rect 1x1
rotate row y=0 by 3
rect 2x1
rotate row y=0 by 7
rect 3x1
rotate row y=0 by 3
rect 1x1
rotate row y=0 by 3
rect 1x2
rotate row y=1 by 13
rotate column x=0 by 1
rect 2x1
rotate row y=0 by 5
rotate column x=0 by 1
rect 3x1
rotate row y=0 by 18
rotate column x=13 by 1
rotate column x=7 by 2
rotate column x=2 by 3
rotate column x=0 by 1
rect 17x1
rotate row y=3 by 13
rotate row y=1 by 37
rotate row y=0 by 11
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=4 by 1
rotate column x=0 by 1
rect 10x1
rotate row y=2 by 37
rotate column x=19 by 2
rotate column x=9 by 2
rotate row y=3 by 5
rotate row y=2 by 1
rotate row y=1 by 4
rotate row y=0 by 4
rect 1x4
rotate column x=25 by 3
rotate row y=3 by 5
rotate row y=2 by 2
rotate row y=1 by 1
rotate row y=0 by 1
rect 1x5
rotate row y=2 by 10
rotate column x=39 by 1
rotate column x=35 by 1
rotate column x=29 by 1
rotate column x=19 by 1
rotate column x=7 by 2
rotate row y=4 by 22
rotate row y=3 by 5
rotate row y=1 by 21
rotate row y=0 by 10
rotate column x=2 by 2
rotate column x=0 by 2
rect 4x2
rotate column x=46 by 2
rotate column x=44 by 2
rotate column x=42 by 1
rotate column x=41 by 1
rotate column x=40 by 2
rotate column x=38 by 2
rotate column x=37 by 3
rotate column x=35 by 1
rotate column x=33 by 2
rotate column x=32 by 1
rotate column x=31 by 2
rotate column x=30 by 1
rotate column x=28 by 1
rotate column x=27 by 3
rotate column x=26 by 1
rotate column x=23 by 2
rotate column x=22 by 1
rotate column x=21 by 1
rotate column x=20 by 1
rotate column x=19 by 1
rotate column x=18 by 2
rotate column x=16 by 2
rotate column x=15 by 1
rotate column x=13 by 1
rotate column x=12 by 1
rotate column x=11 by 1
rotate column x=10 by 1
rotate column x=7 by 1
rotate column x=6 by 1
rotate column x=5 by 1
rotate column x=3 by 2
rotate column x=2 by 1
rotate column x=1 by 1
rotate column x=0 by 1
rect 49x1
rotate row y=2 by 34
rotate column x=44 by 1
rotate column x=40 by 2
rotate column x=39 by 1
rotate column x=35 by 4
rotate column x=34 by 1
rotate column x=30 by 4
rotate column x=29 by 1
rotate column x=24 by 1
rotate column x=15 by 4
rotate column x=14 by 1
rotate column x=13 by 3
rotate column x=10 by 4
rotate column x=9 by 1
rotate column x=5 by 4
rotate column x=4 by 3
rotate row y=5 by 20
rotate row y=4 by 20
rotate row y=3 by 48
rotate row y=2 by 20
rotate row y=1 by 41
rotate column x=47 by 5
rotate column x=46 by 5
rotate column x=45 by 4
rotate column x=43 by 5
rotate column x=41 by 5
rotate column x=33 by 1
rotate column x=32 by 3
rotate column x=23 by 5
rotate column x=22 by 1
rotate column x=21 by 2
rotate column x=18 by 2
rotate column x=17 by 3
rotate column x=16 by 2
rotate column x=13 by 5
rotate column x=12 by 5
rotate column x=11 by 5
rotate column x=3 by 5
rotate column x=2 by 5
rotate column x=1 by 5
)"""";

using namespace std;
using i32 = int64_t;
using Pixels = std::vector<i32>;

const int LIMIT_X = 50;
const int LIMIT_Y = 6;

void rect(Pixels &grid, i32 x, i32 y){
    for(auto index=0; index<y; index++)
        for(auto ix=0; ix<x; ix++)
            grid[index] = grid[index] | (1 << ix);
}


void rotate_column(Pixels &grid, int x, int val){
    auto size = int(grid.size());
    vector<i32> tmp(grid.size(), 0);

    for(int iy=0; iy<size; iy++){
        auto *row = &grid[iy];
        auto target_bit = 1UL << x;

        if(*row & target_bit){
            *row = *row ^ target_bit;

            int location = (iy + val) % size;
            tmp[location] = tmp[location] | target_bit;
        }
    }

    for(int i=0; i<size; i++)
        grid[i] = grid[i] | tmp[i];
}

void rotate_row(Pixels &grid, int y, int val){
    auto row = grid[y];

    i32 tmp_row = 0;
    for(int x=0; x<LIMIT_X; x++){
        if(row & (1UL << x)){
            i32 jmp = (val + x) % LIMIT_X;
            tmp_row = tmp_row | (1UL << jmp);
        }
    }

    grid[y] = tmp_row;

}



int dbg(Pixels& grid){
    int counter = 0;
    for(auto row: grid){
        for(auto x=0; x<LIMIT_X; x++){

            if(row & (1UL << x)){
                std::cout << "#";
                counter++;
            }else{
                std::cout << " ";
            }
        }
        std::cout << "\n";
    }
    cout << "----------------------- \n\n";
    return counter;
}

template <typename FN>
void rotate(i32 &t1, Pixels& grid, FN&& rotation_func){
    string rotate_type;
    string rotate_axis;
    t1 >> rotate_axis;
    auto eq = rotate_axis.find("=");
    string val;
    string y = rotate_axis.substr(eq+1, rotate_axis.size());
    t1 >> val;
    t1 >> val;
    std::cout << "val1: " << y << ", val2: "<< val << "\n";
    rotation_func(grid, stoi(y), stoi(val));
}


void solve_1(std::string payload){
    std::stringstream ss(payload);
    std::string token;
    Pixels grid(LIMIT_Y,0);

    while(std::getline(ss,token,'\n')){
        if(token == "")
            continue;

        std::basic_stringstream<string> t1(token);
        string cmd;
        string args;
        t1 >> cmd;


        if(cmd == "rect"){
            t1 >> args;
            auto where_is_x = args.find("x");
            // 3x2
            string val1 = args.substr(0,where_is_x); // pick 3 from 3x2
            string val2 = args.substr(where_is_x+1,args.size()); // pick 2 from 3x2
            cout << "rect -> " << val1 << ", " << val2 << '\n';
            rect(grid, stoi(val1), stoi(val2));
        }

        if(cmd == "rotate"){
            string rotate_type;
            string rotate_axis;
            t1 >> rotate_type;

            if(rotate_type == "row"){
                std::cout << "rotate row: ";
                rotate(t1, grid, rotate_row);
            }

            if(rotate_type == "column"){
                std::cout << "rotate column: ";
                rotate(t1, grid, rotate_column);
            }


        }
        int r = dbg(grid);
        cout << "progress => " << r << '\n';

    }

    int r = dbg(grid);
    cout << "solution = " << r << '\n';
}

int main(int argc, const char * argv[]) {

    solve_1(payload);
    return 0;
}

