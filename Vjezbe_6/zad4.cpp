#include <iostream>

using namespace std;

void sustjedz(int a1,int a2,int b1,int b2,int c1,int c2)
{
    //a1x+b1y=c1
    //a2x+b2y=c2
    int y;
    y=a1*c2-a2*c1-b2*a1+a2*b1;
    int x;
    x=(c1-b1*y)/a1;
    std::cout << "y= "<<y<< " x= " <<x<< std::endl;
    

}
 int main()
 {
    sustjedz(1,1,1,1,1,1);
    
 }