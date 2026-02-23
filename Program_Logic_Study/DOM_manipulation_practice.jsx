// 1. Change Text on Button Click
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
</head>
<body>
    <p id="test">Hello</p>
    <button id="btn">CLick me</button>
    <script>
        const btn = document.getElementById("btn");
        const txt = document.getElementById("text");
        btn.addEventListener("click", function() {
            txt.innerText = "Button Clicked!";
        });
    </script>
</body>
</html>