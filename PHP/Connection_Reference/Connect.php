<?php
$host = "localhost";
$user = "root";
$password = "ali123hodroj";
$db_name = "DB_1";

// Creating Connection
$conn = new mysqli($host, $user, $password, $db_name);
// Checking Connection
if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
}
// SQL querys
$sql = "";

if ($sql != "" && $conn->query($sql) == TRUE) {
     echo "query successful";
}else {
     echo "query Failed";
};
$conn->close();
?>
