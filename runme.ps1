write-host "install numpy, scikit-learn, copy photos to img directory and then run this script"
Write-HOst "Googleapis.com access is required"
python .\getexifdata.py
python .\dbscanit.py
python .\getLocationName.py
python .\generateHTML.py


