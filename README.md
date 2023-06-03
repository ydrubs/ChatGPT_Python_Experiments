# ChatGPT_Python_Experiments
Experiments generating different types of programs with Python with the help of ChatGPT

**Pixel_Painter:**
- Use Pixel_Painter.py to generate a sequence of pixels to the screen. 
 	- Keys:
  		- Arrow keys: Move the pixel around
  		- Spacebar: Change color of the pixel to a random color
  		- 's': Set the current pixel position to the color of the pixel
  		- 'g': Generate a script called grid_pattern.py which stores the orientation of the pixels 

- Use Pixel_Playground.py to manipulate the pixels created by Pixel_Painter. The script looks for and loads grid_pattern.py or gives an error if not found. 
	- Keys:
		- 'p': enable the pixels to fall down 
		- 'r': reset the pixels to the initial orientation when first loaded (movement must be off via the 'p' key)
		- 'w': Toggle pixel drift on and off (fall slightly left or right instead of down)
		- 'c': Toggle pixel collision on and off 

