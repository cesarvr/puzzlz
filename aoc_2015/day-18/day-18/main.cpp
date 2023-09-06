//
//  main.cpp
//  day-18
//
//  Created by Cesar Valdez on 08/09/2022.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    string seed = "HOH";
    string hello = "Hello World \n";
    std::string x = seed.substr(0, 6);
    
    auto _hello = x.replace(1, 6, "ELLO");
 
    std::cout << "?? ->" << x << std::endl;
    std::cout << "hello ->" << _hello << std::endl;
    
    return 0;
}
