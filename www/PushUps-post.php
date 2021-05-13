<?php
/* Arturas Pranskunas
 * This is the second part of "Push-Ups Counter"  project
 * The project can be found at https://ehelper.tk/
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 */
include 'config.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
	
	// Create connection
	$conn = new mysqli($servername, $username, $password, $dbname);
	// Check connection
	if ($conn->connect_error) {
		die("Connection failed: " . $conn->connect_error);
	}
	// Updating new record and updating push ups statistics
	if(isset($_POST['update_btn']) && $_POST['update_btn'] == "Update"){
		$sqlPbBest ="INSERT INTO records (`number`) VALUES ((SELECT Num FROM current_state WHERE id = 1)); ";
		$sqlPbBest.="UPDATE personal_best SET total_this_week = (SELECT SUM(number) AS totalThisWeek FROM records WHERE yearweek(DATE(date), 1) = yearweek(curdate(), 1)); "; 
		$sqlPbBest.="UPDATE personal_best SET personal_best = (SELECT MAX(number) FROM records); ";
		$sqlPbBest.="UPDATE current_state SET Num = 0 WHERE ID = 1; ";
		if($conn->multi_query($sqlPbBest) === TRUE){
			//Personal best records updated
			
			}
			else{
				echo "Error updating personal best records". $conn->error;
				}
		
		}
		// Setting current state push-ups count to 0
	if(isset($_POST['reset_btn']) && $_POST['reset_btn'] == "Reset"){
		//echo "Reset clicked";
		
		$sql = "UPDATE `current_state` SET Num = 0 WHERE ID =1";
		if($conn->query($sql) === TRUE){
		//echo "Record updated";
		}else {
		echo "Error updating". $conn->error;
			}
		
		}	
		
	$conn->close();
	
	
}
else {
   // echo "No data posted with HTTP POST.";
}

?> 