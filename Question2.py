from PIL import Image
import time

# Generate the number 'n'
current_time = int(time.time())
generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated Number: {generated_number}")

# Load the image
image = Image.open("chapter1.jpg")
pixels = image.load()

# Get the dimensions of the image
width, height = image.size

# Create a variable to store the sum of red pixel values
red_sum = 0

# Modify the image by adjusting the (r, g, b) values and sum the red values
for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        new_r = min(r + generated_number, 255)  # Ensure the value stays within 0-255
        new_g = min(g + generated_number, 255)
        new_b = min(b + generated_number, 255)
        
        pixels[x, y] = (new_r, new_g, new_b)
        
        # Add the red value to the sum
        red_sum += new_r

# Save the modified image
image.save("chapter1out.png")

# Output the sum of red pixel values
print(f"Sum of red pixel values: {red_sum}")
