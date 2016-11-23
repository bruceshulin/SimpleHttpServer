#!/bin/sh
echo "Content-type: text/html; charset=UTF-8"
echo "Content-Length: 554"
echo
echo "<html><head><style type=text/css> .align-center{ margin:0 auto;width:500px;text-align:left; } </style> </head><body><div class=align-center> "
echo	
echo	"</br></br><CENTER>list all today user record</CENTER></br>"
echo
echo
 file=`echo |date "+%Y-%m-%d".file |awk -F ' ' '{print $1}'`
echo $file
#echo "</br><span>id	姓名	工作任务	时间	吐槽</span>"
echo "<pre>"

cat $file
echo "</pre>"
echo "</br><CENTER><a href='temp.html'>go home</a></CENTER></br>"
echo "</div></body></html>"
