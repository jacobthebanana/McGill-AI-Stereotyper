Ever thought about making a movie or a TV series? What would be people's response? Would the average rating of your movie beat the averge? 

Fill out the following details and we will provide an estimate based on the analysis of over **300,000** titles! 

Also: take a look the [technical specs](technical).

## Predict-a-title
Enter the details and hit submit! (Fields marked with an asterisk (\*) are *required*.) 

- **y = 1** means that we expect your title to get an above-average rating. Congratulations! 😆
- **y = 0** means that your title might get a below-average rating. Don't panic. Take a closer look at the "top features" shown below the score. Considering tweaking features with the highest "contribution" for a better performance. 😉
- In the unlikely event of a 503 Service Unavailable message, please (kindly) email `Jacob at Banana dot Abay dot Cf`. Not interested in waiting? Thanks to Docker, it takes as few as one line of command to spin up this API backend on your own machine! Get started by visiting the [project page](https://hub.docker.com/r/jacobthebanana/movie-rfc-backend) on Docker Hub. 🐳

<html>
    <body>
        <form action="https://machine-learning.api.tianshome.com/movie-predictor-api" target="_blank" name="form" id="form1" method="get">
            <label for="startYear">Start Year (enter a number) (*)</label><br>
            <input type="text" id="startYear" name="startYear" value="2014"><br>
            <label for="runtimeMinutes">Number of Minutes (enter a number) (*)</label><br>
            <input type="text" id="runtimeMinutes" name="runtimeMinutes" value="107"><br>
            <br>
            <p>Keep in mind that the average rating you are aiming for is <strong>7</strong>.</p>
            <label for="tconst">Average rating for directors (on a scale of 10) (*)</label><br>
            <input type="text" id="directorAverage" name="directorAverage" value="9"><br>
            <label for="writerAverage">Average rating for writers (on a scale of 10) (*)</label><br>
            <input type="text" id="writerAverage" name="writerAverage" value="9"><br>
            <label for="principalAverage">Average rating for actors (on a scale of 10) (*)</label><br>
            <input type="text" id="principalAverage" name="principalAverage" value="5"><br>
            <br>
            <input type="checkbox" id="isAction" name="isAction">
            <label for="isAction">Action</label>
            <input type="checkbox" id="isAdventure" name="isAdventure">
            <label for="isAdventure">Adventure</label><br>
            <input type="checkbox" id="isAnimation" name="isAnimation">
            <label for="isAnimation">Animation</label>
            <input type="checkbox" id="isBiography" name="isBiography">
            <label for="isBiography">Biography</label>
            <input type="checkbox" id="isComedy" name="isComedy">
            <label for="isComedy">Comedy</label><br>
            <input type="checkbox" id="isCrime" name="isCrime">
            <label for="isCrime">Crime</label>
            <input type="checkbox" id="isDocumentary" name="isDocumentary">
            <label for="isDocumentary">Documentary</label>
            <input type="checkbox" id="isDrama" name="isDrama" checked>
            <label for="isDrama">Drama</label><br>
            <input type="checkbox" id="isFamily" name="isFamily">
            <label for="isFamily">Family</label>
            <input type="checkbox" id="isFantasy" name="isFantasy">
            <label for="isFantasy">Fantasy</label>
            <input type="checkbox" id="isFilm-Noir" name="isFilm-Noir">
            <label for="isFilm-Noir">Film-Noir</label><br>
            <input type="checkbox" id="isGame-Show" name="isGame-Show">
            <label for="isGame-Show">Game-Show</label>
            <input type="checkbox" id="isHistory" name="isHistory">
            <label for="isHistory">History</label>
            <input type="checkbox" id="isHorror" name="isHorror">
            <label for="isHorror">Horror</label><br>
            <input type="checkbox" id="isMusic" name="isMusic">
            <label for="isMusic">Music</label>
            <input type="checkbox" id="isMusical" name="isMusical">
            <label for="isMusical">Musical</label>
            <input type="checkbox" id="isMystery" name="isMystery">
            <label for="isMystery">Mystery</label><br>
            <input type="checkbox" id="isNews" name="isNews">
            <label for="isNews">News</label>
            <input type="checkbox" id="isReality-TV" name="isReality-TV">
            <label for="isReality-TV">Reality-TV</label>
            <input type="checkbox" id="isRomance" name="isRomance" checked>
            <label for="isRomance">Romance</label><br>
            <input type="checkbox" id="isSci-Fi" name="isSci-Fi" checked>
            <label for="isSci-Fi">Sci-Fi</label>
            <input type="checkbox" id="isShort" name="isShort">
            <label for="isShort">Short</label>
            <input type="checkbox" id="isSport" name="isSport">
            <label for="isSport">Sport</label><br>
            <input type="checkbox" id="isTalk-Show" name="isTalk-Show">
            <label for="isTalk-Show">Talk-Show</label>
            <input type="checkbox" id="isThriller" name="isThriller">
            <label for="isThriller">Thriller</label>
            <input type="checkbox" id="isWar" name="isWar">
            <label for="isWar">War</label><br>
            <input type="checkbox" id="isWestern" name="isWestern">
            <label for="isWestern">Western</label>
            <br>
            <input type="submit" value="Submit ✔️">
        </form>
        <p>Please allow the backend around 30 seconds to warm up after submitting first request for prediction. Subsequent requests will be a breeze.</p> 
    </body>
</html>
