#include <iostream>
using namespace std;

// Abstraction for payment methods
class PaymentMethod {
public:
    virtual void processPayment(double amount) const = 0;
};

// Concrete implementation of credit card payment
class CreditCardPayment : public PaymentMethod {
public:
    void processPayment(double amount) const override {
        cout << "Processing credit card payment of " << amount << endl;
    }
};

// Concrete implementation of PayPal payment
class PayPalPayment : public PaymentMethod {
public:
    void processPayment(double amount) const override {
        cout << "Processing PayPal payment of " << amount << endl;
    }
};

// High-level module depending on abstraction
class ShoppingCart {
private:
    const PaymentMethod& paymentMethod;
public:
    ShoppingCart(const PaymentMethod& method) : paymentMethod(method) {}
    
    void checkout(double amount) const {
        paymentMethod.processPayment(amount);
    }
};

int main() {
    CreditCardPayment creditCard;
    PayPalPayment payPal;

    ShoppingCart cart1(creditCard);
    ShoppingCart cart2(payPal);

    cart1.checkout(100.0);
    cart2.checkout(200.0);

    return 0;
}
