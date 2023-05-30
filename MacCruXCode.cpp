//Mac, takes input of cursor coordinates
#include <iostream>
#include <thread>
#include <chrono>
#include <CoreGraphics/CoreGraphics.h>

// Constants for the screen size
const int SCREEN_WIDTH = 1920;   // Width of the screen
const int SCREEN_HEIGHT = 1080;  // Height of the screen

// Constants for the areas
const int LEFT_AREA_WIDTH = 200;     // Width of the left area
const int LEFT_AREA_HEIGHT = 1080;   // Height of the left area

const int RIGHT_AREA_X = 1720;       // X-coordinate of the right area
const int RIGHT_AREA_WIDTH = 200;    // Width of the right area
const int RIGHT_AREA_HEIGHT = 1080;  // Height of the right area

const int TOP_AREA_HEIGHT = 100;     // Height of the top area
const int BOTTOM_AREA_Y = 980;       // Y-coordinate of the bottom area
const int BOTTOM_AREA_HEIGHT = 100;  // Height of the bottom area

// Function to get the current mouse position
void getMousePosition(int& x, int& y)
{
    CGEventRef event = CGEventCreate(nullptr);
    CGPoint cursor = CGEventGetLocation(event);
    CFRelease(event);

    x = static_cast<int>(cursor.x);
    y = static_cast<int>(cursor.y);
}

int main()
{
    int x, y;
    bool notMoving = true;

    while (true)
    {
        getMousePosition(x, y);

        // Check if the cursor is in the left area
        if (x >= 0 && x < LEFT_AREA_WIDTH && y >= 0 && y < LEFT_AREA_HEIGHT)
        {
            std::cout << "left" << std::endl;
            notMoving = false;
        }
        // Check if the cursor is in the right area
        else if (x >= RIGHT_AREA_X && x < SCREEN_WIDTH && y >= 0 && y < RIGHT_AREA_HEIGHT)
        {
            std::cout << "right" << std::endl;
            notMoving = false;
        }
        // Check if the cursor is in the top area
        else if (y >= 0 && y < TOP_AREA_HEIGHT)
        {
            std::cout << "up" << std::endl;
            notMoving = false;
        }
        // Check if the cursor is in the bottom area
        else if (y >= BOTTOM_AREA_Y && y < SCREEN_HEIGHT)
        {
            std::cout << "down" << std::endl;
            notMoving = false;
        }

        if (notMoving)
        {
            std::cout << "Not moving" << std::endl;
        }

        notMoving = true;

        // Wait for a small duration before checking the mouse position again
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    return 0;
}
