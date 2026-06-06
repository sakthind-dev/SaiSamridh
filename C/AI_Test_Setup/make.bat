del *gcda *.gcno *.html
gcc --version
gcov --version
g++ --version

gcc -v math1.c -o math1.exe
math1.exe
gcc -g -fprofile-arcs -ftest-coverage test_math1.c math1.c unity.c -o test_math1.exe
.\test_math1.exe
dir *.gcno *.gcda
gcov math1.c
gcov test_math1.c
gcov -o . math1.c

::OpenCppCoverage.exe --sources . -- test_math1.exe
::OpenCppCoverage.exe --sources Learnings\SaiSamridh\C -- test_math1.exe
::OpenCppCoverage.exe --sources earnings\SaiSamridh\C --modules SaiSamridh\C -- test_math1.exe
::OpenCppCoverage.exe --sources . -- test_math1.exe

gcc -g -fprofile-arcs -ftest-coverage test_math1.c math1.c unity.c -o test_math1.exe
.\test_math1.exe
OpenCppCoverage.exe --sources Learnings\SaiSamridh\C --modules Learnings\SaiSamridh\C -- test_math1.exe


:: Python312\site-packages\gcovr\coverage.py -r . --html --html-details -o coverage.html

python -m gcovr =v -r . --html --html-details -o coverage.html
