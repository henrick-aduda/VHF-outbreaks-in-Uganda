#!/usr/local/bin/python
import sys
#sys.path.insert(0, "/Applications/anaconda")
import os.path
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import csv
import subprocess
import datetime
import string
import numpy as np #imported numpy so as to use the matrix feature.

#path_to_usearch = "/Applications/usearch"


# Step 1 parse genbank entries and write fasta file for use as usearch database
if len(sys.argv)!=2:
	print("Usage: python SLIM_dbmkr4e.py Genbank_entries_list_file")
	sys.exit()
	
print("SLIM_dbmkr4e.py running")
genbank_entries_list_file = sys.argv[1]
outprefix_set = os.path.splitext(genbank_entries_list_file)[0]

database_file_list=[]
genbank_files = open(genbank_entries_list_file, "rU")
motif_reader= csv.reader(genbank_files)
for row in motif_reader:
	database_file_list.append(row[0])
genbank_files.close()

for database_file in database_file_list:
	unique_records = []
	clean_up_list=[]
	pieces = database_file.split("_")
	outprefix = pieces[0]

	print_string_header = "Accession_number,Record_Date,Length,Country,Collection_date,Journal,Title,Authors,Comment"
	f2 = open(outprefix+"_summary.csv", "a")

	#print(file=f2, print_string_header)
	print(print_string_header, file=f2)  # Python 3.x
	f2.close()
	
	record_mat= np.zeros(shape=(0,9))
	count_index=0
	for record in SeqIO.parse(database_file, "genbank"):	
		count_index= count_index+1	
		accno = record.id
		organism = record.annotations["organism"]
		sequence = record.seq
		length_entry = len(record.seq)
		raw_description_string = record.description
		no_space_rds = raw_description_string.replace(" ", "_")
#		clean_rds= no_space_rds.translate(None, ',[].-/:=;')
		clean_rds= no_space_rds.translate(str.maketrans('','',string.punctuation))
		accession_number_pieces=accno.split('.')
		accession_number_clean= accession_number_pieces[0]	
		new_name = accession_number_clean+'_'+clean_rds
		new_name_80max= new_name[0:80]

		#print ("RECORD: ", record)
		#print (record.description)

		#print ("record.id: ", record.id)
		#print ("record.annotations: ", record.annotations)

		accno = record.id
		sequence = record.seq
		length_entry = len(record.seq)
		this_record_date = record.annotations["date"]

		print ("ANNOTATIONS: ", record.annotations.keys())
		print ("SOURCE: ", record.annotations.get("source"))
		print ("References: ", record.annotations.get("references"))
		print ("Journal: ", record.annotations.get("journal"))
		print("country: ", record.features[0].qualifiers.get('country'))
		print("collection_date: ", record.features[0].qualifiers.get('collection_date'))
		
		
		these_authors =  record.annotations['references'][0].authors.translate(str.maketrans('','',string.punctuation))
		this_title = record.annotations['references'][0].title.translate(str.maketrans('','',string.punctuation))
		this_journal =record.annotations['references'][0].journal.translate(str.maketrans('','',string.punctuation))
		this_comment = record.annotations['references'][0].comment.translate(str.maketrans('','',string.punctuation))
		this_country = record.features[0].qualifiers.get("country")
		this_collection_date = record.features[0].qualifiers.get("collection_date")


		if this_country is None:
			this_country = "Null"
		if this_collection_date is None:
			this_collection_date = "Null"
		this_country=this_country[0].translate(str.maketrans('','',string.punctuation))
		print(this_country)
		f = open(outprefix+"_file1.fas", "a") #Python 3.x
		#print >> f, '>'+new_name_80max
		print('>'+new_name_80max, file=f)  # Python 3.x
		#print >> f, sequence 		
		print(sequence, file=f)  # Python 3.x
		f.close()
		record_mat = np.append(record_mat, [[accno, this_record_date, length_entry,  this_country, this_collection_date[0], this_journal,this_title,these_authors,this_comment]], axis=0)
		entry_print_string= accno+","+this_record_date+","+str(length_entry)+","+this_journal+","+","+this_country[0]+","+this_collection_date[0]+","+this_comment
		#f2 = open(outprefix+"_summary.csv", "a")
		#print >> f2, entry_print_string	
		#print(entry_print_string, file=f2)  # Python 3.x
		np.savetxt(outprefix+"_summary.csv", record_mat, delimiter=",",fmt='%s', header=print_string_header)

		#f2.close()
	

	total_records = count_index
	#report summaries values
		
	now = datetime.datetime.now()
	year = str(now.year)
	month = str(now.month)
	day = str(now.day)
	new_file_name = outprefix+"_"+str(total_records)+"_"+year+"-"+month+"-"+day+".fas"
	
	print ("this_set: " + new_file_name )
	print ("final_unique_records: " +str(total_records) )

	# Step 5 rename file
	old_file_name = outprefix+"_file1.fas"
	rename_call = "mv "+old_file_name+" "+new_file_name
	subprocess.call(rename_call, shell=True)




print ("That\'s All Folks!")
