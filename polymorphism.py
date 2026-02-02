#include <iostream>
#include <string>
using namespace std;

/* ===== Base Class ===== */
class Employee {
protected:
    string firstName;
    char initial;
    string lastName;

public:
    Employee(string f, char i, string l) {
        firstName = f;
        initial = i;
        lastName = l;
    }

    virtual ~Employee() {}

    // Pure virtual function
    virtual double getMonthlyPay() const = 0;

    string getFullName() const {
        return firstName + " " + initial + ". " + lastName;
    }
};

/* ===== Salary Employee ===== */
class SalaryEmployee : public Employee {
private:
    double monthlySalary;

public:
    SalaryEmployee(string f, char i, string l, double salary)
        : Employee(f, i, l) {
        monthlySalary = salary;
    }

    double getMonthlyPay() const override {
        return monthlySalary;
    }
};

/* ===== Hourly Employee ===== */
class HourlyEmployee : public Employee {
private:
    double hoursWorked;
    double ratePerHour;

public:
    HourlyEmployee(string f, char i, string l, double hours, double rate)
        : Employee(f, i, l) {
        hoursWorked = hours;
        ratePerHour = rate;
    }

    double getMonthlyPay() const override {
        return hoursWorked * ratePerHour;
    }
};

/* ===== Application (Main) ===== */
int main() {
    Employee* employees[2];

    employees[0] = new SalaryEmployee("John", 'A', "Doe", 50000);
    employees[1] = new HourlyEmployee("Mary", 'B', "Smith", 160, 500);

    for (int i = 0; i < 2; i++) {
        cout << "Employee: " << employees[i]->getFullName() << endl;
        cout << "Monthly Pay: " << employees[i]->getMonthlyPay() << endl;
        cout << "-------------------------" << endl;
    }

    for (int i = 0; i < 2; i++) {
        delete employees[i];
    }

    return 0;
}
