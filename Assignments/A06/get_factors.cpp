#include <iostream>
#include <fstream>
using namespace std;
int main() {
  int long number;
  int count = 1; 
  while(cin >> number){
    bool isPrime = true;
    if (number == 0 || number == 1) {
      //Number 1: 231697363 - Factors: 419 * 607 * 911
      cout << "Number " << count << " :" << number << " - Factors: " << number << endl;
    }
    else{
      for (int i = 2; i <= number / 2; i++) {
        if (number % i == 0) {
          isPrime = false;
          break;
        }
      }
    }
    //Number 2: 709 - Prime
    if(isPrime == false){
      cout << "Number " << count << " :" << number << " - Factors: ";
      while (number%2 == 0){
        cout<<"2 * ";
        number = number/2;
      }
      for (int i = 3; i <= number; i = i+2){
        if (number%i == 0){
          number = number/i;
          if(number == 1){
            cout << i;
          }
          else{
            cout << i <<" * ";
          }
        }
      }
      cout << endl;
    }
    else{
      cout << "Number " << count << " :" << number << " - Prime \n";
    }
    count++;
  }
}
