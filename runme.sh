printf "install numpy, scikit-learn, copy photos to img directory and then run this script"
printf "pip3 install --user numpy scipy matplotlib ipython jupyter pandas sympy nose scikit-learn"
printf "\n"
python3 ./getexifdata.py
python3 ./dbscanit.py
python3 ./getLocationName.py
python3 ./generateHTML.py

