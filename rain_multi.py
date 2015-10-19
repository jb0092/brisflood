#-------------------------------------------------------------------------------
# Name:        rain_multi.py
# Purpose:
#
# Author:      Jacinda.Boully
#
# Created:     12/10/2015
# Copyright:   (c)
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os, glob, csv
import numpy as np

# Folder where csv's live
csv_folder = r'K:\_Personal\JAB\hde'

# Folder where the outputs will live
out_csv_folder = r'K:\_Personal\JAB\hde\output'
m_factor = float(30)

def main():

    # Get a list of all the csv's in the folder
    files = glob.glob(csv_folder +  '\*.csv')

    # Loop through each csv in the list (This is where the action happens)
    for f in files:

        # Get the file name
        tmp,file_name = os.path.split(f)

        # Setup empty list for appending
        rf_id = []
        rf_date=[]
        rf_mm =[]

        # IF USING NUMPY
        # Read the data into a numpy array (GOOD FOR DATA ONLY. NOT SO GOOD FOR DATA + STRINGS)
        #data  = np.genfromtxt(f, dtype=("|S16", '|S20', float), delimiter=",")

        # Using CSV Reader
        with open(f, 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                try:
                    rf_id.append(row[0])        # This is a list
                    rf_date.append(row[1])      # This is a list
                    rf_mm.append(row[2])        # This is a list

                    #print row
                except:
                    print 'ERROR - extracting chainage from line: '

        # Multiply the relevant column by X
        for i,d in enumerate(rf_mm):
            rf_mm[i]= float(rf_mm[i]) * m_factor

        # Write the new data back out to csv
        outdata = zip(rf_id,rf_date,rf_mm)  # Puts it back in a tuple (easy to output)

        # Output to csv
        with open(os.path.join(out_csv_folder,file_name),'w+') as outcsvfile:
            for row in outdata:
                outcsvfile.write('%(rainid)s,%(raindate)s,%(rain)6.2f\n'  % \
                    {"rainid": row[0],"raindate": row[1],"rain": row[2]})

        print('File ' + file_name + ' has been successfully processed...')


if __name__ == '__main__':
    main()
