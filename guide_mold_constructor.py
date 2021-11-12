# -*- coding: utf-8 -*-

"""

Created on Tue Nov  9 17:56:55 2021
@author: Marina Moro López

"""

def main():
    
    gene_file_name = input("Introduce gene file name (e.g. mygene.fasta): ")
    gene_file = open(gene_file_name, 'r')
    gene_seq = gene_file.readlines()[1:]
    gene_seq = ''.join(gene_seq)
    gene_seq = gene_seq.replace('\n', '')
    gene_file.close()

    mutation_type = input("Introduce mutation type (in/out): ")
    knockin_type = ""
    
    if mutation_type == "in":
        knockin_type = input("Introduce the knock-in position in the gene (mid/end): ")
    
    if knockin_type == "mid":
        DNA_guide, mutated_gene_seq, mold = knock_in_mid(gene_seq)
    elif knockin_type == "end":
        DNA_guide, mutated_gene_seq, mold = knock_in_end(gene_seq)
    else:
        DNA_guide, mutated_gene_seq, mold = knock_out(gene_seq)

    mutated_gene_file = open('MUTATED_SEQUENCE.txt', 'w')
    mutated_gene_file.write(mutated_gene_seq)
    mutated_gene_file.close()

    guide_file = open('GUIDE.txt', 'w')
    guide_file.write(DNA_to_RNA(DNA_guide))
    guide_file.close()

    mold_file = open('MOLD.txt', 'w')
    mold_file.write(mold)
    mold_file.close()


def knock_in_mid(gene_seq):
    
    mutation_position = int(input("Introduce the numeric position of the mutation base (e.g. 1, 25, 203): "))
    mutation_base = input("Introduce the new base corresponding to the defined mutation position (A/T/G/C): ")
            
    DNA_guide = gene_seq[mutation_position-25:mutation_position+25]
    mutated_gene_seq = gene_seq[:mutation_position-1] + mutation_base + gene_seq[mutation_position:]
    mold = mutated_gene_seq[mutation_position-25:mutation_position+25]
    
    return DNA_guide, mutated_gene_seq, mold


def knock_in_end(gene_seq):

    plasmid_file_name = input("Introduce plasmid file name (e.g. myplasmid.fasta): ")
    plasmid_file = open(plasmid_file_name, 'r')
    plasmid_seq = plasmid_file.readlines()[1:]
    plasmid_seq = ''.join(plasmid_seq)
    plasmid_seq = plasmid_seq.replace('\n', '')
    plasmid_file.close()
            
    DNA_guide = gene_seq[len(gene_seq)-50:len(gene_seq)]
    mutated_gene_seq = gene_seq + plasmid_seq
    mold = DNA_guide + plasmid_seq
    
    return DNA_guide, mutated_gene_seq, mold


def knock_out(gene_seq):
    
    DNA_guide = gene_seq
    mutated_gene_seq = ""
    mold = ""
    
    return DNA_guide, mutated_gene_seq, mold


def DNA_to_RNA(DNA_guide):
    
    RNA_guide = ""
    for base in DNA_guide:
        if base == "T":
            RNA_guide += "A"
        elif base == "A":
            RNA_guide += "U"
        elif base == "C":
            RNA_guide += "G"
        elif base == "G":
            RNA_guide += "C"
    
    return RNA_guide


main()