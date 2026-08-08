#include <iostream>
using namespace std;

// Strategy Interface
class PaymentStrategy
{
public:
    virtual void pay(double amount) = 0;
    virtual ~PaymentStrategy() {}
};

// Concrete Strategy 1: Credit Card
class CreditCardPayment : public PaymentStrategy
{
public:
    void pay(double amount)
    {
        cout << "Paid Rs. " << amount << " using Credit Card." << endl;
    }
};

// Concrete Strategy 2: UPI
class UPIPayment : public PaymentStrategy
{
public:
    void pay(double amount)
    {
        cout << "Paid Rs. " << amount << " using UPI." << endl;
    }
};

// Concrete Strategy 3: PayPal
class PayPalPayment : public PaymentStrategy
{
public:
    void pay(double amount)
    {
        cout << "Paid Rs. " << amount << " using PayPal." << endl;
    }
};

// Context
class PaymentProcessor
{
private:
    PaymentStrategy* strategy;

public:
    PaymentProcessor()
    {
        strategy = nullptr;
    }

    void setPaymentStrategy(PaymentStrategy* newStrategy)
    {
        strategy = newStrategy;
    }

    void processPayment(double amount)
    {
        if (strategy != nullptr)
        {
            strategy->pay(amount);
        }
        else
        {
            cout << "Payment method not selected." << endl;
        }
    }
};

int main()
{
    PaymentProcessor processor;

    CreditCardPayment creditCard;
    UPIPayment upi;
    PayPalPayment paypal;

    cout << "Payment using Credit Card:" << endl;
    processor.setPaymentStrategy(&creditCard);
    processor.processPayment(1500);

    cout << "\nPayment using UPI:" << endl;
    processor.setPaymentStrategy(&upi);
    processor.processPayment(2000);

    cout << "\nPayment using PayPal:" << endl;
    processor.setPaymentStrategy(&paypal);
    processor.processPayment(2500);

    return 0;
}
