import sys, re
#Stephen Lazaro 2/20/2016
#tbh this probably would have been easier in ruby but w/e

def main():
	#Usual set up, read in text and split on regex match
    script = open(sys.argv[1])
    #Matches capitalizes strictly given more than once
    regexp = re.compile("([A-Z]{2,})") 
    all_text = script.read()
    script.close()
    out_file = open("out.txt", "w")
    splitted = re.split(regexp, all_text) 
    #Unfortunately, splits before and after.
    #Need recombine into AGENT,line form if possible.
    print(splitted)
    #Here we recombine things with a quick loop
    recomb = []
    for index, text in enumerate(splitted):
	    #Correct for index out of bounds obviously
	    if index == len(splitted) - 1:
		    pass
	    elif text.upper() == text:
		    recomb.append(text + splitted[index + 1])
    #Write everything out to file on individual lines
    for text in recomb:
        out_file.write(str(text) + "\n")
    out_file.close()


if __name__ == '__main__':
    main()