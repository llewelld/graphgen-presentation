#!/bin/sh

cd figures

mv automark.txt automark-prev.txt
mv automark-next.txt automark.txt
mv automark-prev.txt automark-next.txt
touch automark.txt

cd ..

