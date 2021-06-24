#include "blendlib.h"

//using namespace cv;
//using namespace std;




// Blending Options (Multiple Files)
cv::Mat AdditionBlend(std::string filePath1, std::string filePath2) {
	try {
		// Read the image files
		cv::Mat image1 = cv::imread(filePath1);
		cv::Mat image2 = cv::imread(filePath2);

		return image1 + image2;
	}
	catch (...) {
		std::cout << "Addition Blend: There was an error with one of the files." << std::endl;
	}
}

cv::Mat SubtractionBlend(std::string filePath1, std::string filePath2) {
	try {
		// Read the image files
		cv::Mat image1 = cv::imread(filePath1);
		cv::Mat image2 = cv::imread(filePath2);

		return image1 - image2;
	}
	catch (...) {
		std::cout << "Subtraction Blend: There was an error with one of the files." << std::endl;
	}
}

// Function calls for external binding/linkage to Python
extern "C" {
    cv::Mat AdditionBlend_Bound(std::string filePathA, std::string filePathB) {
        return AdditionBlend(filePathA, filePathB);
    }

    cv::Mat SubtractionBlend_Bound(std::string filePathA, std::string filePathB) {
        return SubtractionBlend(filePathA, filePathB);
    }
}

