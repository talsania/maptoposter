#!/usr/bin/env python3
"""
Split a wide poster into two equal halves.
"""

import sys
from pathlib import Path
from PIL import Image


def split_poster(input_path, output_dir="posters"):
    """
    Split a poster image into left and right halves.
    
    Args:
        input_path: Path to the input image
        output_dir: Directory to save output images
    """
    # Load the image
    img = Image.open(input_path)
    width, height = img.size
    
    print(f"Original image: {width}x{height} pixels")
    
    # Calculate the midpoint
    midpoint = width // 2
    
    # Split into left and right halves
    left_half = img.crop((0, 0, midpoint, height))
    right_half = img.crop((midpoint, 0, width, height))
    
    print(f"Left half: {left_half.size[0]}x{left_half.size[1]} pixels")
    print(f"Right half: {right_half.size[0]}x{right_half.size[1]} pixels")
    
    # Generate output filenames
    input_file = Path(input_path)
    stem = input_file.stem
    ext = input_file.suffix
    
    left_output = Path(output_dir) / f"{stem}_left{ext}"
    right_output = Path(output_dir) / f"{stem}_right{ext}"
    
    # Save the halves
    left_half.save(left_output, dpi=(600, 600))
    right_half.save(right_output, dpi=(600, 600))
    
    print(f"\n✓ Saved left half: {left_output}")
    print(f"✓ Saved right half: {right_output}")
    print(f"\nEach poster is now 5:7 ratio at 600 DPI")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python split_poster.py <input_image_path>")
        print("Example: python split_poster.py posters/ahmedabad_midnight_blue_20260218_123456.png")
        sys.exit(1)
    
    input_path = sys.argv[1]
    
    if not Path(input_path).exists():
        print(f"Error: File '{input_path}' not found")
        sys.exit(1)
    
    split_poster(input_path)
