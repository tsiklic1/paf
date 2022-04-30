#include <Particle.h>
#include <math.h>
#include <cmath>
#include <iostream>

void Particle::evolve(){
    vy += g * dt;
    x += vx * dt;
    y += vy * dt;
    t += dt;

}

double Particle::range(){
    while(y >= 0){
        evolve();
    }
    std::cout << x << std::endl;
    return x;
}

double Particle::time(){
    while(y >= 0){
        evolve();
    }
    std::cout << t << std::endl;
    return t;
}

Particle::Particle(double v, double theta, double x0, double y0)
{
    t = 0;

    v = v;
    theta = theta;
    x = x0; 
    y = y0;

    vy = sin(theta) * v;
    vx = cos(theta) * v;  
}