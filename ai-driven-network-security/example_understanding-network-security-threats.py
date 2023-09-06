# Simulate a phishing email detector
import re

email_text = "This is a phishing email trying to steal your information. Please do not click on any links."
if re.search(r'phishing|steal|click', email_text):
    print("Potential phishing email detected!")
else:
    print("Email is safe.")
