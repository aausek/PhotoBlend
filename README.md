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
Custom application build using a PyQt5 GUI as the frontend and C library supporting the backend. 

### Installation Options
- To install PhotoBlend start a virtual environment (in WSL also start XServer)
- `pip install photoblend` then run `photoblend`
- You're ready to start using PhotoBlend!

- Alternatively, `git clone` this repository
- Execute `python3 setup.py install`
- Run `python3 library/main.py` to launch app

### Repository link
- [GitHub Repo] (https://github.com/aausek/PhotoBlend)

### Completed Features
- Select 2 starter images
- Add and Subtract blending modes
- Clockwise image rotation 
- Image preview
- Save product image to local drive   
- Buttons for all remaining modes and filters
- Supporting .jpg and .png files

### In-Progress Features
- Multiply, Screen, Overlay, Lighten, Darken, Color Dodge and Color Burn blending modes
- Crop and Gray Scale options
- Additional filter options
- Support other file extensions

### Planned Features
- Crop and Gray Scale options
- Additional filter options
- Support other file extensions
