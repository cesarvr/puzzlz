#include <iostream>
#include <vector>

void test_computeGiftForHouseV2Bench();

void testFindBestMinimalHouse();

void solving_puzzle();

int computeGiftForHouse(int house){
    int ret = 0;
    for(int i=2; i<=house; i++){
        if(house%i == 0){
            ret += i;
        }
    }

    return (ret * 10) + 10;
}

int computeGiftForHouseV3(int n){
    int tail = n;
    int total = 0;
    for(int i=1; i<tail; i++){
        if(n%i==0){
            tail = n/i;

            if(tail != i)
                total += tail;

            total += i;
        }
    }

    return total * 10;
}

int computeGiftForHouseV4(int n){
    int tail = n;
    int total = 0;
    int head = 0;
    for(int i=1; i<tail; i++){
        if(n%i==0){
            tail = n/i;

            if(tail != i)
                total += tail;

            total += i;
            head += i;

            if(head < 66 && i > 20){
                return 0;
            }
        }
    }

    return total * 10;
}


template <typename Fn>
int getMinHouseWithMoreOrEqGift(int house_target, Fn&& computeGifts=computeGiftForHouse, int start_from_house=1){
    int giftTarget = computeGifts(house_target);
    for(int house=start_from_house; house<=house_target; house++)
    {
        int gifts = computeGiftForHouse(house);
        if(gifts >= giftTarget){
            return house;
        }
    }
    return -1;
}

template <typename Fn>
int getMinHouseWithMoreOrEqGiftV2(int house_target, Fn&& computeGifts=computeGiftForHouse, int start_from_house=1){
    int giftTarget = computeGifts(house_target);
    for(int house=start_from_house; house<=house_target; house++)
    {
        int gifts = computeGiftForHouse(house);
        if(gifts >= giftTarget){
            return house;
        }
    }
    return -1;
}


std::string isEQUAL(bool x) {
    return x?"Pass":"Fail";
}

void test_1(){
    std::cout << "House 1 == 10 -> " << isEQUAL(computeGiftForHouse(1) == 10) << std::endl;
}

void test_2(){
    std::cout << "House 9 == 130 -> " << isEQUAL(computeGiftForHouse(9) == 130) << std::endl;
}

void test_solution_1(){
    std::cout << "Testing Solution 1 House 9 <= House 8 -> " << isEQUAL(getMinHouseWithMoreOrEqGift(9,
                                                                                                    computeGiftForHouse) == 8) << std::endl;
}

void test_solution_2(){
    auto val = getMinHouseWithMoreOrEqGift(41, computeGiftForHouse);
    std::cout << "value: "<< val << std::endl;
    std::cout << "Testing Solution 1 House 40 <= House x -> " << isEQUAL(val == 20) << std::endl;
}

void test_solution_3(){
    auto val = getMinHouseWithMoreOrEqGift(101000, computeGiftForHouse);

    std::cout << "Testing Solution 1 House 40 <= House x -> " << isEQUAL(val == 60480) << std::endl;
}

void test_solution_3_2(){
    int N = 110;
    auto val = getMinHouseWithMoreOrEqGift(N, computeGiftForHouse);
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

void test_computeGiftForHouseV2(){
    for(int i=6; i<100000; i++){
        int v1 = computeGiftForHouseV3(i);
        int v2 = computeGiftForHouse(i);
        if( v1 != v2){
            std::cout << "We got a problem: " << v1 << " != " << v2 << " for number: " << i << std::endl;
        }
    }
}

void testPerformanceAndCorrectness(std::vector<int>&& nums){
    for(int N: nums) {
        std::cout << "testing => " << N << std::endl;
        auto valid = getMinHouseWithMoreOrEqGift(N, computeGiftForHouse);
        std::cout << "running opt...\n";
        auto b = [&]() { return getMinHouseWithMoreOrEqGiftV2(N, computeGiftForHouseV4); };
        auto sol = bench("sol1", b);

        std::string status = (valid == sol) ? "Pass" : "Fail";
        if(status == "Fail")
            break;
        std::cout << "Solution: " << sol << " gifts: "<< computeGiftForHouse(sol) << " is valid: " << status << std::endl;
        std::cout << "==============\n" << std::endl;
    }
}

void test1(int N, int expected){
    std::cout << "testing => " << N << std::endl;
    auto b = [&]() { return getMinHouseWithMoreOrEqGiftV2(N, computeGiftForHouseV4); };
    auto sol = bench("sol1", b);

    std::string status = (expected == sol) ? "Pass" : "Fail";
    std::cout << "Solution: " << sol << " gifts: "<< computeGiftForHouse(sol) << " is valid: " << status << std::endl;
    std::cout << "==============\n" << std::endl;
}


int main() {
    //testFindBestMinimalHouse(139000);

   // testPerformanceAndCorrectness({19, 100, 139, 119, 200, 10000, 10090, 11091, 211, 309, 311, 21, 66}); //1000000
    test1(11, 6);
    test1(100, 84);
    test1(2019, 840);
    test1(100000, 64680);
    test1(300000, 240240);
    test1(1000999, 249480);
    
    return 0;
}


