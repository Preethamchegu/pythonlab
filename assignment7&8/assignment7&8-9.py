import re
punctuations = r'[.,!?;:()]'
date = r'\d{1,2}[-/]\d{1,2}[-/]\d{3,4}|\d{3,4}[-/]\d{1,2}[-/]\d{1,2}[-/]'
urls = r'https?://[^$\s/.?#].[^\s]'
email = r'[\u0c00-\u0c7F0-9]+@[\u0c00-\u0c7F0-9]+.[\u0c00-\u0c7F]{2,}'
number = r'(\d{1,3}(?:,\d{3})*(?:.\d{1,2})?)'
social_ids = r'@[\u0c00-\u0c7F0-9_]+'
telugu_text = r'[\u0c00-\u0c7F]+'
telugu_words= r'[\u0c00-\u0c7F,]+'
pattern = [punctuations,date,urls,email,number,social_ids,telugu_text,telugu_words]
combined_pattern = '|'.join(pattern)
def tokenizer(text):
    tokens = []
    for patterns in pattern:
        matches = re.findall(patterns,text)
        tokens.extend(matches)
    return tokens
text = '''నమస్కారం! ఎలా ఉన్నారు?
'''
tokens = tokenizer(text)
print(tokens)