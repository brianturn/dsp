# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

def points_diff(filename):
	# create a dictionary with a key of team name and a value of the absolute difference between goals for/against
	d = dict()
	for line in filename:
		columns = line.strip().split(',')
		if columns[0] != 'Team':
			d[columns[0]] = abs(int(columns[-2]) - int(columns[-3]))
	return d

def sort_dict():
	# sort the dictionary as a list and display the first result
	d = points_diff(filename)
	results = list(d.items())
	return sorted(results, key=lambda points: points[1])[0]

filename = open('football.csv', 'r')
print (sort_dict())