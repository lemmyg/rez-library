#include <iostream>
#include <string>
#include <vector>
#include <OpenImageIO/imageio.h>

OIIO_NAMESPACE_USING

// Function to calculate factorial
int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// Function to load and display image information
bool loadImage(const std::string& filename) {
    auto in = ImageInput::open(filename);
    if (!in) {
        std::cerr << "Could not open " << filename << ", error = " << OIIO::geterror() << std::endl;
        return false;
    }

    const ImageSpec &spec = in->spec();
    std::cout << "\nImage Information:" << std::endl;
    std::cout << "Resolution: " << spec.width << "x" << spec.height << std::endl;
    std::cout << "Channels: " << spec.nchannels << std::endl;
    std::cout << "Format: " << spec.format << std::endl;

    // Read the image data
    std::vector<unsigned char> pixels(spec.width * spec.height * spec.nchannels);
    in->read_image(0, 0, 0, spec.nchannels, TypeDesc::UINT8, &pixels[0]);

    in->close();
    return true;
}

int main() {
    // Basic output
    std::cout << "Welcome to the C++ Example Program!" << std::endl;
    
    // Try to load an image
    std::string imagePath = "test.jpg";  // You can change this to your image path
    if (!loadImage(imagePath)) {
        return 1;
    }
    
    return 0;
}
