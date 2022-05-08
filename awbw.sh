#!/bin/bash

##############################################################################
# AWBW.sh
# ----------------------------------------------------------------------------
#   ID:     AWBW ID number (look at README for reference)
#   NAME:   Arbitrary match name for folder and file naming
#   TURNS:  Number of turns taken on the match (look at README for reference)
#   ZOOM:   Zoom level (look at README for reference)
#   PTH:    Folder in which the files will be exported
#   RES:    Resolution for small thumbnail version of the GIF
#   DELAY:  Delay between frames (in miliseconds)
##############################################################################
ID=$1
NAME=$2
TURNS=$3
ZOOM=$4
PTH=$5
RES='290'
DELAY='120'
# Create paths and names for the frames and gifs -----------------------------
IN="$PTH/$NAME/*.png"
OUT_SM="$PTH/$NAME/${NAME}_small"
OUT_LG="$PTH/$NAME/${NAME}"
OUT_MD="$PTH/$NAME/${NAME}_medium"
# Print filename to terminal -------------------------------------------------
echo "${OUT_LG}.gif"
# Scrape battle frames -------------------------------------------------------
python main.py $ID $NAME $TURNS $ZOOM $PTH
# Convert frames to gifs and mp4 ---------------------------------------------
convert -delay $DELAY -resize "${RES}x${RES}" -loop 0 $IN "${OUT_SM}.gif"
convert -delay $DELAY -loop 1 $IN "${OUT_LG}.gif"
convert -delay $DELAY -loop 1 $IN "${OUT_LG}.mp4"
# Compres gifs ---------------------------------------------------------------
gifsicle -i "${OUT_LG}.gif" -O3 --colors 256 -o "${OUT_MD}.gif"