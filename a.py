print("glad i joined staragile")
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Zepto.js Example</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/zepto/1.2.0/zepto.min.js"></script>
</head>
<body>
    <button id="clickButton">Click Me!</button>
    <div id="message" style="display: none;">You clicked the button!</div>

    <script>
        $('#clickButton').on('click', function() {
            $('#message').show();
        });
    </script>
</body>
</html>
