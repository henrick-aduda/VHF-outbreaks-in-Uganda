# README
## Step by step instructions
1. I went to NCBI Nucleotides page (https://www.ncbi.nlm.nih.gov/nuccore)\

2. I then extracted taxonomic ids for each of the viral hemorrhagic fevers of interest in Uganda. I did this by searching for key terms on NCBI taxonomy browser:(https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi).
*Key terms:* (Yellow fever virus,Crimean-Congo hemorrhagic fever virus,Ebola virus,Rift Valley fever virus,Marburg virus MBG)
 
| Taxonomic_id   | Viral hemorrhagic Fever      | 
| -------------  |:----------------------------:|
|  :11089:       | :Yellow Fever Virus:         | 
|  :11588:       | :Rift Valley Fever Virus     |
|  :11269:       | :Marburg Virus Disease       | 
|  :1980519:     | :Crimean Congo Fever         | 
|  :1570291:     | :Ebola Virus Disease         |

3. I then searched for each of the VHF sequences on NCBI.I placed in the taxonomic id,a parameter for country as well as sequence length to ensure I get the full length viral sequences and the partial sequences. I put in the maximum sequence
length parameter using information from ViralZone database (https://viralzone.expasy.org/). I toggled with the SLEN parameter placing different lengths each time to ensure i pick up all the full length sequences and the partial sequences.
(Example for Yellow fever virus : txid11089[Organism] AND 2000[SLEN]:12000[SLEN] AND Uganda)- 2 results for this search

4. I repeated the same process for each viral hemorrhagic fever. I then created a genbank file for all of of the sequences found for each viral hemorrhagic fever.I did this by Clicking on send to icon, selected on complete record checkbox, then on file checkbox and finally selected on Genbank(full) on the format dropdown arrow.

5. I saved each file with the appropriate name.At the end of each filename I indicated the number of sequence records that 
were obtained.For instance;(Yellow-fever-virus_2.gb)

6. I then went into my home directory, created a project folder for all of my data.(VHF-UG-Sequence-data). I then created a text file and saved it as VHF-outbreaks-UG.gb_list.txt.I did this because the python script that extracts the sequence data requires a list of the viral hemorraghic fever genbank names for easier downstream analysis later on.I then saved the filenames of each of the viral hemorrhagic fevers i obtained from
 my genbank search by using the linux command:

```bash
ls *.gb > VHF-outbreaks-UG.gb_list.txt 
```
7. I then ran the python extraction script drafted by Matthew Cotten.

```python
python GenBank_Henrick1.py Yellow-fever-virus_289.gb_list.txt 
#this python script uses python version 3.7.1. However its possible to modify to use previous python versions like 2.7
```
8. The python script outputs the sequence records for each viral hemorrhagic fever in a csv file. It also prints out the number of records for each viral hemorraghic fever.

9. Next process is now to fill in missing fields in the dataset obtained on the csv files. This will be done by checking for 
the missing information from publications on pubmed. I will also look at making summary graphs for all the information gathered so far.


Phew!!!Thats all for now!!
