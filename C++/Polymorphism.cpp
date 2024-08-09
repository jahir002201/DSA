#include <iostream>
using namespace std;

class Shape {
public:
    virtual void draw() const { cout << "Drawing a shape" << endl; }
};

class Circle : public Shape {
public:
    void draw() const override { cout << "Drawing a circle" << endl; }
};

class Square : public Shape {
public:
    void draw() const override { cout << "Drawing a square" << endl; }
};

int main() {
    Shape* shape;

    Circle circle;
    Square square;

    shape = &circle;
    shape->draw(); 

    shape = &square;
    shape->draw();  

    return 0;
}
