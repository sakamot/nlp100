#!/bin/sh

echo "-- 1st column --"
eval 'cut -f 1 hightemp.txt'
echo "-- 2nd column --"
eval 'cut -f 2 hightemp.txt'
