class Particle {
    public:
        double v;
        double theta;
        double x;
        double y; 

        double calculateArea(){   
            return length * breadth;
        }

        double calculateVolume(){   
            return length * breadth * height;
        }

};

#include <iostream>
#include <math.h>
#include <list>


using namespace std;

class Particle {
    public:
        Particle p1
        double v;
        double theta;
        double x;
        double y; 

    private:
        double __move(dt){
            double vx;
            vx=v*cos(theta);
            double vy;
            vy=v*sin(theta);
            float g=9.81;
            x=x + vx*dt;
            vy=vy - g*dt;
            y=y + vy*dt;
        }
    public:
         double range(){
            while (y>=0){
                p1.__move(dt);
                if y <=0:
                    break  
            }
                
            return max(x)
            std::cout << max(x) << std::endl;
         }
        
        
        
        
    int main()
 {
    Particle(1,2,3,4);
    p1.__move(0.5)
    p1.range()

};