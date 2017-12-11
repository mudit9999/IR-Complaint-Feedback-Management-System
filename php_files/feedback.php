<?php
$servername = "127.0.0.1";
$username = "kunwar";
$password = "";
$database = "twitter";

$conn = new mysqli($servername, $username, $password,$database);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

						$sql = "select * from tweets where prediction=0 order by id desc;";
						$result = $conn->query($sql);

						if ($result->num_rows > 0) {
    					while($row = $result->fetch_assoc()) {
    						echo "<table><tr><td style='color:black' width='180%'>";
        					echo $row["tweet"];
        					echo "</td><td width='20%'><button type='button' class='btn btn-info'><b>Reply</b></button></td></tr></table>";
    						}


							} ?>
