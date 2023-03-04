#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

long long int n = 1;
long long int p = 0;
long long int mersenne_num = 0;
long long int perfect_num = 0;

int perfectNumbersFound = 0;

bool isPrime(long long int n)
{
  bool is_prime = true;

  // 0 and 1 are not prime numbers
  if (n == 0 || n == 1) {
    is_prime = false;
  }

  // loop to check if n is prime
  for (long long int i = 2; i <= n/2; ++i) {
    if (n % i == 0) {
      is_prime = false;
      break;
    }
  }

  return is_prime;
}

long long int generateMersenneNum(long long int n)
{
  long long MersenneNum;

  MersenneNum = pow(2, n) - 1;

  return MersenneNum;
}

long long int generatePerfectNum(long long int n)
{
  long long int perfectNum;

  perfectNum = (n * (n + 1))/2;

  return perfectNum;
}

int main()
{
  while( true )
  {
    mersenne_num = generateMersenneNum(n);
    if( isPrime(n) && isPrime(mersenne_num) )
    {
      cout << "\n\n" << mersenne_num << " is a Mersenne Prime!";
      perfect_num = generatePerfectNum(mersenne_num);
      cout << "\n" << perfect_num << " is a Perfect Number!";
      ++perfectNumbersFound;
      cout << "\n" << "==>> "<< perfectNumbersFound << " Perfect Numbers Found!" << " <<==" << "\n\n";
    }
    else
    {
      printf("\rChecking %d...", n);
      fflush(stdout);
    }

    ++n;

    if(n < 0 || mersenne_num < 0 || perfect_num < 0)
    {
      cout << "\n" << "================================\n";
      cout << "\n" << "OVERFLOW: TERMINATING PROGRAM...\n";
      cout << "\n" << "================================\n";
      break;
    }
  }

  return 0;
}
