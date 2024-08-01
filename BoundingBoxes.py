import cv2

# Load image
image = cv2.imread('example.jpg')

# Coordinates for bounding box
start_point = (100, 100)
end_point = (200, 200)
color = (255, 0, 0)  # Red color in BGR format
thickness = 2

# Draw bounding box
image_with_box = cv2.rectangle(image, start_point, end_point, color, thickness)

# Save the image with bounding box
cv2.imwrite('image_with_box.jpg', image_with_box)

# Print a message to confirm that the image was saved
print("Image saved as 'image_with_box.jpg'")
