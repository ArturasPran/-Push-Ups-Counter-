<?php
/* Arturas Pranskunas
 * This is the second part of "Push-Ups Counter"  project
 * The project can be found at https://ehelper.tk/
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 */
header('Access-Control-Allow-Origin: *');
header('Content-type: application/json');

include 'config.php';

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$sql = "SELECT Num FROM current_state";
$liverecord ="";
$result2 ="";
if($result = $conn->query($sql)){
	$row = $result->fetch_assoc();
	$liverecord = $row["Num"];
	#echo $row["Num"];
}
$sql2 = "SELECT personal_best, total_this_week FROM personal_best";
if($result2= $conn->query($sql2)){
	$row = $result2->fetch_assoc();
	    $response = array();
		$response[0] = array(
			'id' => '0',
			'liverecord' => $liverecord,
			'pbest'=> $row["personal_best"],
			'tthisweek'=> $row["total_this_week"]
    );
echo json_encode($response);	
}

?> 
