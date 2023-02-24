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

int computeGiftForHouseV2(int n){
    if(n%2 != 0) return -1;
    int tail = n/2;
    int total = tail;
    for(int i=3; i<tail; i++){
        if(n%i==0){
            tail = n/i;

            if(tail>i)
                total += tail;

            total += i;
        }
    }

    return ((total + n) * 10) + 30 ;
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
    int giftTarget = computeGiftForHouseV2(house_target);

    int section = 0;
    int max_gift = -1;

    while(true){
        for(int house=0; house<10; house+=2) {
            if(house == 0 && section == 0)
                continue;

            int gifts = computeGiftForHouseV2(section + house);

            if((section) == 1680){
                std::cout << "?";
            }

            if(section+house > house_target){
                return -1;
            }

            if(gifts >= giftTarget){
                return house+section;
            }



            max_gift = std::max(gifts, max_gift);
        }

        if(giftTarget > (max_gift * 1000) && house_target >= (section + 100)){
            section += 10;
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
    int N = 110;
    auto val = getMinHouseWithMoreOrEqGift(N);
    for(int x=1; x<=N; x++){
        std::cout << x << " => " << computeGiftForHouse(x) << std::endl;
    }

    std::cout << "value: " << val << std::endl;
}

template <typename Fn>
int bench(const std::string& msg, Fn&& fn){
    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
    int ret = fn();
    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();

    std::cout << "Time difference for " << msg << " = " << std::chrono::duration_cast<std::chrono::nanoseconds> (end - begin).count() << "[ns]" << std::endl;
    std::cout << "Time difference for " << msg << " = " << std::chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() << "[ms]" << std::endl;

    return ret;
}


void test_solution_4(){
    int HOUSE_TARGET = 29000000;
    auto optimizedGiftCalculator = [&](){ return getMinHouseWithMoreOrEqGiftV2(HOUSE_TARGET); };
    auto giftCalculator = [&](){ return getMinHouseWithMoreOrEqGift(HOUSE_TARGET); };

    auto v1 = bench("optimized", optimizedGiftCalculator);
    auto v2 = bench("normal",giftCalculator);

    std::cout << "valid: " << isEQUAL(v1 == v2) << std::endl;
    std::cout << "v1: " << v1 << std::endl;
    std::cout << "v2: " << v2 << std::endl;
}



int main() {

//    test_1();
//    test_2();
//    test_solution_1();
//    test_solution_2();
test_solution_3_2();
test_solution_4();
    return 0;
}
