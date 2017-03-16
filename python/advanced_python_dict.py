import csv
import re

print ('Q6.  *************')

def make_faculty_dict(): # Q6
	faculty_dict = {}
	with open('faculty.csv', 'r') as f:
		reader = csv.reader(f, delimiter=',')
		header = next(reader)

		for row in reader:
			names = row[0]
			degrees = row[1].strip()
			titles = row[2]
			emails = row[3]

			last = re.findall(r'[A-Z][a-z]*\S$', names)

			for item in last:
				if item not in faculty_dict:
					faculty_dict[item] = [degrees, titles, emails]
				else:
					faculty_dict[item] = [[degrees, titles, emails], faculty_dict[item]]

	return faculty_dict

for k, v in sorted(make_faculty_dict().items())[:3]:
	print (k, v)

print (make_faculty_dict())

print ('Q7.  *************')

def make_professor_dict(): # Q7
	professor_dict = {}
	with open('faculty.csv', 'r') as f:
		reader = csv.reader(f, delimiter=',')
		header = next(reader)

		for row in reader:
			names = row[0]
			degrees = row[1].strip()
			titles = row[2]
			emails = row[3]

			last = re.findall(r'[A-Z][a-z]*\S$', names)
			first = re.findall(r'^[A-Z][a-z]*\S*', names)

			full_name = zip(first, last)

			for item in full_name:
				professor_dict[item] = [degrees, titles, emails]

	return professor_dict

for k, v in sorted(make_professor_dict().items())[:3]:
	print (k, v)

print ('Q8. ***************')

for k, v in sorted(make_professor_dict().items(), key=lambda k: k[0][1])[:3]: # Q8
	print (k, v)

print ('***************')

print (make_professor_dict())