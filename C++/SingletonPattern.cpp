#include <iostream>
using namespace std;

class Singleton {
private:
    static Singleton* instance;
    Singleton() {}  // Private constructor
public:
    static Singleton* getInstance() {
        if (!instance)
            instance = new Singleton();
        return instance;
    }
    void showMessage() { cout << "Singleton Instance" << endl; }
};

Singleton* Singleton::instance = nullptr;

int main() {
    Singleton* singleton = Singleton::getInstance();
    singleton->showMessage();
    return 0;
}
