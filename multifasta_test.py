#!/usr/bin/env python3.8
import sys
import fileinput



infile = open('prev_algU_for_multifasta','r')
datafile = open('wholegenus_FAAcatfile','r')
data = datafile.readlines() #Read in entire data file, store as different lines



id_lines = [] #Find the lines that are ID values
id_list = [] #List of IDs

for j in range( 0,len(data)): #For each line in the file
    if data[j][0] == '>': #If the first character is '>'
        id_lines.append(j) #Add j to list of lines that are an ID
        temp = data[j].split()
        id_list.append(temp[0][1:]) #Add IDs to the list


numIDs = len(id_list)

#output_file = sys.stdout

#if len(sys.argv) == 1:
output = open(sys.argv[1],'w')
line = []
i = 0
for line in infile:
        if ('\t') in line:
                new_line = line.split('\t')
                subject_id = new_line[0]
                alignment = new_line[1]
                
                for j in range(0,numIDs):
                    if(subject_id == id_list[j]):
              
                        temp = ''
                
                        for k in range(id_lines[j]+1,id_lines[j+1]):
                            temp = temp+data[k]
                        temp = temp.replace('\n','')
                        break
         
                alignment = temp
                output.write('>' + subject_id + '\n' + alignment)
        i = i+1
        if i > 20:
            exit()

#with infile, open('test', 'w') as outfile:
    #temp = infile.read().replace("-", "")
    #outfile.write(temp)

infile.close()
