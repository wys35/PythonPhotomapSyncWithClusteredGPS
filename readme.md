1. Install numpy, scikit-learn, pillow (pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose scikit-learn pillow)
2. Install ImageMagick (Include legacy tools - "convert")
3. Copy photos to a subfolder (name_of_the_trip) of img directory 
4. Tweak dbscanit.py for cluster distance, execute runme.ps1, until satisfied with results in (name_of_the_trip).html
5. Execute resizeimage.ps1 to resize images to 800x800.
6. Tweak (name_of_the_trip).html, zoom factor appropriately.
7. Copy all files except *.csv, *.py for upload.

References

GPS data extraction 
	http://geospatialtraining.com/extracting-geographic-coordinates-from-photos-using-python/

Scikit-learn
	DBSCAN https://geoffboeing.com/2014/08/clustering-to-reduce-spatial-data-set-size/

JQuery scroll into view animaiton
	https://erraticdev.blogspot.com/2011/02/jquery-scroll-into-view-plugin-with.html
