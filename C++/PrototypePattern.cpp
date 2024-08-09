#include <iostream>
using namespace std;

class Prototype {
public:
    virtual Prototype* clone() const = 0;
    virtual void show() const = 0;
    virtual ~Prototype() {}
};

class ConcretePrototype : public Prototype {
private:
    int data;
public:
    ConcretePrototype(int d) : data(d) {}
    Prototype* clone() const override { return new ConcretePrototype(*this); }
    void show() const override { cout << "ConcretePrototype data: " << data << endl; }
};

int main() {
    ConcretePrototype prototype(5);
    Prototype* clone = prototype.clone();
    clone->show();  
    delete clone;
    return 0;
}
