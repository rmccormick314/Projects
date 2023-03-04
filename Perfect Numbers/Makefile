CC=g++
PARAMS=-std=c++1y
PARAMS_GMP=-std=c++1y -lgmp -lgmpxx
TARGETS=primeFactors 3perfectNums 8perfectNums LucasLehmerTest

all: $(TARGETS)

LucasLehmerTest:
	$(CC) LucasLehmerTest.cpp -o $@ $(PARAMS_GMP)

8perfectNums:
	$(CC) 8perfectNums.cpp -o $@ $(PARAMS)

3perfectNums:
	$(CC) 3perfectNums.cpp -o $@ $(PARAMS)

primeFactors:
	$(CC) primeFactors.cpp -o $@ $(PARAMS)

clean:
	rm $(TARGETS)
