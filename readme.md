1. Install numpy, scikit-learn (pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose scikit-learn)
2. Install ImageMagick (Include legacy tools - "convert")
2. Copy photos to a subfolder (name_of_the_trip) of img directory 
3. GenerateHTML.py need to be modified for image source path depending on whether files are self hosted or on Github pages (absolute path required)
4. Tweak dbscanit.py for cluster distance, execute runme.ps1, until satisfied with results
5. Execute resizeimage.ps1 to resize images to 800x800.
6. Tweak (name_of_the_trip).html, zoom factor appropriately.
7. Copy all files except *.csv, *.py for upload.


