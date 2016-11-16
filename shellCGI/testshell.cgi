#!/bin/sh

echo "Content-type: text/plain; charset=iso-8859-1"
echo
echo "<body align=center>"

echo "<div >"

echo "</br>---------------------1--------------------------------</br>"



echo "</br>---------------------2--------------------------------</br>"


#eval `./test.sh $*` 
#
temp="6bKN5Lmm5p6X6bKN5Lmm5p6X6bKN5Lmm5p6X"
echo $temp
echo "</br>"
echo `echo $temp|base64 -d`>>aaa789.file
#ok 


#find id
isfindid=0
id="61"
filepath=`echo |date "+%Y-%m-%d".file  |awk -F ' ' '{print $1}'`
for user in $(cat $filepath | awk -F: '{print $1 "\t" $5}') ; 
do
    if [ "$id" = "$user" ] ; then
        isfindid=1
        break;
    else
    	echo 
    fi
done
    if [ $isfindid = 1 ];
    then
    	echo "find yes"
    else
    	echo "find no"
    fi
#endif


return
#find id
username="root"
for user in $(cat /etc/passwd | awk -F: '{print $1 "\t" $5}') ; 
do
    echo "&lt;li&gt;"
    if [ "$username" = "$user" ] ; then
        echo "&lt;strong&gt;$user&lt;/strong&gt;"
    else
        echo "$user"
    fi
    echo "&lt;/li&gt;</br>"
done
#endif





echo "</div>"
echo "</body>"
