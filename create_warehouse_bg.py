from PIL import Image
import os

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Ensure images directory exists
ensure_dir('images')

# Create a new image with warehouse background
warehouse_bg = Image.open('warehouse.jpg')  # The image you provided
warehouse_bg = warehouse_bg.resize((1350, 700), Image.Resampling.LANCZOS)
warehouse_bg.save('images/warehouse_bg.png', 'PNG')

print("Warehouse background image has been created successfully!") 