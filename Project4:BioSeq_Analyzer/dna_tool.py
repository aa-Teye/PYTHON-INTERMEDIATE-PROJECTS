def analyze_dna(sequence):
    # Convert to uppercase to handle 'atgc' or 'ATGC'
    sequence = sequence.upper()
    
    # 1. Nucleotide Counting
    # This creates a dictionary of how many times each base appears
    counts = {base: sequence.count(base) for base in "ATGC"}
    
    # 2. GC Content Calculation
    # Vital for determining DNA stability in Bioinformatics
    gc_count = counts['G'] + counts['C']
    gc_content = (gc_count / len(sequence)) * 100
    
    # 3. Transcription (DNA -> RNA)
    # In nature, Thymine (T) is replaced by Uracil (U)
    rna_sequence = sequence.replace('T', 'U')
    
    # Print the results in a clean format
    print(f"\n--- Analysis for: {sequence} ---")
    print(f"Nucleotide Counts: {counts}")
    print(f"GC Content: {gc_content:.2f}%")
    print(f"RNA Sequence: {rna_sequence}")

# Test the tool with a sample sequence
if __name__ == "__main__":
    sample = "ATGCGATCGTAGCTAG"
    analyze_dna(sample)
