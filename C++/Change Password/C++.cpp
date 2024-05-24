#include <iostream>
#include <string>
using namespace std;

class Password{
    public:;
    protected:
        string password = "toto12345";
    ;
};

class change_password:public Password{
    public:
    string old_password;
    string new_password;
    string repeat_new_password;
    void function(){
        cout << "Old Password:";
        cin >> old_password;
        cout << "New Password:";
        cin >> new_password;
        cout << "Repeat Password:";
        cin >> repeat_new_password;
        if(old_password == password){
            password = new_password;
            cout << "Alright" <<endl <<"Your New Password Is " << password;
        }
        else{
            cout << "Oops!Something went wrong.Please Try again.";
        };
    };
};

int main(){
    Password Class1;
    change_password Class2;
    cout << "Change Your Password" << endl;
    Class2.function();
    return 0;
};