#include <iostream>
#include <sstream>  
#include <list>
using namespace std;
//zad1
void pravacK(float x1, float y1, float x2, float y2){
    if (x2 != x1){
        float k = (y2 - y1)/(x2 - x1);
        float l = (y2 - y1)/(x2 - x1) * (-1) * x1 + y1;
        std::cout << "y = " << k << "x +"  <<l << std::endl;
    }
    else{
        std::cout << "x = " << x1;
    }
}

//zad2
void kruznica(float p, float q, float r, float x, float y){

    if ((x-p)*(x-p) + (y - q)*(y-q) <= r*r){
        std::cout << "Unutar" << std::endl;
    }
    else{
        std::cout << "Van" << std::endl;
    }
}

//zad3
void interval(int lista[], int i1, int i2, int size){
    if(i1 >= 0 && i2 < size){
        for(int i = i1; i < i2 + 1; i++){
            std::cout << lista[i] <<std::endl;
        }
    }
    else{
        std::cout << "Unijeli ste raspon veći od duljine liste";
    }
    
    
}
//kako returnat listu??
void obrat(int lista[], int size){
    int obrnuta[size];
    for(int i = 0; i < size; i++){
        obrnuta[i] = lista[size - 1 - i];
        //std::cout << i << std::endl;
        //std::cout << obrnuta[i];
    }
    for(int j = 0; j < size; j++){
        lista[j] = obrnuta[j];
    }
}

void zamjena(int lista[], int i1, int i2){
    int temp;
    temp = lista[i2];
    lista[i2] = lista[i1];
    lista[i1] = temp;
}

void sortiranje(int lista[], int size){
    int temp;
    for(int i = 0; i < size; i++){
        for(int j = i+1; j < size; j++){
            if (lista[j] < lista[i]){
                temp = lista[i];
                lista[i] = lista[j];
                lista[j] = temp;

            }
        }
    }
    for(int i = 0; i < size; i++){
        std::cout << lista[i] << " ";
    }
    
}

void sustav(float a1,float b1, float c1, float a2, float b2, float c2){
    float x;
    float y;
    if((a1*b2 - b1*a2) != 0){
        x = (c1*b2 - b1*c2)/(a1*b2 - b1*a2);
        y = (a1*c2 - c1*a2)/(a1*b2 - b1*a2);
        std::cout << "(" << x << "," << y << ")";
    }
    else{
        std::cout << "Nema rješenja.";
    }
    
    
}


int main(){

    pravacK(3, 4, 0, 2);
    

    // kruznica(0, 0, 5, 5, 0);

    // int lista[5] = {1,2,3,4,5};

    // int nesortirana[5] = {5, 7, 2, 33, 1};
    // interval(lista, 1, 4, 5);
    // obrat(lista, 5);
    // zamjena(lista, 2, 3);


    //sortiranje(nesortirana, 5);
    //sustav(2, 3, 2, 2, 3, 7);
    return 0;
}