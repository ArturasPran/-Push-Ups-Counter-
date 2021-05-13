<html>
<head>
<link rel="stylesheet" href="style.css">
</head>
<body>
<script src="scripts.js"></script>
<?php include 'PushUps-post.php';?>
<div class="wrapper">
	<center>
	<h1 class="header">Push ups counter</h1>
	</center>
	<p id="liveRecord">0</p>
	<table id="t01">
	<tr>
	<th>Personal Best</th>
	<th>Total this week</th>
	</tr>
	<tr>
	<td id="pbest">0</td>
	<td id ="thisweek">0</td>
	</tr></table>
	<br>
	<center>
	<div class="buttonw">
		<form action="" method="POST">
        <!--<input type="button" onclick="loadRecord()" value="Update"> -->
        <input type="submit" id="updateButton" name ="update_btn" value="Update" disabled ="true">
		<input type="submit" name ="reset_btn" value = "Reset">
	</div>
	</center>
</form>

</div>
</body>
</html>
	
