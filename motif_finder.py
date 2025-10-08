import argparse
from core.motif_search import overlapping_motif, highlight_motifs
from core.sequence_utils import load_fasta


def find_overlapping_motif(infile: str, motif: str) -> None:
    """Run the overlapping motif search."""
    seqs = load_fasta(infile)
    for seq_id, seq in seqs.items():
        positions = overlapping_motif(seq, motif)
        highlighted = highlight_motifs(seq, positions)
        print(f"\n> {seq_id}")
        print(f"Motif '{motif}' found at positions: {positions}")
        print(f"Highlighted sequence:\n{highlighted}\n")


def main():
    parser = argparse.ArgumentParser(
        prog="motif_finder",
        description="A tool for finding motifs in DNA sequences."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- Subcommand: find_overlapping_motif ---
    parser_overlap = subparsers.add_parser(
        "find_overlapping_motif",
        help="Find overlapping motifs in a FASTA file."
    )
    parser_overlap.add_argument("--infile", required=True, help="Path to input FASTA file")
    parser_overlap.add_argument("--motif", required=True, help="Motif sequence to search for")

    args = parser.parse_args()

    if args.command == "find_overlapping_motif":
        find_overlapping_motif(args.infile, args.motif)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
