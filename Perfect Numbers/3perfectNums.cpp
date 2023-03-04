#include <iostream>
#include <cctype>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <immintrin.h>
#include "omp.h"

using namespace std;

long long int n = 2;//pow(10, 1500);
long long int i = 1;
long long int sum = 0;

bool found = 0;

const int CHUNK = 16;
const int NB_THREADS = 8;

int main()
{
  //#pragma omp parallel num_threads(NB_THREADS) private(n, i, sum, found)
  while( !found )
  {
    i = 1;
    sum = 0;

    while( i < n )
    {
      if( n % i == 0 )
      {
         sum = sum + i;
      }
      ++i;
    }

    if( sum == n )
    {
       cout << "\n" << i << " is a PERFECT number!\n";
       if( i % 2 != 0 )
       {
         return 0;
       }
    }
    else
    {
      printf("\r%lld isn't perfect..", n);
      fflush(stdout);
    }

    n += 1;
  }
}
