#include <iostream>

using namespace std;

class Box
{
    public:
        double length;
        double width;
        double height;

        double get_volume(void);
        void set_volume(double len, double wid, double hei);
};

double Box::get_volume(void)
{
    return length * width * height;
}

void Box::set_volume(double len, double wid, double hei)
{
    length = len;
    width = wid;
    height = hei;
}

int main() {
    Box box1;
    Box box2;
    Box box3;
    double volume = 0.0;

    box1.length = 5.0;
    box1.width = 6.0;
    box1.height = 7.0;

    box2.length = 10.0;
    box2.width = 12.0;
    box2.height = 13.0;

    volume = box1.length * box1.width * box1.height;
    cout << "box1体积：" << volume << endl;

    volume = box2.length * box2.width * box2.height;
    cout << "box2体积：" << volume << endl;

    box3.set_volume(16.0, 8.0, 12.0);
    volume = box3.get_volume();
    cout << "box3体积：" << volume << endl;
    return 0;
}