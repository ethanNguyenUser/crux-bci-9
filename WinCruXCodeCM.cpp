//Windows, takes input of actual computer cursor
#include <iostream>
#include <Windows.h>

void getMousePosition(int& x, int& y) {
    POINT cursorPos;
    if (GetCursorPos(&cursorPos)) {
        x = cursorPos.x;
        y = cursorPos.y;
    } else {
        std::cerr << "Failed to retrieve mouse position." << std::endl;
    }
}

int main() {
    int x, y;
    bool notMoving = true;

    while (notMoving) {
        getMousePosition(x, y);

        // Check if cursor is on the left side
        if (x < 0.2 * GetSystemMetrics(SM_CXSCREEN)) {
            std::cout << "Left" << std::endl;
        }
        // Check if cursor is on the right side
        else if (x > 0.8 * GetSystemMetrics(SM_CXSCREEN)) {
            std::cout << "Right" << std::endl;
        }
        // Check if cursor is on the top side
        else if (y < 0.2 * GetSystemMetrics(SM_CYSCREEN)) {
            std::cout << "Up" << std::endl;
        }
        // Check if cursor is on the bottom side
        else if (y > 0.8 * GetSystemMetrics(SM_CYSCREEN)) {
            std::cout << "Down" << std::endl;
        }
        // Cursor is in none of the areas
        else {
            notMoving = true;
        }

        // Add some delay to avoid excessive looping
        Sleep(100);
    }

    return 0;
}
