#include <vector>
using namespace std;
class oscilator{

//k, m, t, x0, v0
    private:

    double x, v;
    double dt = 0.01;

    vector<double> listaT;
    vector<double> listaX;
    vector<double> listaV;
    vector<double> listaA;


    void evolve();


    public: 

    oscilator(double k, double m, double x0, double v0, double t);

    double _k, _m, _x0, _v0, _t;

    double x_t();
    double v_t();
    double a_t();

};