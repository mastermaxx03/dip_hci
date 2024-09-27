Local Binary Pattern
There are lots of different types of texture descriptors are used to extract features of an image. Local Binary Pattern, also known as LBP, is a simple and grayscale invariant texture descriptor measure for classification. In LBP, a binary code is generated at each pixel by thresholding it’s neighbourhood pixels to either 0 or 1 based on the value of the centre pixel. The rule for finding LBP of an image is as follows:

Set a pixel value as center pixel.
1.Collect its neighbourhood pixels (Here I am taking a 3 x 3 matrix so; total number of neighbourhood pixel is 8)
Threshold it’s neighbourhood pixel value to 1 if its value is greater than or equal to centre pixel value otherwise threshold it to 0.
2.After thresholding, collect all threshold values from neighbourhood either clockwise or anti-clockwise.
3.The collection will give you an 8-digit binary code. Convert the binary code into decimal.
4.Replace the center pixel value with resulted decimal and do the same process for all pixel values present in image.
