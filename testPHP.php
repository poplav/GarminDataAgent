<?php
mysql_connect("localhost","root","");
mysql_select_db("garmin");
$sql=mysql_query("select * from garminData");
while($row=mysql_fetch_assoc($sql))
$output[]=$row;
print(json_encode($output));// this will print the output in json
mysql_close();
?>
