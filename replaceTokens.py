import sys
import in_place


def to_dict(propertyFile):
    """
    returns dict after converting properties file in the form of 
    prop=value
    """
    token_dict = {}
    #TODO check if file not exists
    with open(propertyFile) as file:
        return { line.split("=")[0].strip():line.split("=")[1].strip()  for line in file }

def replace_tokens(filesWithTokens, propertiesFile ):
    token_dict = to_dict(propertiesFile)
    #TODO open file , for each line  replace tokens
    #TODO there are multiple issues with this implementation fix
    with in_place.InPlace(filesWithTokens) as fp:
        for line in fp:
            flag = 0
            for k,v in token_dict.items():
                if k in line:
                    flag = 1
                    modifiedLine = line.replace(k, v)
                    fp.write(modifiedLine)
            if ( flag == 0 ):
                fp.write(line)

if __name__ == "__main__":
    #TODO add condition to check if required number of cmd arguments are provided 
    #print(to_dict(sys.argv[1]))
    replace_tokens(sys.argv[1], sys.argv[2])