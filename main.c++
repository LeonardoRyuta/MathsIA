#include <iostream>
#include <fstream>
using namespace std;

int main() {
    float valuesArray[3] = {0.00, 0.00, 2.20}; //n, t, d
    float dvdt = -9.81;
    float h = 0.00001;
    int counter = 0;

    ofstream MyFile("filename.txt");

    while (true) {
        if (counter == 100001) break;
        float n = valuesArray[0];
        float t = valuesArray[1];
        float d = valuesArray[2];
        
        valuesArray[0] = n++;
        valuesArray[1] = t + h;
        valuesArray[2] = d + h * (dvdt * t);

        MyFile << valuesArray[0] << " " << valuesArray[1] << " " << valuesArray[2] << endl;

        counter++;

        if (valuesArray[2] < 0) break;
    }

    MyFile.close();

    return 0;
}