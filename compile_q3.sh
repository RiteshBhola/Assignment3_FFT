#make changes according to path of your GSL library
echo "### Change path of gsl library before compiling and remove this comment ###"
gcc -Wall -I/home/ritesh/gsl/include -c q3.c
gcc -L/home/ritesh/gsl/lib q3.o -lgsl -lgslcblas -lm -o fftgsl.out
./fftgsl.out
python3 plotq3.py
