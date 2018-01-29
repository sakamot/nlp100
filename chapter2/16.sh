#!/bin/sh

echo "自然数を入力"
read input
command="split -l ${input} hightemp.txt"
eval $command
