"""Assignment 1.
"""

import math

# Maximum number of characters in a valid tweet.
MAX_TWEET_LENGTH = 50

# The first character in a hashtag.
HASHTAG_SYMBOL = '#'

# The first character in a mention.
MENTION_SYMBOL = '@'

# Underscore is the only non-alphanumeric character that can be part
# of a word (or username) in a tweet.
UNDERSCORE = '_'

SPACE = ' '


def is_valid_tweet(text: str) -> bool:
    """Return True if and only if text contains between 1 and 
    MAX_TWEET_LENGTH characters (inclusive).

    >>> is_valid_tweet('Hello Twitter!')
    True
    >>> is_valid_tweet('')
    False
    >>> is_valid_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    False

    """
    
    return (len(text) >= 1) and (len(text) <= MAX_TWEET_LENGTH)

def compare_tweet_lengths(text1: str, text2: str) -> int:
    """Return 1 if text1 has more characters than text2, 
    -1 if text2 has more characters than text1, 
    and 0 if text1 has the same number of characters as text2.
    
    >>> compare_tweet_lengths('Hello Twitter!', 'Hi Twitter!')
    1
    >>> compare_tweet_lengths('Ding', 'Angela')
    -1
    >>> compare_tweet_lengths('Dog', 'Cat')
    0
    
    """
    
    if len(text1) > len(text2):
        return 1
    elif len(text2) > len(text1):
        return -1
    else:
        return 0
    
def add_hashtag(text: str, word: str) ->str:
    """Return a tweet followed by a hashtag with a tweet word. 
    In other words, return text followed by SPACE, HASHTAG_SYMBOL, and word. 
    If tweet with SPACE with HASHTAG_SYMBOL with word exceeds MAX_TWEET_LENGTH, 
    return tweet.
    
    >>> add_hashtag('I like', 'cats')
    'I like #cats'
    >>> add_hashtag('My favourite number is', '20')
    'My favourite number is #20'
    >>> add_hashtag('I won!', 'success')
    'I won! #success'
    >>> add_hashtag(2 * 'ABCDEFGHIJKLMNOPQRSTUVWX', 'wow')
    'ABCDEFGHIJKLMNOPQRSTUVWXABCDEFGHIJKLMNOPQRSTUVWX'
    
    """
    
    tweet_length = len(text) + len(SPACE) + len(HASHTAG_SYMBOL) + len(word)
    if 1 <= tweet_length <= MAX_TWEET_LENGTH:
        return text + SPACE + HASHTAG_SYMBOL + word
    return text

def contains_hashtag(text: str, word: str) -> bool:
    """Return True if text contains a hashtag symbol with word. Return False
    if text does not contain a hashtag symbol with word.
    
    >>> contains_hashtag('I like #cats', 'cats')
    True
    >>> contains_hashtag('I like #dogs', 'cats')
    False
    >>> contains_hashtag('#cats#dogs..#birds#hedgehogs??', 'hedgehogs')
    True
    >>> contains_hashtag('I like cats', 'cats')
    False
    >>> contains_hashtag('#birds#hedgehogs??', 'hedge')
    False
    
    """
    
    return (' ' + HASHTAG_SYMBOL + word + ' ') in (clean(text) + ' ')

def is_mentioned(text: str, word: str) -> bool:
    """Return True if text contains a mention symbol with word. Return False
    if text does not contain a mention symbol with word.
    
    >>> is_mentioned('Thanks @Angela!', 'Angela')
    True
    >>> is_mentioned('@KFC is really good.', 'McDonalds')
    False
    >>> is_mentioned('@Angela @Ding!!', 'Ang')
    False
    
    """
    
    return (' ' + MENTION_SYMBOL + word + ' ') in (clean(text) + ' ')

def add_mention_exclusive(text: str, word: str) -> str:
    """Return tweet with SPACE with MENTION_SYMBOL with word if the potential
    tweet does not exceed MAX_TWEET_LENGTH and tweet does not contain 
    MENTION_SYMBOL with word already. Return tweet if potential tweet exceeds 
    MAX_TWEET_LENGTH and/or tweet contains MENTION_SYMBOL with word already.
    
    >>> add_mention_exclusive('I like', 'cats')
    'I like @cats'
    >>> add_mention_exclusive('I like @cats', 'cats')
    'I like @cats'
    >>> add_mention_exclusive(2 * 'ABCDEFGHIJKLMNOPQRSTUVWX', 'wow')
    'ABCDEFGHIJKLMNOPQRSTUVWXABCDEFGHIJKLMNOPQRSTUVWX'
    
    """
    tweet_length = len(text) + len(SPACE) + len(MENTION_SYMBOL) + len(word)
    if not is_mentioned(text, word):
        if 1 <= tweet_length <= MAX_TWEET_LENGTH:
            return text + SPACE + MENTION_SYMBOL + word
    return text

def num_tweets_required(message: str) -> int:
    """Return the total number of tweets needed for a certain message. In other
    words, return the ceiling value of the length of message divided by
    MAX_TWEET_LENGTH.
    
    >>>num_tweets_required('Hi')
    1
    >>>num_tweets_required(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    2
    """
    return math.ceil(len(message)/MAX_TWEET_LENGTH)

def get_nth_tweet(message: str, n: int) -> str:
    """Return the nth tweet from the number of tweets that contain message. If n
    exceeds the number of the tweets there are in total, return an empty string.
    
    >>>get_nth_tweet('Hello there.', 0)
    'Hello there.'
    >>>get_nth_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234', 1)
    'UVWXYZ1234'
    >>>get_nth_tweet(2 * 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 2)
    ''
    """
    max_len = MAX_TWEET_LENGTH
    index = num_tweets_required(message)
    if n <= index:
        return message[(n * max_len) : (n * max_len) + max_len]
    return ''

# A helper function.  Do not modify this function, but you are welcome
# to call it.

def clean(text: str) -> str:
    """Return text with every non-alphanumeric character, except for
    HASHTAG_SYMBOL, MENTION_SYMBOL, and UNDERSCORE, replaced with a
    SPACE, and each HASHTAG_SYMBOL replaced with a SPACE followed by
    the HASHTAG_SYMBOL, and each MENTION_SYMBOL replaced with a SPACE
    followed by a MENTION_SYMBOL.

    >>> clean('A! lot,of punctuation?!!')
    'A  lot of punctuation   '
    >>> clean('With#hash#tags? and@mentions?in#twe_et #end')
    'With #hash #tags  and @mentions in #twe_et  #end'
    """

    clean_str = ''
    for char in text:
        if char.isalnum() or char == UNDERSCORE:
            clean_str = clean_str + char
        elif char == HASHTAG_SYMBOL or char == MENTION_SYMBOL:
            clean_str = clean_str + SPACE + char
        else:
            clean_str = clean_str + SPACE
    return clean_str
