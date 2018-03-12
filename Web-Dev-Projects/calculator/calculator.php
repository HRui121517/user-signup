<!DOCTYPE html>
<html>
    <head>
        <title>Results</title>
    </head>
    <body>
        <?php
            $f = $_GET["1v"];
            $s = $_GET["2v"];
            $op = $_GET["operator"];
            if (trim($x) == "" || trim($y) == "" || $op == "") {
                echo "Missing field. Enter x,y and the operation.";
            }
            else {
                switch ($op) {
                    case 'Add':
                        $out = $f + $s;
                        echo "$f + $s = $out";
                        break;
                    case 'Minus':
                        $out = $f - $s;
                        echo "$f - $s = $out";
                        break;
                    case 'Multiply':
                        $out = $f * $s;
                        echo "$f * $s = $out";
                        break;
                    case 'Divide':
                        if ($s == 0) {
                            echo "Error: Division by 0.";
                        }
                        else {
                            $out = $f / $s;
                            echo "$f / $s = $out";
                        }
                        break;
                    default:
                        break;
                }
            }
        ?>
    </body>
</html>
    