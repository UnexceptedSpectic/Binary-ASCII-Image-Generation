# Randomized binary ASCII image generator

This repository describes a procedure for using any image to generate another with randomized* binary as its foreground and whitespace as its background.

**The foreground edges are configured to consist of "1" characters to ensure a more crisp delineation between the foreground and the background.*

## Steps:

1. Use https://cloudapps.herokuapp.com/imagetoascii/ to generate ASCII text from an input image (e.g. `charlotte_skyline.jpg`), using a custom charset of `01`.
2. Click "Copy to Text" and paste the contents into a text file e.g. `imagetoascii.txt`.
3. Manually modify `imagetoascii.txt` to correct/improve appearance, as needed.
4. Run `ascii_customizer.py` to remove the image background and randomize the foreground binary (except for the edges, which are set to "1"s).  `customized_ascii.txt` is automatically generated.
5. Use the "Copy to HTML" feature of the web service from step 1 to create an `customized_ascii.html` file.
6. Replace the content of the `pre` element in `customized_ascii.html` to include the text contained within `customized_ascii.txt`. *If upon previewing `customized_ascii.html` in your browser, the image is distorted, try pasting the ASCII content using a different text editor*.
7. Optionally, customize the CSS styling of the `pre` element to change the foreground font and background color.
8. Use [WebVector](https://github.com/radkovo/WebVector) to generate an SVG based off of `customized_ascii.html`.
9. Use [cloudconvert](https://cloudconvert.com/svg-to-png) to generate PNGs of variable resolutions, as needed.
10. Crop PNGs as needed.
