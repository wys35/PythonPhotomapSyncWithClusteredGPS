param (
    [Parameter(mandatory=$true)]
    $tripname
)
$files = Get-ChildItem -Path img/$tripname *.jpg
$files | ForEach-Object {
    convert -resize 800x800 $_.FullName $_.FullName
}