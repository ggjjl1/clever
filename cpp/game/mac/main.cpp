// 编译命令：g++ main.cpp -o main -I/Library/Frameworks/SDL2.framework/Headers -F/Library/Frameworks -framework SDL2
#include <iostream>
extern "C" {
    #include <SDL2/SDL.h>
}
using namespace std;

const int WIDTH = 400, HEIGHT = 300; // SDL窗口的宽和高
int main() {
    if(SDL_Init(SDL_INIT_EVERYTHING) < 0) {
        cout << "SDL could not initialized with error: " << SDL_GetError() << endl;
    }
    SDL_Window *window = SDL_CreateWindow("A Small Game", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, WIDTH, HEIGHT, SDL_WINDOW_ALLOW_HIGHDPI); // 创建SDL窗口
    if (NULL == window) {
        cout << "SDL could not create window with error: " << SDL_GetError() << endl;
    }

    SDL_Event windowEvent; // SDL窗口事件
    while(true) {
        if (SDL_PollEvent(&windowEvent)) { // 对当前待处理事件进行轮询
            if (SDL_QUIT == windowEvent.type) { // 如果事件为退出，则结束循环
                cout << "SDL quit!!" << endl;
                break;
            }
        }
    }
    SDL_DestroyWindow(window); // 销毁SDL窗体
    SDL_Quit(); // 退出
    return 0;
}