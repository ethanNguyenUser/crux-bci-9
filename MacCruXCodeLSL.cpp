//Mac, takes input of LSL stream
#include <iostream>
#include <lsl_cpp.h>

void getMousePosition(int& x, int& y) {
    // Create a resolver to find the desired stream on the network
    lsl::stream_info info;
    try {
        lsl::resolve_stream("type", "mouse_position", 1, 5.0f, &info); // Modify the type and name as per your BCI2000 stream configuration
    } catch (std::exception& e) {
        std::cerr << "Failed to resolve the LSL stream: " << e.what() << std::endl;
        return;
    }

    // Create an inlet to read the data from the stream
    lsl::stream_inlet inlet(info);

    // Receive the data sample
    std::vector<float> sample;
    try {
        inlet.pull_sample(sample);
    } catch (std::exception& e) {
        std::cerr << "Failed to read data from the LSL stream: " << e.what() << std::endl;
        return;
    }

    // Extract the X and Y coordinates from the sample
    if (sample.size() >= 2) {
        x = static_cast<int>(sample[0]);
        y = static_cast<int>(sample[1]);
    } else {
        std::cerr << "Invalid sample size. Expected at least 2 values." << std::endl;
        return;
    }
}

int main() {
    int x, y;

    // Continuous tracking loop
    while (true) {
        getMousePosition(x, y);

        // Process the cursor position
        // ...
        // Your code here to determine the output based on the cursor position

        // Add some delay to avoid excessive looping
        usleep(100000);
    }

    return 0;
}
