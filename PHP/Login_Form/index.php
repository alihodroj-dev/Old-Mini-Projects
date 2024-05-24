<!DOCTYPE html>
<html>
   <head>
      <title>Login Form</title>
         <meta charset="utf-8">
      <link href="Style.css" rel="stylesheet">
   </head>
   <body id="body">
      <script src="script.js"></script>
         <form action="index.php" method="post" id="form">
            <h1 id="h1">Register</h1>
               <input id="email" type="email" placeholder="name@example.com" name="email" required>
                  <input id="pass" type="password" placeholder="password" name="pass" required>
                     <input id="pass" type="password" placeholder="confirm-password" >
                  <input id="age" type="text" placeholder="Age" name="age" required>
               <input id="city" type="text" placeholder="City" name="city" required>
            <input id="btn" type="submit" value="Register">
         </form>
         <?php
         $host = "localhost";
         $user = "root";
         $password = "ali123hodroj";
         $db_name = "Toxic_Code";
         $email = $_POST['email'];
         $pass = $_POST['pass'];
         $age = $_POST['age'];
         $city = $_POST['city'];

         // Creating Connection
         $conn = new mysqli($host, $user, $password, $db_name);
         // Checking Connection
         if ($conn->connect_error) {
              die("Connection failed: " . $conn->connect_error);
         }
         // SQL querys
         $sql = "INSERT INTO USERS (ID,EmaiL,Pass_word,Age,City) VALUES('$email','$pass',$age,'$city')";
         //$_POST['email'],$_POST['pass'],$_POST['age'],$_POST['city']
         $conn->query($sql);

         $conn->close();
         ?>
   </body>
</html>
