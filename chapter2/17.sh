#!/bin/sh

eval "cut -f1 hightemp.txt | sort | uniq"
