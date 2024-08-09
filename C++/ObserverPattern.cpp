#include <iostream>
#include <vector>
using namespace std;

class Observer {
public:
    virtual void update(int state) = 0;
};

class Subject {
private:
    vector<Observer*> observers;
    int state;
public:
    void attach(Observer* observer) { observers.push_back(observer); }
    void setState(int newState) {
        state = newState;
        notify();
    }
    int getState() const { return state; }
    
    void notify() {
        for (Observer* observer : observers) {
            observer->update(state);
        }
    }
};

class ConcreteObserver : public Observer {
private:
    Subject* subject;
public:
    ConcreteObserver(Subject* subj) : subject(subj) {
        subject->attach(this);
    }
    void update(int state) override {
        cout << "Observer: State updated to " << state << endl;
    }
};

int main() {
    Subject subj;
    ConcreteObserver obs1(&subj);
    ConcreteObserver obs2(&subj);

    subj.setState(10);
    subj.setState(20);

    return 0;
}
