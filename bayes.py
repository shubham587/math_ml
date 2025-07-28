

total_emails = 1000
emails_with_free = 300
spam_emails = 400
spam_and_free = 120

P_spam = spam_emails / total_emails
P_free = emails_with_free / total_emails
P_free_given_spam = spam_and_free / spam_emails

P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print(f"P(Spam | Free): {P_spam_given_free:.4f}")
