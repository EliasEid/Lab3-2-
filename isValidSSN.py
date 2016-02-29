def isValidSSN(tmpSSN):
    ''' Description: Checks to see if tmpSSN is a valid SSN in the format ###-##-####
        Precondition: tmpSSN is a string '''

    if len(tmpSSN) != 11:
        return False
    if tmpSSN[0:3].isdigit() and tmpSSN[3] == "-" and tmpSSN[4:6].isdigit() and tmpSSN[6] == "-" and tmpSSN[7:].isdigit():
        return True
    else:
        return False
