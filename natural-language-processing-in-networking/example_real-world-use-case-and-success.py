# NLP-based network documentation automation
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample network documentation automation task
documentation_task = "Create documentation for the new network configuration of VLAN 10."

# Tokenize and process the documentation task
nltk.download('stopwords')
nltk.download('punkt')

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(documentation_task)
filtered_task = [word for word in word_tokens if word.lower() not in stop_words]

# Generate network documentation based on the task
if 'documentation' in filtered_task and 'VLAN' in filtered_task:
    vlan_number = filtered_task[filtered_task.index('VLAN') + 1]
    print(f"Documentation created for VLAN {vlan_number}.")
else:
    print("Documentation task not recognized.")
