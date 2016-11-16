#!/bin/sh
echo "Content-type: text/html; charset=iso-8859-1"
echo "Content-Length: 554"
echo
echo "<html><head></head><body>"
echo
 file=`echo |date "+%Y-%m-%d".file |awk -F ' ' '{print $1}'`
echo $file
echo "<pre>"
cat $file
echo "</pre>"
echo "</body></html>"
