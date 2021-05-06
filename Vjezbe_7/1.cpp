#include <iostream>
#include <math.h>
#include <list>


using namespace std;

class Particle 
{
    public:
        double v;
        double theta;
        double x;
        double y;
        double vy;
        double vx;
        Particle(double v_, double theta_, double x_, double y_){
            double pi = 3.14159265359;
            v = v_;
            theta = theta_ * (pi/180) ;
            x = x_;
            y = y_;
            vx=v*cos(theta);
            vy=v*sin(theta);
        }

    private:
        double __move(double dt){
            
            float g=9.81;
            x=x + vx*dt;
            vy=vy - g*dt;
            y=y + vy*dt;
            std::cout << vy <<  " " << y << std::endl;
        }
    public:
         double range(double dt){
            do {
                 __move(dt);
                
            }
            while (y>=0);
            
            std::cout << x << std::endl;
            }
};
        
        
        
        
int main()
{
    Particle p1(10,60,0,0);
    //p1.__move(0.5);  
    p1.range(0.01);    

    return 0;  
}