import re

article = """
Python continues to grow in popularity across industries. 
Many companies are adopting Python for data science, machine learning, and automation. 
Its simple syntax and large ecosystem make development faster.
"""

prompt = f"""
Summarize the following news article in exactly 2 sentences:

{article}
"""

summary = """
Python is widely used across industries for data science and automation. 
Its simple syntax and large ecosystem make development faster.
"""

words = summary.split()

if len(words) > 50:
    sentences = re.split(r'(?<=[.!?])\s+', summary)
    final_summary = ""
    count = 0

    for sentence in sentences:
        sentence_words = sentence.split()

        if count + len(sentence_words) <= 50:
            final_summary += sentence + " "
            count += len(sentence_words)
        else:
            break

    summary = final_summary.strip()

print(summary)