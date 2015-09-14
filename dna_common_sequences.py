from itertools import combinations
from copy import deepcopy

POSSIBLE_ELEMENTS = 'ATCG'

CACHE = {}

def findfirst(sequence, start_index, target):
    key = sequence+str(start_index)+target
    if sequence+str(start_index)+target in CACHE:
        return CACHE[key]
    for i in range(start_index, len(sequence)):
        if sequence[i] == target:
            CACHE[key] = [i]
            return CACHE[key]
    return []


def common(first, second):
    if len(first) < len(second):
        first, second = second, first
    results = set([])

    open_set = set([])
    closed_set = set([])
    longest_matches = 0
    for target in POSSIBLE_ELEMENTS:
        index_of_first = findfirst(first, 0, target)
        index_of_second = findfirst(second, 0, target)

        for j in index_of_first:
            for k in index_of_second:
                open_set.add((tuple([j]), tuple([k])))

    length_of_first = len(first)
    length_of_second = len(second)
    while open_set:
        # get one from open_set which reached farthest
        current = sorted(open_set, key=lambda x: -x[0][-1])[0]
        # current = sorted(open_set, key=lambda x: -max(x[0][-1], x[1][-1]))[0]
        open_set.remove(current)
        # closed_set.add(current)
        # print(longest_matches, len(open_set), len(closed_set), len(current[0]) + (len(first) - 1 - current[0][-1]))
        if longest_matches > len(current[0]) + (length_of_first - 1 - current[0][-1]) \
                or longest_matches > len(current[1]) + (length_of_second - 1 - current[1][-1]):
            continue

        for target in POSSIBLE_ELEMENTS:
            index_of_first = findfirst(first, current[0][-1] + 1, target)
            index_of_second = findfirst(second, current[1][-1] + 1, target)
            if (not index_of_first) or (not index_of_second):
                if len(current[0]) >= longest_matches:
                    results.add(current)
                    longest_matches = len(current[0])
            else:
                i_first = index_of_first[0]
                i_second = index_of_second[0]
                combination = (tuple(list(current[0]) + [i_first]),
                               tuple(list(current[1]) + [i_second]))
                if longest_matches > (len(current[0]) + 1) + (length_of_first - 1 - i_first) \
                        or longest_matches > (len(current[1]) + 1) + (length_of_second - 1 - i_second):
                    pass
                elif combination not in closed_set:
                    open_set.add(combination)
    results = [i for i in results if len(i[0]) == longest_matches]

    # translate indexes into chars
    sequences = []
    for i in results:
        sequences.append(''.join([first[j] for j in i[0]]))
    # print(','.join(sorted(list(set(sequences)))))
    return ','.join(sorted(list(set(sequences))))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert common("ACGTC", "TTACTC") == "ACTC", "One"
    assert common("CGCTA", "TACCG") == "CC,CG,TA", "Two"
    assert common("GCTT", "AAAAA") == "", "None"
    assert common('TTGGTGTCGCTAGACC', 'CGCTAGTGGGGAAT') == 'TTGGGGAA'
    assert common('GGAGTACCATGGGCGGGACGTCACAGCCCCCAACTCA',
                  'AAGGTGACGCAAATGGTATATTCGCTAAGGATT') == 'AGTACCATGGACGCAAGAT,AGTACCATGGACGTAAGAT,AGTACCATGGATACGCAAA,AGTACCATGGATACGCAAT,AGTACCATGGCGCTAAGAT,GGGACCATGGACGCAAGAT,GGGACCATGGACGTAAGAT,GGGACCATGGATACGCAAA,GGGACCATGGATACGCAAT,GGGACCATGGCGCTAAGAT,GGTACCATGGACGCAAGAT,GGTACCATGGACGTAAGAT,GGTACCATGGATACGCAAA,GGTACCATGGATACGCAAT,GGTACCATGGCGCTAAGAT'
    # assert common('AACGTTTTGGGTTTAGAGAAAGTGCTCACAGTAGGTACGTCCCCCAGACCCCACGCCAATGTAT',
    #               'TTTGGGAATGCAATTTAGCTCACAGAGCATACAATGAGAACCACCGAGATCATATTAAGTCTCC') == 'TTTGGGAAGAAAGCTCACAGAGTACGAGACCCCAGCAATGTT,TTTGGGAAGAAAGCTCACAGAGTACGAGACCCCAGCAATTAT,TTTGGGAAGAAAGCTCACAGAGTACTAGACCCCAGCAATGTT,TTTGGGAAGAAAGCTCACAGAGTACTAGACCCCAGCAATTAT,TTTGGGAAGAATGCTCACAGAGTACGAGACCCCAGCAATGTT,TTTGGGAAGAATGCTCACAGAGTACGAGACCCCAGCAATTAT,TTTGGGAAGAATGCTCACAGAGTACTAGACCCCAGCAATGTT,TTTGGGAAGAATGCTCACAGAGTACTAGACCCCAGCAATTAT'
    # assert common('CATTCATTTACAACACTAGGGTAACACCAGCGCGATAGGCTGAGAAAACAC', 'CTCACCATTGAAGACAACCCGCTTGCGAACCGAAATGGTGACGGAACAACCCTCCCAGTT') == 'CACATTAAACAACCCGCGCGAAGGTGAGAAAACA,CACATTAAACAACCCGCGCGAAGGTGAGAAAACC,CACATTAAACAACCCGCGCGATGGTGAGAAAACA,CACATTAAACAACCCGCGCGATGGTGAGAAAACC,CACATTAAACAAGGCAACCGAAGGTGAGAAAACA,CACATTAAACAAGGCAACCGAAGGTGAGAAAACC,CACATTAAACAAGGCAACCGATGGTGAGAAAACA,CACATTAAACAAGGCAACCGATGGTGAGAAAACC,CACATTAAACAAGGGAACAAATGGTGAGAAAACA,CACATTAAACAAGGGAACAAATGGTGAGAAAACC,CACATTAAACAAGGGAACCAAAGGTGAGAAAACA,CACATTAAACAAGGGAACCAAAGGTGAGAAAACC,CACATTAAACAAGGGAACCAATGGTGAGAAAACA,CACATTAAACAAGGGAACCAATGGTGAGAAAACC,CACATTAAACAAGGGAACCGAAGGTGAGAAAACA,CACATTAAACAAGGGAACCGAAGGTGAGAAAACC,CACATTAAACAAGGGAACCGATGGTGAGAAAACA,CACATTAAACAAGGGAACCGATGGTGAGAAAACC,CACATTAAACAAGTCAACCGAAGGTGAGAAAACA,CACATTAAACAAGTCAACCGAAGGTGAGAAAACC,CACATTAAACAAGTCAACCGATGGTGAGAAAACA,CACATTAAACAAGTCAACCGATGGTGAGAAAACC,CACATTAAACACCCCGCGCGAAGGTGAGAAAACA,CACATTAAACACCCCGCGCGAAGGTGAGAAAACC,CACATTAAACACCCCGCGCGATGGTGAGAAAACA,CACATTAAACACCCCGCGCGATGGTGAGAAAACC,CACATTAAACACGGCAACCGAAGGTGAGAAAACA,CACATTAAACACGGCAACCGAAGGTGAGAAAACC,CACATTAAACACGGCAACCGATGGTGAGAAAACA,CACATTAAACACGGCAACCGATGGTGAGAAAACC,CACATTAAACACGGGAACAAATGGTGAGAAAACA,CACATTAAACACGGGAACAAATGGTGAGAAAACC,CACATTAAACACGGGAACCAAAGGTGAGAAAACA,CACATTAAACACGGGAACCAAAGGTGAGAAAACC,CACATTAAACACGGGAACCAATGGTGAGAAAACA,CACATTAAACACGGGAACCAATGGTGAGAAAACC,CACATTAAACACGGGAACCGAAGGTGAGAAAACA,CACATTAAACACGGGAACCGAAGGTGAGAAAACC,CACATTAAACACGGGAACCGATGGTGAGAAAACA,CACATTAAACACGGGAACCGATGGTGAGAAAACC,CACATTAAACACGTCAACCGAAGGTGAGAAAACA,CACATTAAACACGTCAACCGAAGGTGAGAAAACC,CACATTAAACACGTCAACCGATGGTGAGAAAACA,CACATTAAACACGTCAACCGATGGTGAGAAAACC,CACATTAAACACTGCAACCGAAGGTGAGAAAACA,CACATTAAACACTGCAACCGAAGGTGAGAAAACC,CACATTAAACACTGCAACCGATGGTGAGAAAACA,CACATTAAACACTGCAACCGATGGTGAGAAAACC,CACATTAAACACTGGAACAAATGGTGAGAAAACA,CACATTAAACACTGGAACAAATGGTGAGAAAACC,CACATTAAACACTGGAACCAAAGGTGAGAAAACA,CACATTAAACACTGGAACCAAAGGTGAGAAAACC,CACATTAAACACTGGAACCAATGGTGAGAAAACA,CACATTAAACACTGGAACCAATGGTGAGAAAACC,CACATTAAACACTGGAACCGAAGGTGAGAAAACA,CACATTAAACACTGGAACCGAAGGTGAGAAAACC,CACATTAAACACTGGAACCGATGGTGAGAAAACA,CACATTAAACACTGGAACCGATGGTGAGAAAACC,CACATTAAACACTTCAACCGAAGGTGAGAAAACA,CACATTAAACACTTCAACCGAAGGTGAGAAAACC,CACATTAAACACTTCAACCGATGGTGAGAAAACA,CACATTAAACACTTCAACCGATGGTGAGAAAACC,CACATTACAACCGGCAACCGAAGGTGAGAAAACA,CACATTACAACCGGCAACCGAAGGTGAGAAAACC,CACATTACAACCGGCAACCGATGGTGAGAAAACA,CACATTACAACCGGCAACCGATGGTGAGAAAACC,CACATTACAACCGGGAACAAATGGTGAGAAAACA,CACATTACAACCGGGAACAAATGGTGAGAAAACC,CACATTACAACCGGGAACCAAAGGTGAGAAAACA,CACATTACAACCGGGAACCAAAGGTGAGAAAACC,CACATTACAACCGGGAACCAATGGTGAGAAAACA,CACATTACAACCGGGAACCAATGGTGAGAAAACC,CACATTACAACCGGGAACCGAAGGTGAGAAAACA,CACATTACAACCGGGAACCGAAGGTGAGAAAACC,CACATTACAACCGGGAACCGATGGTGAGAAAACA,CACATTACAACCGGGAACCGATGGTGAGAAAACC,CACATTACAACCGTCAACCGAAGGTGAGAAAACA,CACATTACAACCGTCAACCGAAGGTGAGAAAACC,CACATTACAACCGTCAACCGATGGTGAGAAAACA,CACATTACAACCGTCAACCGATGGTGAGAAAACC,CACATTACAACCTGCAACCGAAGGTGAGAAAACA,CACATTACAACCTGCAACCGAAGGTGAGAAAACC,CACATTACAACCTGCAACCGATGGTGAGAAAACA,CACATTACAACCTGCAACCGATGGTGAGAAAACC,CACATTACAACCTGGAACAAATGGTGAGAAAACA,CACATTACAACCTGGAACAAATGGTGAGAAAACC,CACATTACAACCTGGAACCAAAGGTGAGAAAACA,CACATTACAACCTGGAACCAAAGGTGAGAAAACC,CACATTACAACCTGGAACCAATGGTGAGAAAACA,CACATTACAACCTGGAACCAATGGTGAGAAAACC,CACATTACAACCTGGAACCGAAGGTGAGAAAACA,CACATTACAACCTGGAACCGAAGGTGAGAAAACC,CACATTACAACCTGGAACCGATGGTGAGAAAACA,CACATTACAACCTGGAACCGATGGTGAGAAAACC,CACATTACAACCTTCAACCGAAGGTGAGAAAACA,CACATTACAACCTTCAACCGAAGGTGAGAAAACC,CACATTACAACCTTCAACCGATGGTGAGAAAACA,CACATTACAACCTTCAACCGATGGTGAGAAAACC,CTCACCATAAACACCGCGCGAAGGTGAGAAAACA,CTCACCATAAACACCGCGCGAAGGTGAGAAAACC,CTCACCATAAACACCGCGCGATGGTGAGAAAACA,CTCACCATAAACACCGCGCGATGGTGAGAAAACC,CTCACCATAGAAACCGCGCGAAGGTGAGAAAACA,CTCACCATAGAAACCGCGCGAAGGTGAGAAAACC,CTCACCATAGAAACCGCGCGATGGTGAGAAAACA,CTCACCATAGAAACCGCGCGATGGTGAGAAAACC,CTCACCATAGAACCCGCGCGAAGGTGAGAAAACA,CTCACCATAGAACCCGCGCGAAGGTGAGAAAACC,CTCACCATAGAACCCGCGCGATGGTGAGAAAACA,CTCACCATAGAACCCGCGCGATGGTGAGAAAACC,CTCACCATAGACACCGCGCGAAGGTGAGAAAACA,CTCACCATAGACACCGCGCGAAGGTGAGAAAACC,CTCACCATAGACACCGCGCGATGGTGAGAAAACA,CTCACCATAGACACCGCGCGATGGTGAGAAAACC,CTCACCATGAACACCGCGCGAAGGTGAGAAAACA,CTCACCATGAACACCGCGCGAAGGTGAGAAAACC,CTCACCATGAACACCGCGCGATGGTGAGAAAACA,CTCACCATGAACACCGCGCGATGGTGAGAAAACC,CTCACCATGGAAACCGCGCGAAGGTGAGAAAACA,CTCACCATGGAAACCGCGCGAAGGTGAGAAAACC,CTCACCATGGAAACCGCGCGATGGTGAGAAAACA,CTCACCATGGAAACCGCGCGATGGTGAGAAAACC,CTCACCATGGAACCCGCGCGAAGGTGAGAAAACA,CTCACCATGGAACCCGCGCGAAGGTGAGAAAACC,CTCACCATGGAACCCGCGCGATGGTGAGAAAACA,CTCACCATGGAACCCGCGCGATGGTGAGAAAACC,CTCACCATGGACACCGCGCGAAGGTGAGAAAACA,CTCACCATGGACACCGCGCGAAGGTGAGAAAACC,CTCACCATGGACACCGCGCGATGGTGAGAAAACA,CTCACCATGGACACCGCGCGATGGTGAGAAAACC,CTCACCATTAACACCGCGCGAAGGTGAGAAAACA,CTCACCATTAACACCGCGCGAAGGTGAGAAAACC,CTCACCATTAACACCGCGCGATGGTGAGAAAACA,CTCACCATTAACACCGCGCGATGGTGAGAAAACC,CTCATTAAACAACCCGCGCGAAGGTGAGAAAACA,CTCATTAAACAACCCGCGCGAAGGTGAGAAAACC,CTCATTAAACAACCCGCGCGATGGTGAGAAAACA,CTCATTAAACAACCCGCGCGATGGTGAGAAAACC,CTCATTAAACAAGGCAACCGAAGGTGAGAAAACA,CTCATTAAACAAGGCAACCGAAGGTGAGAAAACC,CTCATTAAACAAGGCAACCGATGGTGAGAAAACA,CTCATTAAACAAGGCAACCGATGGTGAGAAAACC,CTCATTAAACAAGGGAACAAATGGTGAGAAAACA,CTCATTAAACAAGGGAACAAATGGTGAGAAAACC,CTCATTAAACAAGGGAACCAAAGGTGAGAAAACA,CTCATTAAACAAGGGAACCAAAGGTGAGAAAACC,CTCATTAAACAAGGGAACCAATGGTGAGAAAACA,CTCATTAAACAAGGGAACCAATGGTGAGAAAACC,CTCATTAAACAAGGGAACCGAAGGTGAGAAAACA,CTCATTAAACAAGGGAACCGAAGGTGAGAAAACC,CTCATTAAACAAGGGAACCGATGGTGAGAAAACA,CTCATTAAACAAGGGAACCGATGGTGAGAAAACC,CTCATTAAACAAGTCAACCGAAGGTGAGAAAACA,CTCATTAAACAAGTCAACCGAAGGTGAGAAAACC,CTCATTAAACAAGTCAACCGATGGTGAGAAAACA,CTCATTAAACAAGTCAACCGATGGTGAGAAAACC,CTCATTAAACACCCCGCGCGAAGGTGAGAAAACA,CTCATTAAACACCCCGCGCGAAGGTGAGAAAACC,CTCATTAAACACCCCGCGCGATGGTGAGAAAACA,CTCATTAAACACCCCGCGCGATGGTGAGAAAACC,CTCATTAAACACGGCAACCGAAGGTGAGAAAACA,CTCATTAAACACGGCAACCGAAGGTGAGAAAACC,CTCATTAAACACGGCAACCGATGGTGAGAAAACA,CTCATTAAACACGGCAACCGATGGTGAGAAAACC,CTCATTAAACACGGGAACAAATGGTGAGAAAACA,CTCATTAAACACGGGAACAAATGGTGAGAAAACC,CTCATTAAACACGGGAACCAAAGGTGAGAAAACA,CTCATTAAACACGGGAACCAAAGGTGAGAAAACC,CTCATTAAACACGGGAACCAATGGTGAGAAAACA,CTCATTAAACACGGGAACCAATGGTGAGAAAACC,CTCATTAAACACGGGAACCGAAGGTGAGAAAACA,CTCATTAAACACGGGAACCGAAGGTGAGAAAACC,CTCATTAAACACGGGAACCGATGGTGAGAAAACA,CTCATTAAACACGGGAACCGATGGTGAGAAAACC,CTCATTAAACACGTCAACCGAAGGTGAGAAAACA,CTCATTAAACACGTCAACCGAAGGTGAGAAAACC,CTCATTAAACACGTCAACCGATGGTGAGAAAACA,CTCATTAAACACGTCAACCGATGGTGAGAAAACC,CTCATTAAACACTGCAACCGAAGGTGAGAAAACA,CTCATTAAACACTGCAACCGAAGGTGAGAAAACC,CTCATTAAACACTGCAACCGATGGTGAGAAAACA,CTCATTAAACACTGCAACCGATGGTGAGAAAACC,CTCATTAAACACTGGAACAAATGGTGAGAAAACA,CTCATTAAACACTGGAACAAATGGTGAGAAAACC,CTCATTAAACACTGGAACCAAAGGTGAGAAAACA,CTCATTAAACACTGGAACCAAAGGTGAGAAAACC,CTCATTAAACACTGGAACCAATGGTGAGAAAACA,CTCATTAAACACTGGAACCAATGGTGAGAAAACC,CTCATTAAACACTGGAACCGAAGGTGAGAAAACA,CTCATTAAACACTGGAACCGAAGGTGAGAAAACC,CTCATTAAACACTGGAACCGATGGTGAGAAAACA,CTCATTAAACACTGGAACCGATGGTGAGAAAACC,CTCATTAAACACTTCAACCGAAGGTGAGAAAACA,CTCATTAAACACTTCAACCGAAGGTGAGAAAACC,CTCATTAAACACTTCAACCGATGGTGAGAAAACA,CTCATTAAACACTTCAACCGATGGTGAGAAAACC,CTCATTACAACCGGCAACCGAAGGTGAGAAAACA,CTCATTACAACCGGCAACCGAAGGTGAGAAAACC,CTCATTACAACCGGCAACCGATGGTGAGAAAACA,CTCATTACAACCGGCAACCGATGGTGAGAAAACC,CTCATTACAACCGGGAACAAATGGTGAGAAAACA,CTCATTACAACCGGGAACAAATGGTGAGAAAACC,CTCATTACAACCGGGAACCAAAGGTGAGAAAACA,CTCATTACAACCGGGAACCAAAGGTGAGAAAACC,CTCATTACAACCGGGAACCAATGGTGAGAAAACA,CTCATTACAACCGGGAACCAATGGTGAGAAAACC,CTCATTACAACCGGGAACCGAAGGTGAGAAAACA,CTCATTACAACCGGGAACCGAAGGTGAGAAAACC,CTCATTACAACCGGGAACCGATGGTGAGAAAACA,CTCATTACAACCGGGAACCGATGGTGAGAAAACC,CTCATTACAACCGTCAACCGAAGGTGAGAAAACA,CTCATTACAACCGTCAACCGAAGGTGAGAAAACC,CTCATTACAACCGTCAACCGATGGTGAGAAAACA,CTCATTACAACCGTCAACCGATGGTGAGAAAACC,CTCATTACAACCTGCAACCGAAGGTGAGAAAACA,CTCATTACAACCTGCAACCGAAGGTGAGAAAACC,CTCATTACAACCTGCAACCGATGGTGAGAAAACA,CTCATTACAACCTGCAACCGATGGTGAGAAAACC,CTCATTACAACCTGGAACAAATGGTGAGAAAACA,CTCATTACAACCTGGAACAAATGGTGAGAAAACC,CTCATTACAACCTGGAACCAAAGGTGAGAAAACA,CTCATTACAACCTGGAACCAAAGGTGAGAAAACC,CTCATTACAACCTGGAACCAATGGTGAGAAAACA,CTCATTACAACCTGGAACCAATGGTGAGAAAACC,CTCATTACAACCTGGAACCGAAGGTGAGAAAACA,CTCATTACAACCTGGAACCGAAGGTGAGAAAACC,CTCATTACAACCTGGAACCGATGGTGAGAAAACA,CTCATTACAACCTGGAACCGATGGTGAGAAAACC,CTCATTACAACCTTCAACCGAAGGTGAGAAAACA,CTCATTACAACCTTCAACCGAAGGTGAGAAAACC,CTCATTACAACCTTCAACCGATGGTGAGAAAACA,CTCATTACAACCTTCAACCGATGGTGAGAAAACC'
