echo "install numpy, scikit-learn, copy photos to img directory and then run this script"
echo "pip3 install --user numpy scipy matplotlib ipython jupyter pandas sympy nose scikit-learn"
echo "Googleapis.com access is required"
python3 ./getexifdata.py
python3 ./dbscanit.py
python3 ./getLocationName.py
python3 ./generateHTML.py

