#!/bin/sh
echo "Content-type: text/html; charset=iso-8859-1"
echo "Content-Length: 118"
echo
#echo "</br>----</br>"
#echo "</br>id: "
#echo $FORM_id
#echo "</br>user: "
#echo $FORM_user
#echo "</br>task: "
#echo $FORM_task
#echo "</br>time: "
#echo $FORM_time
#echo "</br>----</br>"
#echo "id:$FORM_id</br> name:$FORM_user</br>  workingtime:$FORM_time</br>task:$FORM_task</br>"

echo "<html>"
eval `/var/www/cgi-bin/proccgi.sh $*`
echo "<body align=center>"
echo "<div >"
echo $QUERY_STRING>>log.file
filepath=`echo |date "+%Y-%m-%d".file  |awk -F ' ' '{print $1}'`
if [ -f $filepath ];
then
echo 
else
touch  $filepath
echo "</br>create  $filepath"
fi
#1find file  	2 open file 	3search key 	4 if key

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
#search over
    if [ $isfindid = 1 ];
    then
    	echo "Locate the original records, you can <a href='/delete.cgi?id=$FORM_id'>delete record</a>"
    else
    	echo "$FORM_id\t$FORM_user\t$FORM_time\t$FORM_task">>$filepath
    	echo "</br> submit success! </br> good luck!</br><a href='/list.cgi'>look all</a></br>"
    fi
#endif


echo "</div>"
echo "</body>"
echo "</html>"
