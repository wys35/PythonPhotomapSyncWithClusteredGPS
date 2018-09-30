param (
    [Parameter(mandatory=$true)]
    $tripname
)

python .\getexifdata.py $tripname
python .\dbscanit.py
python .\getLocationName.py
python .\generateHTML.py $tripname


