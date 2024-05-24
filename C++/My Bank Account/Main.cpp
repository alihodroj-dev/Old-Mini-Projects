#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int sum;
int new_sum;
int added_number;

int main() {
    cout << "Number To Add: ";
    cin >> added_number;
    ifstream sum_file;
    sum_file.open("sum_file.txt");
    sum_file >> sum;
    new_sum = sum + added_number;
    ofstream new_sum_file;
    new_sum_file.open("sum_file.txt");
    new_sum_file << new_sum;
    cout << "Your cuurent value is " << new_sum;
}