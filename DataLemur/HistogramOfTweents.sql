SELECT 
  num_tweets AS tweet_bucket,
  COUNT(*) AS users_num
  FROM
      (
SELECT 
    user_id, 
    COUNT(*) AS num_tweets
FROM 
    tweets
    
WHERE 
  tweet_date BETWEEN '01/01/2022' AND '12/31/2022'
GROUP BY 
    user_id
) total_tweets

GROUP BY 
num_tweets
ORDER BY 
num_tweets ASC