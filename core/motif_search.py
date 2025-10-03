def overlapping_motif(seq_dictionary: dict[str, str], motif: str) -> dict[str, list[int]]:
    """
    Find all occurrences of a motif in a given sequence using Sliding windown Method.

    Args:
        dict[str, str]: A dictionary with sequence IDs as keys and sequences as values.
        motif (str): The motif to search for.
    
    Returns:
        dict[str, list[int]]: A dictionary with the sequence IDs as the key and a list of starting positions (1-based) as values.
    """
    motif_pos = {}
    motif = motif.upper()

    for seq_id, seq in seq_dictionary.items():
        seq = seq.upper()

