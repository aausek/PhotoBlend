'''
#########################################
##### BELOW IS FOR TESTING PURPOSES #####
#########################################


# Open images/get dimensions
img1 = Image.open('car.jpg')
width1, height1 = img1.size
img2 = Image.open('layer2.jpg')
width2, height2 = img2.size

# Create blank image object with same dimensions
img3 = Image.new(mode = "RGB", size = (width1, height1))

# Convert the images to a 1-D numpy array
image1 = np.asarray(img1).flatten()
image2 = np.asarray(img2).flatten()
image3 = np.asarray(img3).flatten()

size = image1.size

# Image details
print("Flat image Details:")
print("-------------------")
print(f"Dimensions: {image1.ndim}")
print(f"Shape: {image1.shape}")
print(f"Data Type: {image1.dtype}")
print(f"Object type: {type(image1)}")
print(f"CTypes: {image1.ctypes}\n")

# Testing the call to C
print("Testing Addition Blend call...\n")
addition_blend(size, image1, image2, image3)

# Change resulting image back to 3-D array
new_image = np.reshape(image3, (width1, height1, 3))
result = Image.fromarray(new_image, 'RGB')
result.save('test_image.jpg', 'JPEG')

print("New image loaded.")

'''