#!/bin/sh

echo "Content-type: text/html; charset=UTF-8"
echo "Content-Length: 500"

eval `/var/www/cgi-bin/proccgi.sh $*`
echo
echo "<html><head><style type=text/css> .align-center{ margin:0 auto;width:500px;text-align:left; } </style> </head><body><div class=align-center> "

  if [ ! -n "$FORM_id"  ] ; 
  	then
  	echo "id:$FORM_id</br> id is not fond! <a href ='temp.html'>go home</div></body></html>"
        return;
fi
#show submit param
echo "id:$FORM_id</br> name:$FORM_user</br>  workingtime:$FORM_time</br>task:$FORM_task</br>task:$FORM_tocao"
#save param to log.file
#echo $QUERY_STRING>>log.file

#is file exist
filepath=`echo |date "+%Y-%m-%d".file  |awk -F ' ' '{print $1}'`
if [ -f $filepath ];
then
	echo
else
	touch  $filepath
	echo "</br>create  $filepath"
fi

#find id
isfindid=0
filepath=`echo |date "+%Y-%m-%d".file  |awk -F ' ' '{print $1}'`
for user in $(cat $filepath | awk -F: '{print $1 "\t" $5}') ; 
do
    if [ "$FORM_id" = "$user" ] ; then
        isfindid=1
        break;
    else
    	echo 
    fi
done
echo "</br></br>"
#search over
if [ $isfindid = 1 ];
    then
    	echo "Locate the original records, </br>you can <a href='delete.cgi?id=$FORM_id'>delete record</a> or "
    	echo "<a href='temp.html'>go home</a>"
    else
    	echo "$FORM_id\t$FORM_user\t$FORM_time\t$FORM_task\t$FORM_tocao">>$filepath
    	echo " submit success!  good luck!<a href='list.cgi'>look all</a> or"
    	echo "<a href='delete.cgi?id=$FORM_id'>delete record</a> or "
	echo "<a href='temp.html'>go home</a>"
    fi
#endif


echo "</div></body></html>"
