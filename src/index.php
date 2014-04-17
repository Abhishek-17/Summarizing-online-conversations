<!--
    Authors:
        Abhishek
        Savitansh
    -->
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Your title</title>
<link href="css.css" rel="stylesheet" type="text/css" />
</head>

<body>
<div id="wrap">
<div id="main">
<div id="header">
<h1>Email conversation summarizer</h1>
<p class="desc">IRE PROJECT</p>
</div>
<div id="maincontent">

<?php
$folder = "testSplitted/";
if (isset($_FILES['filename'])&&is_uploaded_file($_FILES['filename']['tmp_name']))  {  
    if (move_uploaded_file($_FILES['filename']['tmp_name'], $folder.$_FILES['filename']['name'])) {
         //Echo "File uploaded";
    } else {
         Echo "File not moved to destination folder. Check permissions";
    }
    $command="python summarize.py ".$folder.$_FILES['filename']['name']." splitted 2>&1";
    //echo $command;
    echo"<h2>Summary</h2>";

    $res = shell_exec($command);
    echo "".$res."";
    $folder = "givenids";
    if (isset($_FILES['summaryFile'])&&is_uploaded_file($_FILES['summaryFile']['tmp_name']))  {  
        if (move_uploaded_file($_FILES['summaryFile']['tmp_name'], $folder)) {
            //Echo "summary file saved uploaded";
     } else {
            Echo "File not moved to destination folder. Check permissions";
        };
     $res2 = shell_exec("python precision_racall.py 2>&1");
     echo "</br></br><h2>Precision and Recall</h2>";
     echo $res2;	
    }  
}
else {
	echo"<h2>Details..</h2>";
    echo "<p>These days summarization has become an increasingly useful approach to tackle the problem of information overload and extracting information from online conversations can be of very good commercial and educational value. But majority of this information is present as noisy unstructured text making traditional document summarization techniques difficult to apply. So using modern language and machine learning techniques we have developed an automatic text summarizer which extracts sentences from the conversation to form a summary.</p>";
    echo"</br><h2>How to use..</h2>";
    echo "
        <p>
        <ul>
        <li>Upload the xml file having a thread to be summarized. </li>
        <li>You can optionally upload a file having ids of sentences which you think should be there in summary. We will give precision and recall using it. </li>
        </ul>       
    ";
}
?>



</div>
</div>

<div id="side">
<div id="sidecontent">
<h3>Upload Test File</h3>
 ( Test xml to be tagged )
<form action="index.php" method="post" enctype="multipart/form-data">
</br><input type="file" name="filename" /> </br>


<h3>Upload Id file</h3>
 
Select a summary file(optional) which has list of sentence ids (one per line, to be used to find precision and recall): <br /><br />
Summary id File: <input type="file" name="summaryFile" /></br></br>
<input type="submit" value="Upload" />
</form>
</div>
</div>

<div id="footer"><p>Abhishek Savitansh Ankur Sneha</p></div>
</div>
</body>
</html>
