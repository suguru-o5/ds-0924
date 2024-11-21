# SQL Lab Select and Filter Data Exercises

## Exercises
### 1. Select all columns from the movies table.
Write a query to retrieve all columns from the movies table.
```
SELECT *
FROM   movies; 
```

### 2. Select only the title and release_year columns from the movies table.
Write a query to retrieve the title and release_year columns from the
movies table.
```
SELECT title,
       release_year
FROM   movies; 
```

### 3. Select all movies released after the year 2000.
Write a query to retrieve all movies that were released after the year 2000.
```
SELECT *
FROM   movies
WHERE  release_year > 2000; 
```

### 4. Select all movies with the genre 'Action'.
Write a query to retrieve all movies that have the genre 'Action'.
```
SELECT *
FROM   movies
WHERE  genre = 'Action'; 
```

###  5. Count the total number of movies in the movies table.
Write a query to count the total number of movies in the movies table.
```
SELECT COUNT(*)
FROM movies;
```

### 6. Count the number of distinct genres in the movies table.
Write a query to count the number of distinct genres in the movies table.
```
SELECT COUNT(DISTINCT genre)
FROM   movies; 
```

### 7. Select all movies released between 1990 and 2000.
Write a query to retrieve all movies that were released between 1990 and 2000.
```
SELECT *
FROM   movies
WHERE  release_year BETWEEN 1990 AND 2000; 
```

### 8. Select all movies that are either in the 'Drama' genre or released before 1990.
Write a query to retrieve all movies that are either in the 'Drama' genre or were released before 1990.
```
SELECT *
FROM   movies
WHERE  genre = 'Drama'
        OR release_year < 1990; 
```

### 9. Select all movies whose titles start with 'The'.
Write a query to retrieve all movies whose titles start with 'The'.
```
SELECT *
FROM   movies
WHERE  title LIKE 'The%' 
```

### 10. Select all movies whose titles do not contain the word 'Love'.
Write a query to retrieve all movies whose titles do not contain the word 'Love'.
```
SELECT *
FROM   movies
WHERE  title NOT LIKE '%Love%' 
```

### 11. Select all movies with genres in ('Drama', 'Fantasy', 'Action').
Write a query to retrieve all movies with genres in ('Drama', 'Fantasy', 'Action').
```
SELECT *
FROM   movies
WHERE  genre IN ( 'Drama', 'Fantasy', 'Action' ); 
```

### 12. Select the titles of all 'Fantasy' movies released between 2005 and 2015.
Write a query to retrieve the titles of all 'Fantasy' movies released between 2005 and 2015.
```
SELECT title
FROM   movies
WHERE  genre = 'Fantasy'
       AND release_year BETWEEN 2005 AND 2015; 
```

### 13. Count the number of movies for each genre.
Write a query to count the number of movies for each genre.
```
SELECT genre,
       COUNT(*)
FROM   movies
GROUP  BY genre; 
```

### 14. Select the first 10 movies released after the year 2000.
Write a query to retrieve the first 10 movies that were released after the year 2000.
```
SELECT *
FROM   movies
WHERE  release_year > 2000
LIMIT  10; 
```

### 15. Select the movie titles that contain the word 'Star'.
Write a query to retrieve the titles of movies that contain the word 'Star'.
```
SELECT *
FROM   movies
WHERE  title LIKE '%Star%'; 
```

### 16. Select the distinct release years of movies.
Write a query to retrieve the distinct release years of movies.
```
SELECT DISTINCT release_year
FROM   movies; 
```

### 17. Select the genres that have more than 50 movies.
Write a query to retrieve the genres that have more than 50 movies.
```
SELECT genre
FROM   movies
GROUP  BY genre
HAVING COUNT(genre) > 50; 
```

### 18. Select all movies that are not in the 'Fantasy' genre.
Write a query to retrieve all movies that are not in the 'Fantasy' genre.
```
SELECT *
FROM   movies
WHERE  genre <> 'Fantasy'; 
```

### 19. Select all movies with a release year that is null.
Write a query to retrieve all movies with a release year that is null.
```
SELECT *
FROM   movies
WHERE  release_year IS NULL; 
```

### 20. Select all movies released in the 1990s.
Write a query to retrieve all movies that were released in the 1990s.
```
SELECT *
FROM   movies
WHERE  release_year BETWEEN 1990 AND 1999; 
```