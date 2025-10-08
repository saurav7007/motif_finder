def overlapping_motif(sequence: str, motif: str) -> list[tuple[int, int]]:
    """
    Find all starting positions of a motif in a given sequence using a sliding-window method.

    Args:
        sequence (str): A DNA sequence string.
        motif (str): The motif to search for.

    Returns:
        list[int]: A list of starting positions (1-based).
    """
    motif = motif.upper()
    sequence = sequence.upper()

    if not motif or not sequence or len(motif) > len(sequence):
        return []
    
    return [(pos + 1, pos + 3) for pos in range(len(sequence) - len(motif) + 1) if sequence[pos:pos + len(motif)] == motif]


def highlight_motifs(sequence, motifs_positions, color_code="\033[93m"):
    """
    Highlights motifs in the given sequence.

    Args:
        sequence (str): The input text.
        motifs_positions (list of tuples): List of (start, end) positions for motifs.
        color_code (str): ANSI color code for highlighting. Default is yellow.

    Returns:
        str: Text with motifs highlighted.
    """
    RESET = "\033[0m"
    highlighted_text = ""
    last_index = 0

    for start, end in sorted(motifs_positions):
        # Add text before the motif
        highlighted_text += sequence[last_index:start]
        # Add highlighted motif
        highlighted_text += f"{color_code}{sequence[start - 1:end]}{RESET}"
        last_index = end

    # Add remaining text after the last motif
    highlighted_text += sequence[last_index:]
    return highlighted_text