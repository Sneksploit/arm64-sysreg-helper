import sys

descriptions = {}
def read_descriptions(filename):
    global descriptions

    with open(filename, 'r+') as f:
        lines = f.read().split('\n')
        for line in lines:
            first_space = line.find(" ")
            prefix = line[0:first_space]
            prefix_underscore = prefix.find("_")
            if prefix_underscore > 0:
                prefix = prefix[0:prefix_underscore]
            description = line[first_space+1:]
            prefix = ''.join([i for i in prefix if not i.isdigit()])
            descriptions[prefix] = description

def translate_part(filename):
    output = {}
    print("import sys\n\n")
    print("def translate_sysinst(op0, op1, CRm, CRn, op2):\n")
    with open(filename, 'r+') as f:
        lines = f.read().split('\n')
        for line in lines:
            split = line.split(' ')
            if len(split) < 5:
                continue
            name = split[0]
            op0 = split[1]
            op1 = split[2]
            CRm = split[3]
            CRn = split[4]
            op2 = split[5]
            if op0 not in output:
                output[op0] = {}
            if op1 not in output[op0]:
                output[op0][op1] = {}
            if CRm not in output[op0][op1]:
                output[op0][op1][CRm] = {}
            if CRn not in output[op0][op1][CRm]:
                output[op0][op1][CRm][CRn] = {}
            output[op0][op1][CRm][CRn][op2] = name

    for op0 in output.keys():
        print("\tif op0 == " + op0 + ":")

        for op1 in output[op0].keys():
            print("\t\tif op1 == " + op1 + ":")

            for CRm in output[op0][op1].keys():
                print("\t\t\tif CRm == " + CRm + ":")

                for CRn in output[op0][op1][CRm].keys():
                    print("\t\t\t\tif CRn == " + CRn + ":")

                    for op2 in output[op0][op1][CRm][CRn].keys():
                        print("\t\t\t\t\tif op2 == " + op2 + ":")
                        try:
                            prefix = output[op0][op1][CRm][CRn][op2]
                            prefix = ''.join([i for i in prefix if not i.isdigit()])
                            prefix_underscore = prefix.find("_")
                            if prefix_underscore > 0:
                                prefix = prefix[0:prefix_underscore]
                            description = descriptions[prefix]
                            end_space = description.rfind(".")
                            if end_space > 0:
                                description = description[0:end_space]
                        except:
                            description = ""
                        print("\t\t\t\t\t\treturn(\"" + output[op0][op1][CRm][CRn][op2] + "\", \"" + description + "\")")
    print("\n\nif __name__ == \"__main__\":")
    print("\tprint(translate_sysinst(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])))")

if __name__ == "__main__":
    read_descriptions("descriptions.txt")
    translate_part(sys.argv[1])
