#include <iostream>
using namespace std;
int a[] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000 };
int middleSquareNumber(int number, int digit) {
   int sqn = number * number, next_number = 0;
   int t = (digit / 2);
   sqn = sqn / a[t];
   for (int i = 0; i < digit; i++) {
      next_number += (sqn % (a[t])) * (a[i]);
      sqn = sqn / 10;
   }
   return next_number;
}
int main() {
   cout << "Enter the digit random numbers you want: ";
   int n;
   cin >> n;
   int start = 1;
   int end = 1;
   start = a[n - 1];
   end = a[n];
   int number = ((rand()) % (end - start)) + start;
   cout << "The random numbers are:\n" << number << ", ";
   for (int i = 1; i < n; i++) {
      number = middleSquareNumber(number, n);
      cout << number << ", ";
   }
   cout << ".........";
}
