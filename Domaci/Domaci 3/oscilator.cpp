#include <vector>
#include <iostream>
#include <oscilator.h>
#include <string>
#include <fstream>

using namespace std;

void oscilator::evolve(){
    listaA.push_back(-1 * (_k/_m) * listaX.back());
    listaV.push_back(listaV.back() + listaA.back() * dt);
    listaX.push_back(listaX.back() + listaV.back() * dt); 
}

double oscilator::x_t(){
    for(int i = 0; i < listaT.size(); i++){
        evolve();
    }
    listaX.pop_back();
    listaV.pop_back();
    listaA.pop_back();
    ofstream fwx("C:\\Users\\Korisnik\\Desktop\\New folder\\paf\\Domaci\\Domaci 3\\xt.txt", std::ofstream::out);
    ofstream fwt("C:\\Users\\Korisnik\\Desktop\\New folder\\paf\\Domaci\\Domaci 3\\t.txt", std::ofstream::out);
    ofstream fwv("C:\\Users\\Korisnik\\Desktop\\New folder\\paf\\Domaci\\Domaci 3\\vt.txt", std::ofstream::out);
    ofstream fwa("C:\\Users\\Korisnik\\Desktop\\New folder\\paf\\Domaci\\Domaci 3\\at.txt", std::ofstream::out);
    if (fwx.is_open()){
        for (auto & i : listaX){
            fwx << i << "\n";
        }
        fwx.close();
    }
    else cout << "Greška";

    if (fwt.is_open()){
        for (auto & i : listaT){
            fwt << i << "\n";
        }
        fwt.close();
    }
    else cout << "Greška";

    if (fwv.is_open()){
        for (auto & i : listaV){
            fwv << i << "\n";
        }
        fwv.close();
    }
    else cout << "Greška";

    if (fwa.is_open()){
        for (auto & i : listaA){
            fwa << i << "\n";
        }
        fwa.close();
    }
    else cout << "Greška";
    return 0;
}

oscilator::oscilator(double k, double m, double x0, double v0, double t){
    _k = k;
    _m = m;
    _x0 = x0;
    _v0 = v0;
    _t = t;


    listaA.push_back(-_k/_m * _x0);
    listaV.push_back(_v0);
    listaX.push_back(_x0);

    listaT.push_back(0.);
    int brojac = 0;
    int n = listaT.size();
    while(listaT[n - 1] < t){
        brojac += 1;
        n = listaT.size();
        listaT.push_back(brojac * dt);

    }
}