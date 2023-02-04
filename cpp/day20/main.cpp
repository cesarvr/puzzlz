#include <iostream>

using namespace std;

int giftCalculator(int house_target) {
    int ret = 0;
    for(int house=house_target; house >= 1; house--){
        if((house_target % house) == 0){
            ret += house * 10;
        }
    }

    return ret;
}

int housesCalc(int target){
    int start = 0;
    int gift_target = giftCalculator(target);
    for(int house=0; house<target; house++){
        int gifts = giftCalculator(house);
        cout << "house: " << house << gifts << " target: " << target << " => "<< (gifts >= gift_target) << endl;
        if(gifts >= gift_target){
            return house;
        }
    }

    return 0;
}



int main() {

    housesCalc(20);
    return 0;
}
