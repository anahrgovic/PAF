#include <iostream>
#include <cmath>


using namespace std;

void lineEquation(double x1, double y1, double x2, double y2)
{
    double k;
    k = (y2-y1)/(x2-x1);
    std::cout << "Jednadzba pravca: y-"<<y1<< "=" <<k<< "(x-" <<x1<< ")" << std::endl;
    

}
 int main()
 {
    lineEquation(1,2,3,4);
    
 }