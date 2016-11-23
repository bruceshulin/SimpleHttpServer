#!/bin/sh
echo "Content-type: text/html; charset=UTF-8"
echo "Content-Length: 100"

eval `/var/www/cgi-bin/proccgi.sh $*`
echo
echo "<html><head><style type=text/css> .align-center{ margin:0 auto;width:500px;text-align:left; } </style> </head><body><div class=align-center> "

#echo "</br>----</br>"
echo "</br>id:  $FORM_id</br>"
#echo "</br>user: "
#echo $FORM_user
#echo "</br>task: "
#echo $FORM_task
#echo "</br>time: "
#echo $FORM_time
#echo "</br>----</br>"
#echo "id:$FORM_id</br> name:$FORM_user</br>  workingtime:$FORM_time</br>task:$FORM_task</br>"


  if [ ! -n "$FORM_id"  ] ; 
    then
        echo "id is not fond! <a href ='temp.html'>go home</a></div></body></html>"
        return;
fi

file=`echo |date "+%Y-%m-%d".file |awk -F ' ' '{print $1}'`
echo "$file</br>"
for user in $(cat $file | awk -F: '{print $1 "\t" $5}') ; 
do
    if [ "$FORM_id" = "$user" ] ; 
        then
        break;
    else
        continue;
    fi
done

if [ "$FORM_id" = "$user" ];
    then
    tempfile=`echo |date "+%Y-%m-%d-%s".file |awk -F ' ' '{print $1}'`
    cat $file | sed  '/^'$FORM_id'/d' >$tempfile
    rm -rf $file
    cp $tempfile $file
    rm -rf $tempfile
    echo "delete success! look see <a href='list.cgi'> all list</a>"
    echo " or <a href='temp.html'>go home</a></br>"
else
    echo " not fond id:$FORM_id"
    echo "</br><a href='temp.html'>go home</a></br>"
fi
echo "</div></body></html>"
#echo "<pre>"
#echo `cat $file | sed ' -e /^$FORM_id/d'`
#echo "</pre>"
