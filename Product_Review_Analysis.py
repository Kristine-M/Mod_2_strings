# Task 1: Keyword Highlighter
# Write a program that searches through a series of 
# product reviews for keywords such as "good", "excellent", 
# "bad", "poor", and "average". Print out each review with 
# the keywords in uppercase so they stand out.

def highlight_words(review):
    words = ["good", "excellent", "bad", "poor", "average"]
    
    for keyword in words:
        review = review.replace(keyword, keyword.upper())
    
    return review

# Task 2: Sentiment Tally
# Develop a function that tallies the number of positive and 
# negative words in each review. Use a predefined list of positive 
# and negative words to check against. The function should return 
# the count of positive and negative words for each review.

def tally(review):
    pos_words = ["good", "excellent", "outstanding", "great"]
    neg_words = ["bad", "poor", "unfortunate", "disappointing"]
    
    pos_sum = 0
    neg_sum = 0
    
    for word in pos_words:
        if word in review:
            pos_sum += 1
            
    for word in neg_words:
        if word in review:
            neg_sum += 1
            
    return pos_sum, neg_sum
    
    

# Task 3: Review Summary
# Implement a script that takes the first 50 characters of 
# a review and appends "…" to create a summary. Ensure that 
# the summary does not cut off in the middle of a word.

def summary(review):
    review_cut = review[:50]
    
    if review_cut[49].isalnum():
        i = 0
        
        while(review[49 + i].isalnum()):
            i += 1
            
        review_cut = review[:50 + i] + "..."
        return review_cut
    else:
        review_cut = review_cut + "..."
        return review_cut
        
        
    