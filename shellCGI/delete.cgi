#!/bin/sh
echo "Content-type: text/plain; charset=iso-8859-1"
echo "Content-Length: 100"
eval `/var/www/cgi-bin/proccgi.sh $*`
echo
echo "<body align=center>"

echo "<div >"
#echo "</br>----</br>"
echo "</br>id: "
echo $FORM_id
#echo "</br>user: "
#echo $FORM_user
#echo "</br>task: "
#echo $FORM_task
#echo "</br>time: "
#echo $FORM_time
#echo "</br>----</br>"
#echo "id:$FORM_id</br> name:$FORM_user</br>  workingtime:$FORM_time</br>task:$FORM_task</br>"


#delete option