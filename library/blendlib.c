#include <stdio.h>

#define PIXEL_MIN 0
#define PIXEL_MAX 255

// Helper functions to control minimum and maximum pixel values
int Minimum(int input1, int input2) {
    return input1 < input2 ? input1 : input2;
}

int Maximum(int input1, int input2) {
    return input1 > input2 ? input1 : input2;
}

// Blending functions for multiple images
void AdditionBlend(int size, __uint8_t* image1, __uint8_t* image2, __uint8_t* result) {
    for (int i = 0; i < size; i++) {
        result[i] = Minimum(image1[i] + image2[i], PIXEL_MAX);
    }
}

void SubtractionBlend(int size, __uint8_t* image1, __uint8_t* image2, __uint8_t* result) {
    for (int i = 0; i < size; i++) {
        result[i] = Maximum(image1[i] - image2[i], PIXEL_MIN);
    }
}

void MultiplicationBlend(int size, __uint8_t* image1, __uint8_t* image2, __uint8_t* result) {
    for (int i = 0; i < size; i++) {
        result[i] = (image1[i] * image2[i] / PIXEL_MAX) + 0.5f;
    }
}

void ScreenBlend(int size, __uint8_t* image1, __uint8_t* image2, __uint8_t* result) {
    // TODO
}

void OverlayBlend(int size, __uint8_t* image1, __uint8_t* image2, __uint8_t* result) {
    for (int i = 0; i < size; i++) {
        if (image2[i] / PIXEL_MAX <= 0.5f) {
            result[i] = (2 * (image1[i] * image2[i] / PIXEL_MAX)) + 0.5f;
        }
        else {
            result[i] = ((PIXEL_MAX - (2 * (PIXEL_MAX - image1[i]) * (PIXEL_MAX - image2[i])))) + 0.5f;
            //result[i] = ((1 - (2 * (1 - (image1[i] / PIXEL_MAX)) * (1 - (image2[i] / PIXEL_MAX)))) * PIXEL_MAX) + 0.5f;
        }
    }
}

void LightenBlend(int size, __uint8_t* image1, __uint8_t* image2, __uint8_t* result) {
    for (int i = 0; i < size; i++) {
        //get lighter of two colors (higher value is lighter)
        result[i] = Maximum(image1[i], image2[i]);
    }
}

void DarkenBlend(int size, __uint8_t* image1, __uint8_t* image2, __uint8_t* result) {
    for (int i = 0; i < size; i++) {
        //get darker of two colors (lower value is darker)
        result[i] = Minimum(image1[i], image2[i]);
    }
}

void ColorDodgeBlend(int size, __uint8_t* image1, __uint8_t* image2, __uint8_t* result) {
    for (int i = 0; i < size; i++) {
        // Check for potential zero division
        if (image1[i] != PIXEL_MAX) {
            result[i] = ((image2[i] / (PIXEL_MAX - image1[i])) * PIXEL_MAX) + 0.5f;
        }
        else {
            result[i] = PIXEL_MAX;
        }
    }
}

void ColorBurnBlend(int size, __uint8_t* image1, __uint8_t* image2, __uint8_t* result) {
    for (int i = 0; i < size; i++) {
        // Check for potential zero division
        if (image1[i] != PIXEL_MIN) {
            result[i] = (PIXEL_MAX - ((PIXEL_MAX - image2[i]) / image1[i])) + 0.5f;
        }
        else {
            result[i] = PIXEL_MIN;
        }
    }
}