from PIL import Image, ImageDraw, ImageFont
import os

# Create a simple logo image
def create_logo():
    # Create a new image with a white background
    img = Image.new('RGB', (100, 100), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    
    # Draw a rectangle border
    d.rectangle([(5, 5), (95, 95)], outline=(0, 102, 204), width=2)
    
    # Add text
    try:
        # Try to use a font (may not be available on all systems)
        font = ImageFont.truetype("arial.ttf", 20)
        d.text((25, 40), "IMS", fill=(0, 102, 204), font=font)
    except:
        # Fallback to default font
        d.text((25, 40), "IMS", fill=(0, 102, 204))
    
    # Save the image
    img.save('logo.png')
    print("Logo created successfully!")

if __name__ == "__main__":
    create_logo() 