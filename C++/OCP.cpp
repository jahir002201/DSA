#include <iostream>
#include <vector>
using namespace std;

// Base class
class Shape {
public:
    virtual void draw() const = 0; // Pure virtual function
};

// Derived class
class Circle : public Shape {
public:
    void draw() const override {
        cout << "Drawing a circle" << endl;
    }
};

// Another derived class
class Square : public Shape {
public:
    void draw() const override {
        cout << "Drawing a square" << endl;
    }
};

void renderShapes(const vector<Shape*>& shapes) {
    for (const auto& shape : shapes) {
        shape->draw();
    }
}

int main() {
    vector<Shape*> shapes;
    shapes.push_back(new Circle());
    shapes.push_back(new Square());
    
    renderShapes(shapes);
    
    // Clean up
    for (auto shape : shapes) {
        delete shape;
    }
    
    return 0;
}
