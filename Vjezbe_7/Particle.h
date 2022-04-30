#include <cmath>

class Particle{

    private:

    double t, x, y, vx, vy;
    double dt = 0.01;
    double g = -9.81;

    // vy = sin(theta) * v;
    // vx = cos(theta) * v;  

    void evolve();
    
    public: 

    Particle(double v, double theta, double x0, double y0);

    double range();
    double time();

    // double v = v;
    // double theta = theta;
    // double x0 = x0; 
    // double y0 = y0;

    // vy = sin(theta) * v;
    // vx = cos(theta) * v;  

};