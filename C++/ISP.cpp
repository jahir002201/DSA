#include <iostream>
using namespace std;

// Interface for print functionality
class IPrintable {
public:
    virtual void print() const = 0;
};

// Interface for scan functionality
class IScannable {
public:
    virtual void scan() const = 0;
};

// Class implementing only print functionality
class Printer : public IPrintable {
public:
    void print() const override {
        cout << "Printing document" << endl;
    }
};

// Class implementing both print and scan functionalities
class MultiFunctionPrinter : public IPrintable, public IScannable {
public:
    void print() const override {
        cout << "Printing document" << endl;
    }
    
    void scan() const override {
        cout << "Scanning document" << endl;
    }
};

int main() {
    Printer printer;
    MultiFunctionPrinter mfp;

    printer.print();
    mfp.print();
    mfp.scan();

    return 0;
}
