#!/bin/bash

ID=$1
NAME=$2
TURNS=$3
ZOOM=$4
PTH='/home/chipdelmal/Documents/AWBW'

IN="$PTH/$NAME/M*.png"
OUT_SM="$PTH/$NAME/${NAME}_small.gif"
OUT_LG="$PTH/$NAME/${NAME}.gif"

# python main.py $ID $NAME $TURNS $ZOOM
convert -delay 90 -resize 500x500 -loop 0 $IN $OUT_SM
convert -delay 90 -loop 1 $IN $OUT_LG