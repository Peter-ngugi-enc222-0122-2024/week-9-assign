#include <iostream>
#include "SalaryEmployee.h"
#include "HourlyEmployee.h"
using namespace std;

int main() {
    Employee* employees[2];

    employees[0] = new SalaryEmployee("John", 'A', "ngn", 50000);
    employees[1] = new HourlyEmployee("Mary", 'B', "wairim", 160, 500);

    for (int i = 0; i < 2; i++) {
        cout << "Employee: " << employees[i]->getFullName() << endl;
        cout << "Monthly Pay: " << employees[i]->getMonthlyPay() << endl;
        cout << "--------------------------" << endl;
    }

    for (int i = 0; i < 2; i++) {
        delete employees[i];
    }

    return 0;
}
