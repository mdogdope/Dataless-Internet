import imaplib
import email

ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "" + ORG_EMAIL
FROM_PWD    = ""
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993


mail = imaplib.IMAP4_SSL(SMTP_SERVER)
mail.login(FROM_EMAIL,FROM_PWD)
mail.select('INBOX')

type, data = mail.search(None, 'ALL')
mail_ids = data[0]
id_list = mail_ids.split()

first_email_id = int(id_list[0])
latest_email_id = int(id_list[-1])
print(id_list)

for i in range(latest_email_id,first_email_id, -1):
	typ, data = mail.fetch(i, '(RFC822)' )

	for response_part in data:
		if isinstance(response_part, tuple):
			raw_msg = email.message_from_string(response_part[1])
			#print(raw_msg)
			email_subject = raw_msg['subject']
			email_from = raw_msg['from']
			#email_msg = raw_msg['']
			print(email_from)
			
			
			
			
