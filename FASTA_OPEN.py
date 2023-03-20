from Bio import SeqIO

def open_fasta_as_dict(input_file):
    seq_dict = {rec.id : str(rec.seq) for rec in SeqIO.parse(open(input_file), "fasta")}
    return seq_dict
def open_fasta_as_list(input_file):
    seq_dict = [str(rec.seq) for rec in SeqIO.parse(open(input_file), "fasta")]
    return seq_dict