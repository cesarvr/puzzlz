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

    int section = 0;
    int max_gift = -1;
    while(true){
        for(int house=-2; house<10; house+=2) {
            int gifts = computeGiftForHouse(house);
            if(gifts >= giftTarget){
                return house;
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

void test_solution_3_2(){
    auto val = getMinHouseWithMoreOrEqGift(1999);
    for(int x=0; x<=2000; x++){
        std::cout << x << " => " << computeGiftForHouse(x) << std::endl;
    }

    std::cout << "value: " << val << std::endl;
}

void test_solution_4(){
    auto val = getMinHouseWithMoreOrEqGift(10000000);
    std::cout << "val " << val << std::endl;
  //  std::cout << "Testing Solution 1 House 40 <= House x -> " << isEQUAL(val == 60480) << std::endl;
}


int main() {

//    test_1();
//    test_2();
//    test_solution_1();
//    test_solution_2();
test_solution_3_2();
   // test_solution_4();
    return 0;
}
