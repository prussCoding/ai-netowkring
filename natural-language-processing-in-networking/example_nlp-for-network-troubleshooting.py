# NLP-based network log analysis for troubleshooting
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample network log message
log_message = "Network device ABC123 is experiencing high latency and packet loss."

# Tokenize and process the log message
nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(log_message)
filtered_message = [word for word in word_tokens if word.lower() not in stop_words]

# Analyze log message for network issues
if 'latency' in filtered_message or 'packet loss' in filtered_message:
    print("Network issue detected: High latency or packet loss.")
else:
    print("No network issues detected.")
