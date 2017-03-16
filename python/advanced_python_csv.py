import csv
import re

# Using regular expressions
write_file = open('emails.csv', 'w')
f = open('faculty.csv', 'r')

for line in f:
	email = re.search('[A-Za-z]*@\S*[a-zA-Z]', line)
	if email:
		write_file.write((email.group() + '\n'))
write_file.close()

# Using csv reader:
with open('faculty.csv') as file:
	reader = csv.reader(file, delimiter=',')
	header = next(reader)

	emails = []
	for row in reader:
		email = row[3]
		emails.append(email)

write_file = open('emails.csv', 'w')
writer = csv.writer(write_file)

for i in range(len(emails)):
	email = emails[i]
	writer.writerow([email])

write_file.close()