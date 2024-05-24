<?php
$host = "localhost";
$user = "root";
$password = "ali123hodroj";
$db_name = "Toxic_Code";

$name = 'roro';

// Creating Connection
$conn = new mysqli($host, $user, $password, $db_name);
// Checking Connection
if ($conn->connect_error) {
     die("Connection failed: " . $conn->connect_error);
}
// SQL querys
$sql = "INSERT INTO USERS (EmaiL,Pass_word,Age,City) VALUES()";
//$_POST['email'],$_POST['pass'],$_POST['age'],$_POST['city']
$conn->query($sql);

$conn->close();
?>
