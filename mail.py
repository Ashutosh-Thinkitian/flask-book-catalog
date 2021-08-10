import smtplib as s

ob = s.SMTP("smtp.gmail.com", 587)

#   put connection smtp to TLS mode -> encrypted mode
ob.starttls()

ob.login("ashutosh.patil@thinkitive.com", "#MePatil1112thinkitive")

subject = "This is testing mail from python"
body =" Testing subject "

message ="Subject:{}\n\n{}".format(subject, body)
#   print(message)

# for send mail
listOfAddress = ["ashutosh.patil@thinkitive.com", "ankit.thapa@thinkitive.com"]
ob.sendmail("ashutosh.patil@thinkitive.com", listOfAddress, message)

ob.quit()