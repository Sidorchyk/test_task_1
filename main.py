<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/html">
<head>
    <meta charset="UTF-8">
    <title>Задача 1</title>
</head>

<script>
    const random = (min, max) => {
        let rnd = Math.random() * (max - min)
        return Math.round(rnd)
    }
    window.onload = () => {
            let interval = setInterval(() => {
                document.body.style.background = `rgb(${random(1, 255)}, ${random(1, 255)}, ${random(1, 255)})`
            }, 300)
    }
</script>


</body>
</html>