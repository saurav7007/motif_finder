from Bio import SeqIO


def load_fasta(file_path: str) -> dict[str, str]:
    """
    Load sequences from a FASTA file into a dictionary.

    Args:
        file_path (str): Path to the FASTA file.
    
    Returns:
        dict[str, str]: A dictionary with sequence IDs as keys and sequences as values.
    """
    sequences = {}

    for record in SeqIO.parse(file_path, "fasta"):
        sequences[record.id] = str(record.seq)
    
    return sequences