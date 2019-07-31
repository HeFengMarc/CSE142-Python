# This program will read through the data in an input file about DNA, and it will
# print out the information about the DNA in the output file. The program can generate
# the nucleotide counts, total mass percentage list, codons list, etc. At the last
# line for each DNA, the output file will show whether it is a protein or not.

class Constant:
    min_codons_num = 5
    min_percent_CG = 30
    num_uniq_nucleo = 4
    num_nucleo_per_codon = 3

class Program(Constant):

    # This function will return the list of codons. It has two parameters, the first
    # one is the line of input words, and the second it the output file where we store
    # our output.
    def codon_lst_generator(line, outfile):
        codon_lst = list()
        # Remove the '-' in the line.
        new_line = line.replace('-', '')
        # Print out the list of codons
        for i in range(len(new_line)//Constant.num_nucleo_per_codon):
            codon_lst.append(new_line[Constant.num_nucleo_per_codon*i: \
                             Constant.num_nucleo_per_codon*i + \
                             Constant.num_nucleo_per_codon].upper())
        return codon_lst

    # This function returns the total amount of mass percentage of Cytosine and Guanine.
    # The main purpose for this function is to determine the mass and mass percentage.
    def nuc_counts(line, outfile):
        # This inner function will return the total mass of one nucleotide.
        def mass(num, mass):
            return num * mass
        # This inner function will return the mass percentage of one nucleotide.
        def mass_percent(mass, total_mass):
            return round(mass * 1000 / total_mass) / 10

        nucleo_list = list()
        [num_A, num_C, num_G, num_T, num_junk] = [0, 0, 0, 0, -1]
        mass_A = mass_C = mass_G = mass_T = mass_junk = 0

        # Convert the string to a list such that we can count each
        # character one by one.
        for char in range(len(line)):
            nucleo_list.append(line[char].upper())

        # Count the number of each nucleotide and determine the mass for each of them.
        for char in nucleo_list:
            print(char)
            if char == 'A':
                num_A += 1
                mass_A = 135.128
            elif char == 'C':
                num_C += 1
                mass_C = 111.103
            elif char == 'G':
                num_G += 1
                mass_G = 151.128
            elif char == 'T':
                num_T += 1
                mass_T = 125.107
            else:
                num_junk += 1
                mass_junk = 100.000
        nuc_mass_list = [mass_A, mass_C, mass_G, mass_T, mass_junk]
        nuc_num_list = [num_A, num_C, num_G, num_T, num_junk]

        # Calculate the total mass of four nuc. and the junk.
        total_mass =  0
        for nuc in range(Constant.num_uniq_nucleo + 1):
            total_mass += mass(nuc_num_list[nuc], nuc_mass_list[nuc])
        total_mass = round(total_mass * 10) / 10

        # Print the nuc. count in the output file. User can change the number of types
        # of nuc. in each cases. Also make the list of mass percentage of each nuc., and
        # store the list, we will use the list in the following procedure.
        outfile.write('Nuc. Counts: ' + '[' + str(num_A))
        mass_percent_group = '[' + str(mass_percent(mass(num_A, mass_A), total_mass))
        for nuc in range(1, Constant.num_uniq_nucleo):
            outfile.write(', ' + str(nuc_num_list[nuc]))
            mass_percent_group += ', ' + str(mass_percent(mass(nuc_num_list[nuc] \
                                  , nuc_mass_list[nuc]), total_mass))
        outfile.write(']' + '\n')
        mass_percent_group += ']'

        outfile.write('Total Mass%: ' + mass_percent_group + ' of ' + str(total_mass) + '\n')
        return mass_percent(mass(num_C, mass_C), total_mass) + \
                            mass_percent(mass(num_G, mass_G), total_mass)

    # This function has two parameter, the first one is the sum percentage of C and G, and the second
    # one is the list of codons. The function will base on the four restriction to determine whether
    # the item is protein or not. The function will return 'Yes' or 'No' based on the result.
    def protein_or_not(CG_amount, codon_lst):
        stop_codon_list = ['TAA', 'TAG', 'TGA']
        if (codon_lst[0] == 'ATG') and (codon_lst[len(codon_lst) - 1] in stop_codon_list) \
           and (len(codon_lst) >= Constant.min_codons_num) and (CG_amount >= Constant.min_percent_CG):
            return 'YES'
        else:
            return 'NO'

    # The program starts.
    print("This program reports information about DNA")
    print("nucleotide sequences that may encode proteins.")
    input_file = input("Input file name? ")
    output_file = input("Output file name? ")
    infile = open(input_file, 'r')
    outfile = open(output_file, 'w+')

    # the program will read through the input file line by line.
    line_num = 1
    codon_string = ''
    CG_amount = 0
    for line in infile:
        codon_lst = codon_lst_generator(line, outfile)
        # If the line number is an odd number.
        if line_num % 2 is 1:
            outfile.write("Region name: " + line)
        else:
            outfile.write("Nucleotides: " + line.upper())
            # Convert the list of codons into the string format such that
            # it can be stored in the output file.
            codon_string = '['
            i = 0
            for codon in codon_lst:
                i += 1
                codon_string += codon
                if i is len(codon_lst):
                    codon_string += ']'
                else:
                    codon_string += ', '
            CG_amount = nuc_counts(line.upper(), outfile)
            outfile.write("Codons List: " + codon_string + '\n')
            protein = protein_or_not(CG_amount, codon_lst)
            outfile.write("Is Protein?: " + protein + '\n \n')
        line_num += 1
