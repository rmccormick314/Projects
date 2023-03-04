CC=g++
PARAMS=-std=c++1y
TARGETS=primeFactors 3perfectNums 8perfectNums

all: $(TARGETS)

8perfectNums:
	$(CC) 8perfectNums.cpp -o $@ $(PARAMS)

3perfectNums:
	$(CC) 3perfectNums.cpp -o $@ $(PARAMS)

primeFactors:
	$(CC) primeFactors.cpp -o $@ $(PARAMS)

clean:
	rm $(TARGETS)
