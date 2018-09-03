write-host "install numpy, scikit-learn, copy photos to img directory and then run this script"
write-host "pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose scikit-learn"
Write-HOst "Googleapis.com access is required"
python .\getexifdata.py
python .\dbscanit.py
python .\getLocationName.py
python .\generateHTML.py


