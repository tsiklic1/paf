#include <iostream>
#include <sstream>  
#include <list>
using namespace std;
//zad1
void pravacK(float x1, float y1, float x2, float y2){
    float k = (y2 - y1)/(x2 - x1);

    
    float l = (y2 - y1)/(x2 - x1) * (-1) * x1 + y1;
    std::cout << "y = " << k << "x +"  <<l << std::endl;
}

//zad2
void kruznica(float p, float q, float r, float x, float y){

    if ((x-p)*(x-p) + (y - q)*(y-q) < r*r){
        std::cout << "Unutar" << std::endl;
    }
    else{
        std::cout << "Van" << std::endl;
    }
}

//zad3
void interval(int lista[], int i1, int i2){
    for(int i = i1; i < i2 + 1; i++){
        std::cout << lista[i] <<std::endl;
    }
    
}
//kako returnat listu??
void obrat(int lista[], int size){
    int obrnuta[size];
    for(int i = 0; i < size; i++){
        obrnuta[i] = lista[size - 1 - i];
        //std::cout << i << std::endl;
        std::cout << obrnuta[i];
    }
}

void zamjena(int lista[], int i1, int i2){
    int temp;
    temp = lista[i2];
    lista[i2] = lista[i1];
    lista[i1] = temp;
}

int main(){

    //pravacK(3.2, 3, 5, 4.2);
    

    //kruznica(0, 0, 5, 2, 1);

    int lista[5] = {1,2,3,4,5};
    //interval(lista, 1, 3);
    //obrat(lista, 5);
    zamjena(lista, 2, 3);
    for(int i = 0; i < 5; i++){
        std::cout << lista[i];
    }
    return 0;
}