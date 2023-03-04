#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include "gmp.h"
#include <gmpxx.h>
#include <iomanip>
#include <cmath>

using namespace std;

mpz_class n = 1;
mpz_class p = 0;
mpz_class mersenne_num = 0;
mpz_class perfect_num = 0;

int perfectNumbersFound = 0;
mpz_class lastDigit = 0;

mpz_class generateMersenneNum(mpz_class n)
{
  mpz_class MersenneNum = 0;

  mpz_ui_pow_ui(MersenneNum.get_mpz_t(), 2, n.get_ui());
  mpz_sub_ui(MersenneNum.get_mpz_t(), MersenneNum.get_mpz_t(), 1);

  return MersenneNum;
}

bool isPrimeLL(mpz_class p)
{
  if(p == 2)
  {
    return true;
  }

  // generate the number
  mpz_class checkNumber = generateMersenneNum(p);

  // First number of the series
  mpz_class nextval = 4 % checkNumber;

  // Generate the rest (p-2) terms
  // of the series.
  for (int i = 1; i < p - 1; i++)
    nextval = (nextval * nextval - 2) % checkNumber;

  // now if the (p-1)th term is
  // 0 return true else false.
  return (nextval == 0);
}

bool isPrime(mpz_class n)
{
  bool is_prime = true;

  // 0 and 1 are not prime numbers
  if (n == 0 || n == 1) {
    return false;
  }

  if (n == 2)
  {
    return true;
  }


  mpz_class i = 2;

  while ( i < n )
  {
    if (n % i == 0)
    {
      return false;
    }

    ++i;
  }

  return is_prime;
}

mpz_class generatePerfectNum(mpz_class n)
{
  mpz_class perfectNum;

  perfectNum = (n * (n + 1))/2;

  return perfectNum;
}

int main()
{
  while( true )
  {
    //mersenne_num = generateMersenneNum(n);

    if( isPrime(n) && isPrimeLL(n) )
    {
      cout << "\n\n (2^" << n << " - 1)"<< " is a Mersenne Prime!";
      //perfect_num = generatePerfectNum(mersenne_num);
      //cout << "\n" << perfect_num << " is a Perfect Number!";
      ++perfectNumbersFound;
      cout << "\n" << "==>> "<< perfectNumbersFound << " Perfect Numbers Found!" << " <<==" << "\n\n";
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
