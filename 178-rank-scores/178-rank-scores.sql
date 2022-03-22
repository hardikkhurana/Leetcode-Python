Select score,Dense_RANK() OVER (Order By score DESC) as "RANK"
From Scores;
