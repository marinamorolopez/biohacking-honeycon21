# biohacking-honeycon21
This repository includes the slides of the public presentation 'Biohacking con Python' in the Hack&Beers of HoneyCON21 (PPTX and PDF format) and both the code and files used for the practical case (slide 23 onwards).

## Installation
You simply have to download and save the .py and fasta files in the same folder. If you get your own fasta files from a database as [NCBI](https://www.ncbi.nlm.nih.gov/) just save them in that folder too.

## Usage
First you'll have to introduce the file name of your gene of interest (including its file extension, e.g. 'filename.fasta'). Then introduce the mutation type (knock-in or knock-out) as in/out. If case of a knock-in, you'll have to specify if the DNA change is in the middle or at the end of the gene as mid/end. In case of a knock-in in the middle of the gene, you'll have to introduce the position of the mutation and the new base in that position. In case of a knock-in at the end of the gene, you'll have to introduce the filename with the plasmid of interest (the DNA sequence you want to add to that gene). Then you'll have three .txt files saved in the same folder with the RNA guide, the DNA mold and the mutated sequence.

## Constributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
