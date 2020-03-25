<html>
    <head>
        <meta charset = "utf-8">
        <title>Build and Predict Your Title</title>
    </head>
    <body>
        <form action="https://machine-learning.api.tianshome.com/movie-predictor-api/" target="_blank" name="form" id="form1" method="get">
            <label for="startYear">Start Year (enter a number)</label><br>
            <input type="text" id="startYear" name="startYear"><br>
            <label for="runtimeMinutes">Number of Minutes (enter a number)</label><br>
            <input type="text" id="runtimeMinutes" name="runtimeMinutes"><br>
            <br>
            <label for="tconst">directorAverage (enter a number)</label><br>
            <input type="text" id="directorAverage" name="directorAverage"><br>
            <label for="writerAverage">writerAverage (enter a number)</label><br>
            <input type="text" id="writerAverage" name="writerAverage"><br>
            <label for="principalAverage">principalAverage (enter a number)</label><br>
            <input type="text" id="principalAverage" name="principalAverage"><br>
            <br>
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
