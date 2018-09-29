param (
    [Parameter(mandatory=$true)]
    $tripname
)
write-host "install numpy, scikit-learn, copy photos to a subfolder (name of the trip) in img directory and then run this script"
write-host "pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose scikit-learn"
write-host "generateHTML.py need to be modified depending on whether self hosting or on Github pages (relative path)"
write-host "or absolute path"
write-host "`n`n"

python .\getexifdata.py $tripname
python .\dbscanit.py
python .\getLocationName.py
python .\generateHTML.py $tripname


