from core import load_fasta, overlapping_motif, highlight_motifs

def main(file_path: str = "resources/data/dna2.fasta", motif: str = "ATG") -> None:
    """Load sequences and run motif search, printing results."""
    seqs = load_fasta(file_path)
    for seq_id, seq in seqs.items():
        positions = overlapping_motif(seq, motif)
        highlight_seq = highlight_motifs(seq, positions)
        print(f"Motifs in {seq_id} is {highlight_seq}.")

if __name__ == "__main__":
    main()