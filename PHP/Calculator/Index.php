<!DOCTYPE html>
<html>
  <head>
    <title>Login Form</title>
    <link href="style.css" rel="stylesheet">
  </head>
  <body class="body">
    <form class="form" action="Index.php" method="get">
         <input class="inp1" type="text" name="inp1" placeholder="Number1">
               <input class="inp1" type="text" name="inp2" placeholder="Number2">
          <input class="btn" type="submit" name="add" value="Calculate">
     <select name="drop_down">
          <option>None</option>
               <option>Add</option>
                         <option>Subtract</option>
                    <option>Multiply</option>
               <option>Divide</option>
          </select>
     </form>
<?php
     //Variables
     //$_GET['inp1'];
     //$_GET['inp2'];
     $operator = $_GET['drop_down'];
     $result = 0;
     //Checking for operator
     switch ($_GET['drop_down']) {
          case None:
               echo "<p>Please Enter An Operator</p>";
          break;
          case Add:
               $result = $_GET['inp1'] + $_GET['inp2'];
               echo "<p>Your result is".$result"</p>";
          break;
          case Subtract:
               $result = $_GET['inp1'] - $_GET['inp2'];
               echo "<p>Your result is </p>".$result;
          break;
          case Multiply:
               $result = $_GET['inp1'] * $_GET['inp2'];
               echo "<p>Your result is </p>".$result;
          break;
          case Divide:
               $result = $_GET['inp1'] / $_GET['inp2'];
               echo "<p>Your result is </p>".$result;
          break;
     };
?>
  </body>
</html>
