// C++ program to print all prime factors
#include <bits/stdc++.h>
#include <math.h>
using namespace std;

typedef vector< tuple<int, int> > primeTuple;

long n = 28; //pow(10, 1500);
primeTuple primeFactors;

// A function to print all prime
// factors of a given number n
void primeFactorsCalc(long n)
{
  int currentBase = 0;
  int currentExp = 0;

	// Print the number of 2s that divide n
	while (n % 2 == 0)
	{
		cout << 2 << " ";
		n = n/2;
	}

	// n must be odd at this point. So we can skip
	// one element (Note i = i +2)
	for (int i = 3; i <= sqrt(n); i = i + 2)
	{
		// While i divides n, print i and divide n
		while (n % i == 0)
		{
			cout << i << " ";
			n = n/i;
		}
	}

  if ( currentBase == 0 )
  {
     currentBase = n;
     cout << "peepoo";
     currentExp += 1;
  }

  if ( currentBase != n )
  {
     primeFactors.push_back( tuple<int, int>(currentBase, currentExp) );
  }

	// This condition is to handle the case when n
	// is a prime number greater than 2
	//if (n > 2)
		//cout << n << " ";
}

/* Driver code */
int main()
{
  cout << "Number is: " << n;
  cout << "\n";
	primeFactorsCalc(n);
  for ( primeTuple::const_iterator i = primeFactors.begin(); i != primeFactors.end(); ++i )
  {
     cout << "(" << get<0>(*i) << ", " << get<1>(*i) << ")" << endl;
  }
	return 0;
}

// This is code is contributed by rathbhupendra
