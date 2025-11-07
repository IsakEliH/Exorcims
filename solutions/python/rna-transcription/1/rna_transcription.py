def to_rna(dna_strand):
    
    RNA: dict = {
        "G" : "C",
        "C" : "G",
        "T" : "A",
        "A" : "U"
    }

    final_str = ""
    for strand in dna_strand:
        final_str += RNA[strand]

    return final_str