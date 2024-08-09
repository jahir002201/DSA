#include <iostream>
#include <string>
using namespace std;

class Product {
private:
    string partA;
    string partB;
public:
    void setPartA(const string& a) { partA = a; }
    void setPartB(const string& b) { partB = b; }
    void show() const {
        cout << "Product parts: " << partA << ", " << partB << endl;
    }
};

class Builder {
public:
    virtual void buildPartA() = 0;
    virtual void buildPartB() = 0;
    virtual Product* getResult() = 0;
};

class ConcreteBuilder : public Builder {
private:
    Product* product;
public:
    ConcreteBuilder() { product = new Product(); }
    void buildPartA() override { product->setPartA("PartA"); }
    void buildPartB() override { product->setPartB("PartB"); }
    Product* getResult() override { return product; }
};

class Director {
private:
    Builder* builder;
public:
    void setBuilder(Builder* b) { builder = b; }
    void construct() {
        builder->buildPartA();
        builder->buildPartB();
    }
};

int main() {
    Director director;
    ConcreteBuilder builder;
    
    director.setBuilder(&builder);
    director.construct();
    
    Product* product = builder.getResult();
    product->show();
    
    delete product;
    return 0;
}
