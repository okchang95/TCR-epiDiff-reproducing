import numpy as np

from src.vocabs import MOST_FREQ_CODON, ONE_HOT_ENCODING_TABLE


class Preprocessor:
    """
    TODO: 실제 데이터 전처리 시에는 scikit-learn의 OneHotEncoder를 사용 (데이터가 df)
    근데 음 실제로 학습할 때의 원핫 인코딩이랑 인퍼런스때 같아야하지 않나 (나중에 생각)
    """

    def __init__(self):
        pass

    def aa2codon(self, aa: str) -> str:
        """
        aa를 가장 높은 빈도의 코돈으로 변환합니다.
        """
        return MOST_FREQ_CODON[aa]

    def codon2one_hot(self, codon: str) -> np.ndarray:
        """
        코돈을 one-hot encoding으로 변환합니다.
        0: A, 1: T, 2: G, 3: C
        """
        return np.array([ONE_HOT_ENCODING_TABLE[c] for c in codon])

    def aa_seq2one_hot(self, aa_seq: str) -> np.ndarray:
        """
        aa 시퀀스를 one-hot encoding으로 변환합니다.
        output shape: (seq_len(`len(aa_seq)`), codon_len(3), one_hot_dim(4))
        """
        return np.array([self.codon2one_hot(self.aa2codon(aa)) for aa in aa_seq])


if __name__ == "__main__":
    preprocessor = Preprocessor()
    # aa = "A"
    # codon = preprocessor.aa2codon(aa)
    # print(codon)

    # one_hot = preprocessor.codon2one_hot(codon)
    # print(one_hot)

    aa_seq = "ACGTACGTACGT"
    one_hot = preprocessor.aa_seq2one_hot(aa_seq)
    print(one_hot)
    print(one_hot.shape)  # (seq_len, codon_len, one_hot_dim)
