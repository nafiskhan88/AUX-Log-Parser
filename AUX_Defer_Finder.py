#!/usr/bin/env python


import sys, os
#import timeit
#import time


#f=open(sys.argv[1], 'r')
#start = time.time()
#start_time = timeit.default_timer()



File_Buffer = open("MAX_Device_Exceeded_Astro_1842_AUX_Defer_in_RxInfo.txt", 'r') 

#File_Buffer = open(sys.argv[1], 'r')
    ## Open the file with read only permit
    #File_Buffer = open('Text_File.txt')
    
#text = File_Buffer.read()
#print len(text)

raw_filename = File_Buffer.name

filename_length= len (raw_filename)

desired_filename = raw_filename[:(filename_length-4)]

new_write_filename = desired_filename + '_Only_AUX_Defer'+'.txt'

print new_write_filename

#print desired_filename

#b = c +'_Only_AUX_Defer'
#print b

lines = File_Buffer.readlines()     # this will read all lines of the text file and save it in the lines variable. 
                                    #will be used to access next line of "I2C_R_MOT:"
print "Total number of lines:" , len(lines) 
#print lines [5]

File_Buffer.close()                 #close file

target = open(new_write_filename, 'w')     #prepare file for writing

#target = open(sys.argv[2], 'w')



count = 0

defer_dict = dict()

f = open(raw_filename, 'r')          #opens the AUX log again

#f = open(sys.argv[1], 'r')


for line in f.readlines():
    count = count + 1
    if "DP_Read" in line or "DP_WRITE" in line:
        ls = lines[count].split()
        #print ls
        if ls != [] and ls[4] == 'AUX_DEFER' :
            #print "AUX Deffered DPCD Lines : ", line
            target.write (line)
            defer_aux  = line.split()
            #print defer_aux[6]
            dpcd = defer_aux[6]
            temp = dpcd
            time_temp = defer_aux [2]
            if dpcd not in defer_dict:
                defer_dict[dpcd] = 1
            else:
                defer_dict[dpcd] += 1
                #if temp == dpcd :
                    #print defer_aux[2]

#print "DPCD Address: AUX_Defer_Occured",  defer_dict
target.write("\n")
target.write ("DPCD Address: Number of time AUX Defer occured \n")
target.close()


with open(new_write_filename,'a') as fw:
    fw.writelines('{}:{}         \n'.format(k,v) for k, v in defer_dict.items())
    fw.close()
#target.write ('{}:{}\n'.format(k,v) for k, v in target.defer_dict())


