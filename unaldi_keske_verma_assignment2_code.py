# Assignment 2 - Umutcan Ünaldı (7025677), Shruti Verma (7022659), Nazlıgül Keske (7025902)

# Panda is called for DataFrame
import pandas as pd
# Bio and Bio.Align is specifically used for consensus calculations
from Bio import AlignIO as al
from Bio.Align import AlignInfo as alI

# Alignment is called with the format "clustal"
alignment = al.read("clustalo-E20211130-094437-0140-87358764-p2m.clustal_num", "clustal")
# Summary info is assigned
align = alI.SummaryInfo(alignment)
# Dumb_consensus function of the AlignInfo module is used to generate consensus
consensus = align.dumb_consensus()
print("Consensus of the clustal is:" + "\n" + consensus)

# This part is for reformatting the cluster text file into DataFrame
asd = list()  # Temporary list
dsa = list()  # Splitted list

# All eleven of this lists are assigned to each .pdb ( First is 1A9U_1|Chain, second is 4EYJ_A, etc.)
first = list()
second = list()
third = list()
fourth = list()
fifth = list()
sixth = list()
seventh = list()
eighth = list()
ninth = list()
tenth = list()
eleventh = list()

# Cluster file is called from the same directory with the script
with open('clustalo-E20211130-094437-0140-87358764-p2m.clustal_num', "r") as tryy:
    for line in tryy:
        umut = line.split()
        asd.append(umut)

    # This loop is written for only getting the alignment sequences and exclude headline, whitespaces etc.
    i = 3
    while i < len(asd):
        dsa.append(asd[i:(i + 11)])
        i += 13

# All of the for iterations are conducted for each pdb.
# Our appended list (dsa) had two substring in it. first string is the each paragraph in cluster file.
# First substring is the PDB, and second substring's [1] index is the sequence, these are extracted as
# lists
for i in range(0, len(dsa)):
    first.append(dsa[i][0][1])
first = ''.join(first)

for i in range(0, len(dsa)):
    second.append(dsa[i][1][1])
second = ''.join(second)

for i in range(0, len(dsa)):
    third.append(dsa[i][2][1])
third = ''.join(third)

for i in range(0, len(dsa)):
    fourth.append(dsa[i][3][1])
fourth = ''.join(fourth)

for i in range(0, len(dsa)):
    fifth.append(dsa[i][4][1])
fifth = ''.join(fifth)

for i in range(0, len(dsa)):
    sixth.append(dsa[i][5][1])
sixth = ''.join(sixth)

for i in range(0, len(dsa)):
    seventh.append(dsa[i][6][1])
seventh = ''.join(seventh)

for i in range(0, len(dsa)):
    eighth.append(dsa[i][7][1])
eighth = ''.join(eighth)

for i in range(0, len(dsa)):
    ninth.append(dsa[i][8][1])
ninth = ''.join(ninth)

for i in range(0, len(dsa)):
    tenth.append(dsa[i][9][1])
tenth = ''.join(tenth)

for i in range(0, len(dsa)):
    eleventh.append(dsa[i][10][1])
eleventh = ''.join(eleventh)

# This process took place because terminal wasn't showing all of the columns
# Instead it was showing "..." at the end of each row
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# An empty DataFrame has been created with the same col number with res number from alignment
# And, row number from how many .pdb files are there in alignment
alignment_df = pd.DataFrame(columns=['col ' + str(i) for i in range(1, len(first) + 1)],
                            index=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])


# A convert fuction is created to turn strings into lists separated by characters
def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


# All of the converted strings ( now lists) are inserted into empty DataFrame for each index.
alignment_df.loc['1'] = Convert(first)
alignment_df.loc['2'] = Convert(second)
alignment_df.loc['3'] = Convert(third)
alignment_df.loc['4'] = Convert(fourth)
alignment_df.loc['5'] = Convert(fifth)
alignment_df.loc['6'] = Convert(sixth)
alignment_df.loc['7'] = Convert(seventh)
alignment_df.loc['8'] = Convert(eighth)
alignment_df.loc['9'] = Convert(ninth)
alignment_df.loc['10'] = Convert(tenth)
alignment_df.loc['11'] = Convert(eleventh)

# print(alignment_df)


print(alignment_df)

# This one prints all of the occurrences for each position
# for i in range(1, len(first) + 1):
#    print(alignment_df['col '+str(i)].value_counts())

# We couldn't do the 4th question by this method, so we tried a different approach.
# That approach is stored in the directory as second .py code only for 4th question.