import csv
import re

print ()

# Q1.
print ('Q1.')
def degrees():
	with open('faculty.csv') as file:
		reader = csv.reader(file, delimiter=',')
		header = next(reader)

		degrees = []
		for row in reader:
			degree = row[1].strip()
			match = re.search('\.', degree)
			if match:
				 degrees.append(degree.replace(match.group(), ""))
			else:
				degrees.append(degree)
		
		results = []
		for degree in degrees:
			if re.findall('[A-Z]', degree):
				results.extend(degree.split())

		degree_dict = {}
		for d in results:
			degree_dict[d] = degree_dict.get(d, 0) + 1
		
		print ("There are {} types of degrees.".format(len(sorted(degree_dict.keys()))))
		print ("Here are the frequencies of each degree:")

		for k, v in sorted(degree_dict.items(), key=lambda v: v[1], reverse=True):
			print (k,'=', v)

degrees()
print ()

#Q2.
print('Q2')
def titles():
	with open('faculty.csv') as file:
		reader = csv.reader(file, delimiter=',')
		header = next(reader)

		titles = []
		title_dict = {}
		for row in reader:
			title = row[2]
			match = re.search('\sis\s', title)
			if match:
				title = title.replace(match.group(), ' of ')
			titles.append(title)
			
		for title in titles:
				title_dict[title] = title_dict.get(title, 0) + 1

		print ("There are {} titles.".format(len(sorted(title_dict.keys()))))
		print ("Here are the frequencies of each title:")

		for k, v in sorted(title_dict.items(), key=lambda v: v[1], reverse=True):
			print (k,'=', v)

titles()
print ()

# Q3.
print ("Q3 Using regular expressions:")

f = open('faculty.csv', 'r')
emails = []
for line in f:
	email = re.search('[A-Za-z]*@\S*[a-zA-Z]', line)
	if email:
		emails.append(email.group())
print (emails)
print ()

print ("Q3 Without using regular expressions:")

def emails():
	with open('faculty.csv') as file:
		reader = csv.reader(file, delimiter=',')
		header = next(reader)

		email_list = []
		for row in reader:
			email_list.append(row[3])

		print (email_list)

emails()
print ()

# Q4.
print ('Q4')

f = open('faculty.csv', 'r')

domains = []
for line in f:
	domain = re.search('@\S*[a-zA-Z]', line)
	if domain:
		domains.append(domain.group())

print ("There are {} unique email domains:".format(len(set(domains))))
print (list(set(domains)))
