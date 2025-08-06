import sys
script, input_encoding, error = sys.argv # When you run the script, not only enter the .py, but also make sure the other two arguments (input_encoding and error) are entered.

def main(language_file,encoding,errors):
    line = language_file.readline()
    
    if line:
        print_line(line,encoding,errors)
        return main(language_file,encoding,errors) # callinging main function inside main


def print_line(line,encoding,errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding,errors=errors) #convert a string into bytes
    cooked_string = raw_bytes.decode(encoding,errors=errors)
    
    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")
main(languages,input_encoding,error)
