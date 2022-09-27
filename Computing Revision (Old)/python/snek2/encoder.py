import cv2

# Input image
input = cv2.imread('imageTwo.png')
input = cv2.resize(input, (200,200))
# Get input size
height, width = input.shape[:2]

# Desired "pixelated" size
w, h = (16, 16)

# Resize input to "pixelated" size
temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize output image
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)

cv2_imshow(input)
cv2_imshow(output)