for file in `ls img/*.jpg`
do
    convert -resize 800x800 $file $file
done

