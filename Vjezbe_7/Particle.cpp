#include <iostream>
#include <math.h>
#include <Particle>

Particle::Particle(double v_, double theta_, double x_, double y_){
            double pi = 3.14159265359;
            v = v_;
            theta = theta_ * (pi/180) ;
            x = x_;
            y = y_;
            vx=v*cos(theta);
            vy=v*sin(theta);
        }

double Particle:: __move(double dt){
        float g=9.81;
        x=x + vx*dt;
        vy=vy - g*dt;
        y=y + vy*dt;
        }
 
double Particle::range(double dt){
        do {
             __move(dt);
                
        }
        while (y>=0);

double Particle::time(double dt){
        double t;
        t=0;
        while (y>=0);
        float g=9.81;
        x=x + vx*dt;
        vy=vy - g*dt;
        y=y + vy*dt;
        t=t+dt;
        }
};