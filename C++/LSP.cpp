#include <iostream>
using namespace std;

class Bird {
public:
    virtual void fly() const {
        cout << "Bird is flying" << endl;
    }
};

class Sparrow : public Bird {
public:
    void fly() const override {
        cout << "Sparrow is flying" << endl;
    }
};

class Penguin : public Bird {
public:
    void fly() const override {
        cout << "Penguins can't fly" << endl;
    }
};

void makeBirdFly(const Bird& bird) {
    bird.fly();
}

int main() {
    Sparrow sparrow;
    Penguin penguin;

    makeBirdFly(sparrow); 
    makeBirdFly(penguin); 

    return 0;
}
