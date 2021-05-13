/* Arturas Pranskunas
 * This is the second part of "Push-Ups Counter"  project
 * The project can be found at https://ehelper.tk/
 * 
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 */
 
// Updaing live records without full content refresh
function loadRecord(){
	var xhttp;
	if (window.XMLHttpRequest){
		xhttp = new XMLHttpRequest();
		}
		else {
		// IE5
		xhttp = new ActiveXObject("Microsoft.XMLHTTP");
	    }
	xhttp.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200){
			//document.getElementById("liveRecord").innerHTML = this.responseText;
			var txt = this.responseText;
			var obj = JSON.parse(txt);
			document.getElementById("liveRecord").innerHTML = obj[0].liverecord;
			document.getElementById("pbest").innerHTML = obj[0].pbest;
			document.getElementById("thisweek").innerHTML = obj[0].tthisweek;
			//document.getElementById("updateButton").disabled = true;
			if(obj[0].liverecord == 0){
				document.getElementById("updateButton").disabled = true;
				}
				else{
					document.getElementById("updateButton").disabled = false;
					}
		}
	};
	xhttp.open("GET", "PushUps-update.php", true);
	xhttp.send();
	
}

var number = 0;
var previousnumb = 0;	
function Reset(){
	number = 0;
	document.getElementById("liveRecord").innerHTML = "0"
	};
var timeout = setInterval(loadRecord,500);
