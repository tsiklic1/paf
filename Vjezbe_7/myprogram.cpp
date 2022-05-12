#include <iostream>
#include <Particle.h>

int main(){
    Particle p1(10, 0.1, 0, 0);
    p1.range();
    p1.time();

    Particle p2(3, 0.7, 2, 2);
    p2.range();
    p2.time();
    return 0;
}