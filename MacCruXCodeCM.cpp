//Mac, takes input of actual computer cursor
#include <iostream>
#include <CoreGraphics/CoreGraphics.h>

void getMousePosition(int& x, int& y) {
    CGEventRef event = CGEventCreate(NULL);
    CGPoint cursor = CGEventGetLocation(event);
    CFRelease(event);
    
    x = static_cast<int>(cursor.x);
    y = static_cast<int>(cursor.y);
}

int main() {
    int x, y;
    bool notMoving = true;

    while (notMoving) {
        getMousePosition(x, y);

        // Check if cursor is on the left side
        if (x < 0.2 * CGDisplayPixelsWide(CGMainDisplayID())) {
            std::cout << "Left" << std::endl;
        }
        // Check if cursor is on the right side
        else if (x > 0.8 * CGDisplayPixelsWide(CGMainDisplayID())) {
            std::cout << "Right" << std::endl;
        }
        // Check if cursor is on the top side
        else if (y < 0.2 * CGDisplayPixelsHigh(CGMainDisplayID())) {
            std::cout << "Up" << std::endl;
        }
        // Check if cursor is on the bottom side
        else if (y > 0.8 * CGDisplayPixelsHigh(CGMainDisplayID())) {
            std::cout << "Down" << std::endl;
        }
        // Cursor is in none of the areas
        else {
            notMoving = true;
        }

        // Add some delay to avoid excessive looping
        usleep(100000);
    }

    return 0;
}
