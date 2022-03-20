SELECT id,movie,description,rating
FROM Cinema
Where id%2!=0 and description!="boring"
ORDER BY rating desc;
