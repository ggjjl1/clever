// 依赖 SDL2.dll 动态库
// windows下一个SDL2小程序，编译命令：g++ -std=c++14 main.cpp -o main -IC:\msys64\mingw64\include -LC:\msys64\mingw64\lib -lSDL2main -lSDL2
#include <iostream>
extern "C" {
    #include <SDL2/SDL.h>
}
using namespace std;

const int WIDTH = 400, HEIGHT = 300; // SDL窗口宽和高
int WinMain() {
    if (SDL_Init(SDL_INIT_EVERYTHING) < 0) {
        cout << "Cound not initialize SDL!" << SDL_GetError() << endl;
    }
    SDL_Window *window = SDL_CreateWindow("A Simple Game", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WIDTH, HEIGHT, SDL_WINDOW_ALLOW_HIGHDPI); // 创建SDL窗口
    if (NULL == window) {
        cout << "SDL counld not create window with error: " << SDL_GetError() << endl;
    }

    SDL_Event windowEvent; // SDL窗口事件
    while(true) {
        if(SDL_PollEvent(&windowEvent)) { // 对当前待处理时间进行轮询
            if(SDL_QUIT == windowEvent.type) { // 如果为退出时间，则结束循环
                cout << "SDL Quit!" << endl;
                break;
            }
        }
    }
    SDL_DestroyWindow(window); // 退出SDL窗体
    SDL_Quit(); // 退出

    return 0;
}