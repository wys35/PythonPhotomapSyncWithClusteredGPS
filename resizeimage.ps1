$files = Get-ChildItem -Path img/luoyang *.jpg
$files | ForEach-Object {
    convert -resize 800x800 $_.FullName $_.FullName
}