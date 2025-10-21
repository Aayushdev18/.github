#!/usr/bin/env python3
"""
Script to convert SVG icons to PNG format at 64x64px resolution.
Requires: pip install cairosvg pillow
"""

import os
import cairosvg
from PIL import Image
import io

def convert_svg_to_png(svg_path, png_path, size=64):
    """Convert SVG file to PNG with specified size."""
    try:
        # Convert SVG to PNG bytes
        png_bytes = cairosvg.svg2png(url=svg_path, output_width=size, output_height=size)
        
        # Save as PNG file
        with open(png_path, 'wb') as f:
            f.write(png_bytes)
        
        print(f"✓ Converted {svg_path} to {png_path}")
        return True
    except Exception as e:
        print(f"✗ Error converting {svg_path}: {e}")
        return False

def main():
    """Convert all SVG icons to PNG format."""
    icons = [
        'non-gmo-icon.svg',
        'no-antibiotics-icon.svg', 
        'hydrolyzed-icon.svg',
        'vegan-icon.svg',
        'organic-icon.svg'
    ]
    
    print("Converting SVG icons to PNG format (64x64px)...")
    print("=" * 50)
    
    success_count = 0
    for icon in icons:
        svg_path = icon
        png_path = icon.replace('.svg', '.png')
        
        if convert_svg_to_png(svg_path, png_path):
            success_count += 1
    
    print("=" * 50)
    print(f"Conversion complete: {success_count}/{len(icons)} icons converted successfully")
    
    if success_count < len(icons):
        print("\nNote: If conversion failed, you may need to install required packages:")
        print("pip install cairosvg pillow")

if __name__ == "__main__":
    main()
