eval "cut -f1 hightemp.txt | sort | uniq -c | sort -k1,1 -nr"
