#include <iostream>
using namespace std;

class Car {
private:
    int speed;
public:
    Car() : speed(0) {}
    void accelerate(int amount) { speed += amount; }
    void brake(int amount) { if (speed - amount >= 0) speed -= amount; }
    int getSpeed() const { return speed; }
};

int main() {
    Car myCar;
    myCar.accelerate(50);
    cout << "Current speed: " << myCar.getSpeed() << endl;
    myCar.brake(20);
    cout << "Current speed: " << myCar.getSpeed() << endl;
    return 0;
}
