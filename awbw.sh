#!/bin/bash

ID=$1
NAME=$2
TURNS=$3
ZOOM=$4
PTH='/home/chipdelmal/Documents/AWBW/'

IN="$PTH/$NAME/M*.png"
OUT_SM="$PTH/$NAME/${NAME}_small"
OUT_LG="$PTH/$NAME/${NAME}"

echo "${OUT_SM}.gif"

python main.py $ID $NAME $TURNS $ZOOM $PTH
convert -delay 120 -resize 500x500 -loop 0 $IN "${OUT_SM}.gif"
convert -delay 120 -loop 1 $IN "${OUT_LG}.gif"
convert -delay 120 -loop 1 $IN "${OUT_LG}.mp4"