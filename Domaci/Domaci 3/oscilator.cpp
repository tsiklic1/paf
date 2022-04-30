#include <vector>
#include <iostream>
#include <oscilator.h>

using namespace std;

void oscilator::evolve(){
    // listaA.push_back(-k/m * listaX[listaX.size() - 1]);
    // listaV.push_back(listaV[listaV.size() - 1] + listaA[listaA.size() - 1] * dt);
    // listaX.push_back(listaX[listaX.size() - 1] + listaV[listaV.size() - 1] * dt);

    cout << listaA.back()<< endl;
    cout << listaV.back()<< endl;
    cout << listaX.back()<< endl;
    listaA.push_back(-1 * (k/m) * listaX.back());
    listaV.push_back(listaV.back() + listaA.back() * dt);
    listaX.push_back(listaX.back() + listaV.back() * dt);
    //cout << listaV.back() + listaA.back() * dt << " ";
    
}

double oscilator::x_t(){
    for(int i = 0; i < listaT.size(); i++){
        evolve();
    }
    // for(auto & i : listaA){
    //     cout << i << " ";
    // }
    return 0;
}

oscilator::oscilator(double k, double m, double x0, double v0, double t){
    k = k;
    m = m;
    x0 = x0;
    v0 = v0;
    t = t;

    listaA.push_back(-k/m * x0);
    listaV.push_back(v0);
    listaX.push_back(x0);

    listaT.push_back(0.);
    int brojac = 0;
    int n = listaT.size();
    while(listaT[n - 1] < t){
        brojac += 1;
        n = listaT.size();
        listaT.push_back(brojac * dt);

    }
}