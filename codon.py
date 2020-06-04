ERRORS = {
    "WRONG_LEN": "[ERROR]: The codon sequence contains incomplete codon's.",
    "WRONG_CHARS": "[ERROR]: The codon sequence contains unknown codon's."
    "Maybe you used Urasil ('U') instead of Thymine ('T'). Urasil is used for RNA, not DNA.",
    "UNKNOWN_CODON": "[ERROR]: The supplied codon sequence contains unknown codon's."
}

AMINO_ACIDS = {
    'I': ['ATT', 'ATC', 'ATA'],
    'L': ['CCA', 'CCG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'V': ['GTT', 'GTC', 'GTA', 'GTG'],
    'F': ['TTT', 'TTC'],
    'M': ['ATG'],
    'X': ['TTT', 'TTC', 'TCT', 'TCC', 'TCA', 'TCG', 'CCT', 'CCC', 'CCA', 'CCG',
          'ACT', 'ACC', 'ACA', 'ACG', 'GCT', 'GCC', 'GCA', 'GCG',
          'TAT', 'TAC', 'TAA', 'TAG', 'CAT', 'CAC', 'CAA', 'CAG',
          'AAT', 'AAC', 'AAA', 'AAG', 'GAT', 'GAC', 'GAA', 'GAG',
          'TGT', 'TGC', 'TGA', 'TGG', 'CGT', 'CGC', 'CGA', 'CGG',
          'AGT', 'AGC', 'AGA', 'AGG', 'GGT', 'GGC', 'GGA', 'GGG']
}


def get_codon_slc(codon):
    for slc in AMINO_ACIDS:
        if codon.upper() in AMINO_ACIDS[slc]:
            return slc
    else:
        return ''


def check_codon_validity(codon):
    error = ''

    if (len(codon) % 3) != 0:
        error = ERRORS['WRONG_LEN']
    else:
        for i in codon[:]:
            if i.upper() not in ['A', 'T', 'G', 'C']:
                error = ERRORS['WRONG_CHARS']
                break

    return error


def translate(sequence):
    slc = ''
    error = check_codon_validity(sequence)

    if not error:
        for i in range(len(sequence) // 3):
            codon = sequence[(i*3):(i*3)+3]
            slc += get_codon_slc(codon)

    return (False, slc) if slc != '' else (True, error)


def mutate():
    dnaIn = open('DNA.txt', 'r')
    dna = dnaIn.read()
    dnaIn.close()

    dna = dna.replace("\n", "")
    dna = dna.replace("\r", "")

    # Only here because its mentioned in the instructions
    a_index = dna.find('a')

    normal = dna.replace('a', 'A')
    mutated = dna.replace('a', 'T')

    write_to_file('normalDNA.txt', normal)
    write_to_file('mutatedDNA.txt', mutated)


def write_to_file(filename, text):
    f = open(filename, 'w')
    f.write(text)
    f.close()


def read_file(filename):
    with open(filename, 'r') as f:
        txt = f.read()
    return txt


def txtTranslate():
    mutated = translate(read_file('mutatedDNA.txt'))
    normal = translate(read_file('normalDNA.txt'))

    print(mutated[1])
    print(normal[1])


mutate()
txtTranslate()
