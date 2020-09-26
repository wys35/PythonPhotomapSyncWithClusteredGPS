Installation
1. Install numpy, scikit-learn, exifread, piexif, gpsphoto (pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose scikit-learn exifread piexif gpsphoto)
2. Install ImageMagick (Include legacy tools - "convert")

Generation
1. Copy photos to a subfolder (name_of_the_trip) of img directory 
2. Tweak dbscanit.py for cluster distance, execute runme.ps1 -TripName name_of_the_trip, until satisfied with results in (name_of_the_trip).html
3. Execute resizeimage.ps1 -TripName name_of_the_trip to resize images to 800x800.
4. Tweak (name_of_the_trip).html, "zoom" factor appropriately.
5. Copy name_of_the_trip.html and img/name_of_the_trip/*.* for upload.

References

GPS data extraction 
	http://geospatialtraining.com/extracting-geographic-coordinates-from-photos-using-python/

Scikit-learn
	DBSCAN https://geoffboeing.com/2014/08/clustering-to-reduce-spatial-data-set-size/

JQuery scroll into view animation
	https://erraticdev.blogspot.com/2011/02/jquery-scroll-into-view-plugin-with.html
