#include <iostream>
#include <string>
using namespace std;

class Calculator{
    public:
    void addition(){
        int add_number_1;
        int add_number_2;
        cout << "Please Enter Your First Number: ";
        cin >> add_number_1;
        cout << "Please Enter Your Second Number: ";
        cin >> add_number_2;
        int sum = add_number_1 + add_number_2;
        cout << sum << endl;
    };

    void subtraction(){
        int sub_number_1;
        int sub_number_2;
        cout << "Please Enter Your First Number: ";
        cin >> sub_number_1;
        cout << "Please Enter Your Second Number: ";
        cin >> sub_number_2;
        int sum = sub_number_1 - sub_number_2;
        cout << sum << endl;
    };

    void multiplication(){
        int mult_number_1;
        int mult_number_2;
        cout << "Please Enter Your First Number: ";
        cin >> mult_number_1;
        cout << "Please Enter Your Second Number: ";
        cin >> mult_number_2;
        int sum = mult_number_1 * mult_number_2;
        cout << sum << endl;
    };

    void division(){
        int div_number_1;
        int div_number_2;
        cout << "Please Enter Your First Number: ";
        cin >> div_number_1;
        cout << "Please Enter Your Second Number: ";
        cin >> div_number_2;
        int sum = div_number_1 / div_number_2;
        cout << sum << endl;
    };
};

int main(){
    Calculator Calc_obj;
    char answer;
    char operation;
    cout << "What would you like to do(+,-,*,/)" << endl;
    cin >> operation;
    switch(operation){
        case '+':
        Calc_obj.addition();
        break;
        case '-':
        Calc_obj.subtraction();
        break;
        case '*':
        Calc_obj.multiplication();
        break;
        case '/':
        Calc_obj.division();
        break;
        default:
        cout << "You didn't use any of the above operations please try again." << endl << ":(";
    };
    cout << "Would you like to close the program?(y/n)" << endl;
    cin >> answer;
    if(answer == 'y'){
        cout << "Congrats on your first program ASH";
        return 0;
    }
    else{
        cout << "Congrats on your first program ASH";
        return 0;
    };
};