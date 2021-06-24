#ifndef BLENDLIB_H_
#define BLENDLIB_H_

//#include <opencv2/opencv.hpp>
#include <iostream>

// Blending Options (Multiple Files)
cv::Mat AdditionBlend(std::string filePath1, std::string filePath2);
cv::Mat SubtractionBlend(std::string filePath1, std::string filePath2);

#endif

