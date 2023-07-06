import os 
import csv 

CSV_PATH = os.path.join("Resources", "election_data.csv")

BALLET_IDX = 0 
COUNTY_IDX = 1
CAND_IDX = 2
ballet_ls = []
cand_ls = []
winner = ""
full_cand_ls = []

cand_name = "none"
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        current_ballet = row[BALLET_IDX]
        ballet_ls.append(current_ballet)

        current_cand = row[CAND_IDX]
        full_cand_ls.append(current_cand)

        if current_cand != cand_name:
            cand_name = current_cand
            cand_ls.append(cand_name)

cand_ls_nd = []


for item in cand_ls:
    if item not in cand_ls_nd:
        cand_ls_nd.append(item)
    
first_c = cand_ls_nd[0]
second_c = cand_ls_nd[1]
third_c = cand_ls_nd[2]


total_ballots = len(ballet_ls)
can_1 = full_cand_ls.count("Charles Casper Stockham")
can_2 = full_cand_ls.count("Diana DeGette")
can_3 = full_cand_ls.count("Raymon Anthony Doane")
winner_ls = [can_1,can_2, can_3]
if max(winner_ls) == can_1:
    winner = "Charles Casper Stockham"
if max(winner_ls) == can_2:
    winner = "Diana DeGette"
if max(winner_ls) == can_3:
    winner = "Raymon Anthony Doane"
percent_votes1 = can_1/total_ballots
percent_votes2 = can_2/total_ballots
percent_votes3 = can_3/total_ballots
votes1 = percent_votes1 * 100
votes2 = percent_votes2 * 100
votes3 = percent_votes3 * 100


f = open("PyPoll_anlys.txt", "w")
# printing out the total votes and percentages
f.write("Election results\n")
f.write("-------------------------------------------------------\n")
f.write("\n")
f.write("Total votes: {}\n" .format(total_ballots))
f.write("\n")
f.write("-------------------------------------------------------\n")
f.write("Charles Casper Stockham: ({})" .format(can_1))
f.write("{:.2f}%\n" .format(votes1))
f.write("\n")
f.write("Diana DeGette: ({})" .format(can_2))
f.write("{:.2f}%\n" .format(votes2))
f.write("\n")
f.write("Raymon Anthony Doane: ({})" .format(can_3))
f.write("{:.2f}%\n" .format(votes3))
f.write("\n")
f.write("-------------------------------------------------------\n")
f.write("Winner: {}" .format(winner))

f = open("PyPoll_anlys.txt", "r")
print(f.read())       

f.close()