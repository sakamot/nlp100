#!/bin/sh

echo "自然数を入力"
read input
command="tail -n ${input} hightemp.txt"
eval $command
