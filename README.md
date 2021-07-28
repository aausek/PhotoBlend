```
       ██████╗ ██╗  ██╗ ██████╗ ████████╗ ██████╗ ██████╗ ██╗     ███████╗███╗   ██╗██████╗ 
       ██╔══██╗██║  ██║██╔═══██╗╚══██╔══╝██╔═══██╗██╔══██╗██║     ██╔════╝████╗  ██║██╔══██╗
       ██████╔╝███████║██║   ██║   ██║   ██║   ██║██████╔╝██║     █████╗  ██╔██╗ ██║██║  ██║
       ██╔═══╝ ██╔══██║██║   ██║   ██║   ██║   ██║██╔══██╗██║     ██╔══╝  ██║╚██╗██║██║  ██║
       ██║     ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████╗███████╗██║ ╚████║██████╔╝
       ╚═╝     ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝
      
                                 Developed by Team Senioritis
                                         Summer 2021
```

### Application Description

PhotoBlend is a custom image editor application that allows users to generate new images using blending modes & filters.
Offering a variety of blending modes and other filters, PhotoBlend allows the end user to generate images by working 
with 1 or 2 images at a time, then selecting the desired action to be performed. Finally, the product image is displayed
in the preview screen where it may be saved to the user's local drive. 

### Specifications
Custom application build using a PyQt5 GUI as the frontend, a custom C library for blending images, and the [imagefilters](https://github.com/gatorpazz/imagefilters) PIP package (a Rust-based library) for image filters. 

### Installation Options
- To install PhotoBlend start XServer and Ubuntu terminal
- `pip install photoblend` then run `photoblend`
- **Make sure you have the latest version of pip installed. (upgrade with 'pip install --upgrade pip')

- Alternatively, `git clone` this repository
- Execute `python3 setup.py install`
- `cd library/` and run `python3 main.py` to use PhotoBlend!

### Repository link
- https://github.com/aausek/PhotoBlend

### Completed Features
- Select 1 or 2 image layers.
- Single image filters: blur, bright, gray scale, flip vertical and flip horizontal.
- Blending modes: add, subtract, multiply, screen, overlay, lighten, darken, color dodge, color burn, 
  red/green/blue channel.
- 90° image rotation
- Single and/or double image preview
- Clear image selections
- Save product image to local drive
- Supported file formats: BMP, GIF, JPG, JPEG, PNG, PBM, PGM, PPM, XBM, XPM.

### Shelved Features
- Crop filter
- Preload image resizing




