# NLP-based network status inquiry
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample network status inquiry
user_query = "What is the current status of server 192.168.1.101?"

# Tokenize and process the user query
nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(user_query)
filtered_query = [word for word in word_tokens if word.lower() not in stop_words]

# Interpret user query and provide network status
if 'status' in filtered_query and 'server' in filtered_query:
    server_ip = filtered_query[filtered_query.index('server') + 1]
    print(f"The current status of server {server_ip} is operational.")
else:
    print("Sorry, I couldn't understand your query.")
