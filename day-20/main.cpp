#include <iostream>

int computeGiftForHouse(int house){
    int ret = 0;
    for(int i=2; i<=house; i++){
        if(house%i == 0){
            ret += i;
        }
    }

    return (ret * 10) + 10;
}

int getMinHouseWithMoreOrEqGift(int house_target, int start_from_house=0){
    int giftTarget = computeGiftForHouse(house_target);
    for(int house=start_from_house; house<house_target; house+=2)
    {
        int gifts = computeGiftForHouse(house);
        if(gifts >= giftTarget){
            return house;
        }
    }
    return -1;
}

int getMinHouseWithMoreOrEqGiftV2(int house_target, int start_from_house=0){
    int giftTarget = computeGiftForHouse(house_target);

    int section = house_target / 4;
    int max_gift = -1;
    while(true){
        for(int house=0; house<=10; house+=2) {
            int gifts = computeGiftForHouse(section+house);
            if(gifts >= giftTarget){
                return section+house;
            }
            max_gift = std::max(gifts, max_gift);
        }

        if(giftTarget > (max_gift * 2)){
            section += 100;
        }else{
            section += 10;
        }
    }
}


std::string isEQUAL(bool x) {
    return x?"True":"False";
}

void test_1(){
    std::cout << "House 1 == 10 -> " << isEQUAL(computeGiftForHouse(1) == 10) << std::endl;
}

void test_2(){
    std::cout << "House 9 == 130 -> " << isEQUAL(computeGiftForHouse(9) == 130) << std::endl;
}

void test_solution_1(){
    std::cout << "Testing Solution 1 House 9 <= House 8 -> " << isEQUAL(getMinHouseWithMoreOrEqGift(9) == 8) << std::endl;
}

void test_solution_2(){
    auto val = getMinHouseWithMoreOrEqGift(41);
    std::cout << "value: "<< val << std::endl;
    std::cout << "Testing Solution 1 House 40 <= House x -> " << isEQUAL(val == 20) << std::endl;
}

void test_solution_3(){
    auto val = getMinHouseWithMoreOrEqGift(101000);

    std::cout << "Testing Solution 1 House 40 <= House x -> " << isEQUAL(val == 60480) << std::endl;
}

void test_solution_3_v2(){
    auto val = getMinHouseWithMoreOrEqGift(1999);
    auto val2 = getMinHouseWithMoreOrEqGiftV2(1999);

    std::cout << "value 1: " << val << std::endl;
    std::cout << "value 2: " << val2 << std::endl;
    std::cout << "value: " << isEQUAL(val == val2) << std::endl;
}

template <typename F>
int timing(F&& fn) {
    auto start = std::chrono::high_resolution_clock::now();
    auto val = fn();
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);

    std::cout << "val " << val << std::endl;
    std::cout << "timelapsed: " << (duration.count() / 1000) << std::endl;
    //  std::cout << "Testing Solution 1 House 40 <= House x -> " << isEQUAL(val == 60480) << std::endl;

    return val;
}

void test_solution_4(){
    auto fn1 = []() -> int { return getMinHouseWithMoreOrEqGift(100000); };
    int v1 = timing(fn1);

    auto fn2 = []() -> int { return getMinHouseWithMoreOrEqGiftV2(100000); };
    int v2 = timing(fn2);
    std::cout << "value: " << isEQUAL(v1 == v2) << std::endl;
}


int main() {

//    test_1();
//    test_2();
//    test_solution_1();
//    test_solution_2();
    test_solution_3_v2();
     test_solution_4();
    return 0;
}
