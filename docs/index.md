Ever thought about making a movie? What would be people's response? Would the average rating of your movie beat the averge? Fill out the following details to get an estimate! Also: take a look the [technical specs](technical).

<html>
    <body>
        <form action="https://machine-learning.api.tianshome.com/movie-predictor-api" target="_blank" name="form" id="form1" method="get">
            <label for="startYear">Start Year (enter a number) (*)</label><br>
            <input type="text" id="startYear" name="startYear"><br>
            <label for="runtimeMinutes">Number of Minutes (enter a number) (*)</label><br>
            <input type="text" id="runtimeMinutes" name="runtimeMinutes"><br>
            <br>
            <label for="tconst">Average rating for directors (enter a number) (*)</label><br>
            <input type="text" id="directorAverage" name="directorAverage"><br>
            <label for="writerAverage">Average rating for writers (enter a number) (*)</label><br>
            <input type="text" id="writerAverage" name="writerAverage"><br>
            <label for="principalAverage">Average rating for actors (enter a number) (*)</label><br>
            <input type="text" id="principalAverage" name="principalAverage"><br>
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
            <input type="checkbox" id="isDrama" name="isDrama">
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
            <input type="checkbox" id="isRomance" name="isRomance">
            <label for="isRomance">Romance</label><br>
            <input type="checkbox" id="isSci-Fi" name="isSci-Fi">
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
            <input type="submit" value="Submit">
        </form>
    </body>
</html>
