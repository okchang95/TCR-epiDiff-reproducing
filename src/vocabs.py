"""
DNA codon table - Human (Homo sapiens)
ref: https://www.vectorbuilder.kr/tool/codon-table.html
- image/codon_table.png: 코돈 테이블 이미지

all tabls:
- STANDARD_AMINO_ACIDS: 표준 아미노산 리스트 (Stop 제외)
- CODON_TABLE: 전체 코돈 테이블
- MOST_FREQ_CODON: 각 아미노산별 가장 높은 빈도의 코돈
- AMINO_ACID_TO_CODONS_ALL: 아미노산별 전체 코돈 리스트 매핑
"""

# 표준 아미노산 리스트 (Stop 제외)
STANDARD_AMINO_ACIDS = [
    "A",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "K",
    "L",
    "M",
    "N",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "V",
    "W",
    "Y",
]

# 전체 코돈 테이블
CODON_TABLE = {
    # Phe (F) - Phenylalanine
    "TTT": {"aa": "F", "frequency": 0.46},
    "TTC": {"aa": "F", "frequency": 0.54},
    # Leu (L) - Leucine
    "TTA": {"aa": "L", "frequency": 0.08},
    "TTG": {"aa": "L", "frequency": 0.13},
    "CTT": {"aa": "L", "frequency": 0.13},
    "CTC": {"aa": "L", "frequency": 0.20},
    "CTA": {"aa": "L", "frequency": 0.07},
    "CTG": {"aa": "L", "frequency": 0.40},
    # Ile (I) - Isoleucine
    "ATT": {"aa": "I", "frequency": 0.36},
    "ATC": {"aa": "I", "frequency": 0.48},
    "ATA": {"aa": "I", "frequency": 0.16},
    # Met (M) - Methionine (Start codon)
    "ATG": {"aa": "M", "frequency": 1.0},
    # Val (V) - Valine
    "GTT": {"aa": "V", "frequency": 0.18},
    "GTC": {"aa": "V", "frequency": 0.24},
    "GTA": {"aa": "V", "frequency": 0.12},
    "GTG": {"aa": "V", "frequency": 0.46},
    # Ser (S) - Serine
    "TCT": {"aa": "S", "frequency": 0.18},
    "TCC": {"aa": "S", "frequency": 0.22},
    "TCA": {"aa": "S", "frequency": 0.15},
    "TCG": {"aa": "S", "frequency": 0.05},
    "AGT": {"aa": "S", "frequency": 0.15},
    "AGC": {"aa": "S", "frequency": 0.24},
    # Pro (P) - Proline
    "CCT": {"aa": "P", "frequency": 0.29},
    "CCC": {"aa": "P", "frequency": 0.33},
    "CCA": {"aa": "P", "frequency": 0.28},
    "CCG": {"aa": "P", "frequency": 0.11},
    # Thr (T) - Threonine
    "ACT": {"aa": "T", "frequency": 0.25},
    "ACC": {"aa": "T", "frequency": 0.36},
    "ACA": {"aa": "T", "frequency": 0.28},
    "ACG": {"aa": "T", "frequency": 0.11},
    # Ala (A) - Alanine
    "GCT": {"aa": "A", "frequency": 0.28},
    "GCC": {"aa": "A", "frequency": 0.40},
    "GCA": {"aa": "A", "frequency": 0.23},
    "GCG": {"aa": "A", "frequency": 0.11},
    # Tyr (Y) - Tyrosine
    "TAT": {"aa": "Y", "frequency": 0.44},
    "TAC": {"aa": "Y", "frequency": 0.56},
    # Stop codons
    "TAA": {"aa": "*", "frequency": 0.61},
    "TAG": {"aa": "*", "frequency": 0.09},
    "TGA": {"aa": "*", "frequency": 0.30},
    # His (H) - Histidine
    "CAT": {"aa": "H", "frequency": 0.42},
    "CAC": {"aa": "H", "frequency": 0.58},
    # Gln (Q) - Glutamine
    "CAA": {"aa": "Q", "frequency": 0.27},
    "CAG": {"aa": "Q", "frequency": 0.73},
    # Asn (N) - Asparagine
    "AAT": {"aa": "N", "frequency": 0.47},
    "AAC": {"aa": "N", "frequency": 0.53},
    # Lys (K) - Lysine
    "AAA": {"aa": "K", "frequency": 0.43},
    "AAG": {"aa": "K", "frequency": 0.57},
    # Asp (D) - Aspartic acid
    "GAT": {"aa": "D", "frequency": 0.46},
    "GAC": {"aa": "D", "frequency": 0.54},
    # Glu (E) - Glutamic acid
    "GAA": {"aa": "E", "frequency": 0.42},
    "GAG": {"aa": "E", "frequency": 0.58},
    # Cys (C) - Cysteine
    "TGT": {"aa": "C", "frequency": 0.46},
    "TGC": {"aa": "C", "frequency": 0.54},
    # Trp (W) - Tryptophan
    "TGG": {"aa": "W", "frequency": 1.0},
    # Arg (R) - Arginine
    "CGT": {"aa": "R", "frequency": 0.11},
    "CGC": {"aa": "R", "frequency": 0.19},
    "CGA": {"aa": "R", "frequency": 0.11},
    "CGG": {"aa": "R", "frequency": 0.20},
    "AGA": {"aa": "R", "frequency": 0.21},
    "AGG": {"aa": "R", "frequency": 0.20},
    # Gly (G) - Glycine
    "GGT": {"aa": "G", "frequency": 0.16},
    "GGC": {"aa": "G", "frequency": 0.34},
    "GGA": {"aa": "G", "frequency": 0.25},
    "GGG": {"aa": "G", "frequency": 0.25},
}

# 각 아미노산별 가장 높은 빈도의 코돈 (하드코딩)
MOST_FREQ_CODON = {
    "F": "TTC",  # 0.54
    "L": "CTG",  # 0.40
    "I": "ATC",  # 0.48
    "M": "ATG",  # 1.0
    "V": "GTG",  # 0.46
    "S": "AGC",  # 0.24
    "P": "CCC",  # 0.33
    "T": "ACC",  # 0.36
    "A": "GCC",  # 0.40
    "Y": "TAC",  # 0.56
    "*": "TAA",  # 0.61 (Stop codon)
    "H": "CAC",  # 0.58
    "Q": "CAG",  # 0.73
    "N": "AAC",  # 0.53
    "K": "AAG",  # 0.57
    "D": "GAC",  # 0.54
    "E": "GAG",  # 0.58
    "C": "TGC",  # 0.54
    "W": "TGG",  # 1.0
    "R": "AGA",  # 0.21
    "G": "GGC",  # 0.34
}

# 역방향 매핑: 아미노산 -> 전체 코돈 리스트
AMINO_ACID_TO_CODONS_ALL = {}
for codon, info in CODON_TABLE.items():
    aa = info["aa"]
    if aa not in AMINO_ACID_TO_CODONS_ALL:
        AMINO_ACID_TO_CODONS_ALL[aa] = []
    AMINO_ACID_TO_CODONS_ALL[aa].append(codon)


def get_amino_acid(codon: str) -> str:
    """코돈에서 아미노산을 반환합니다."""
    return CODON_TABLE.get(codon, {}).get("aa", "")


def get_most_freq_codon(aa: str) -> str:
    """아미노산에서 가장 높은 빈도의 코돈을 반환합니다."""
    return MOST_FREQ_CODON.get(aa, "")


def get_frequency(codon: str) -> float:
    """코돈의 사용 빈도를 반환합니다."""
    return CODON_TABLE.get(codon, {}).get("frequency", 0.0)


if __name__ == "__main__":
    print(get_most_freq_codon("A"))
