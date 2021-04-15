#include <iostream>
#include <cmath>


using namespace std;

double udaljenost_tocke(double x1, double y1, double x2, double y2, double r)
{
    double x;
    x = (x1-x2)*(x1-x2) + (y1-y2)*(y1-y2);
    double d;
    d = sqrt(x);
    double epsilon;
    epsilon = 0.01;
    if (d < r)
    {
        std::cout << "Točka je unutar kružnice, a udaljenost je " <<d<< "." << std::endl;
    }
    else if (r-epsilon < d < r+epsilon)
    {
        std::cout << "Točka se nalazi na kružnici." << std::endl;
    }
    else
    {
        std::cout << "Točka je izvan kružnice, a udaljenost je " <<d<< "." << std::endl;
    }

        
    //std::cout << "Jednadzba pravca: y-"<<y1<< "=" <<k<< "(x-" <<x1<< ")" << std::endl;
    

}
 int main()
 {
    udaljenost_tocke(5,4,3,2,1);
    
    return 0;
    
 }