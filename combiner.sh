#!/bin/bash

[ -v GKTODAY ] && set -x

echo "hi"

cd articles || exit
for i in *
do
    cd "$i" || exit
    for mo in */
    do
        cd "$mo" || exit
        pdfunite -- *.pdf "../${mo%*/}.pdf"
        cd .. || exit
    done
    pdfunite -- *.pdf "../${i}.pdf"
    rm -rf -- *.pdf
    cd .. || exit
done
