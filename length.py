#!/usr/bin/env python2.7

# process the 1st part of the input file, and get the calculation rules
def get_rules():
    for line in inFileHandle:
        if line.strip():
            lineList = line.split()
            lenDict[lineList[1]] = float(lineList[3])
        else:    # the blank line encountered
            break
    lenDict['miles'] = lenDict['mile']
    lenDict['yards'] = lenDict['yard']
    lenDict['inches'] = lenDict['inch']
    lenDict['feet'] = lenDict['foot']
    lenDict['faths'] = lenDict['fath']
    lenDict['furlongs'] = lenDict['furlong']
    lenDict['meters'] = lenDict['meter'] = 1


# process the 2nd part of the input file, display and save the result
def cal_save():
    outFileHandle.write(email + '\n\n')
    for line in inFileHandle:
        lineList = line.split()
        expression = ''
        for item in lineList:
            if (item not in lenDict) and (item not in '+-'):    # number
                temp = float(item)
            elif item in lenDict:    # length unit (miles, feet, etc)
                temp *= lenDict[item]
                expression += str(temp)
            else:    # +/-
                expression += item
        print '%.2f m' % eval(expression)
        print >>outFileHandle, '%.2f m' % eval(expression) 


if __name__ == '__main__':
    lenDict = {}    # calculation-rule dict
    inFileName = 'input.txt'
    inFileHandle = open(inFileName, 'r')
    print 'Reading calculation rules'
    get_rules()  

    email = 'rcompass@139.com'
    outFileName = 'output.txt'
    outFileHandle = open(outFileName, 'w')
    print '\nCalculation results are as follows:'
    cal_save()

    inFileHandle.close()
    outFileHandle.close()
    print '\nSaving results in %s.\nDone!' % outFileName
