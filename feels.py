sad=[]
disgust=[]
anger=[]
anticipation=[]
fear=[]
enjoyment=[]
trust=[]
surprise=[]

def feel(sentiment):
    file1 = open('sad.txt','r')
    for line in file1:
        if(',' in line):
            for word in line.split(','):
                sad.append(word.lower().strip())
        else:
                sad.append(line.replace('\n',''))
    file2 = open('disgust.txt','r')
    for line in file2:
        if(',' in line):
            for word in line.split(','):
                disgust.append(word.lower().strip())
        else:
                disgust.append(line.replace('\n',''))
    file3 = open('anger.txt','r')
    for line in file3:
        if(',' in line):
            for word in line.split(','):
                anger.append(word.lower().strip())
        else:
                anger.append(line.replace('\n',''))
    file4 = open('anticipation.txt','r')
    for line in file4:
        if(',' in line):
            for word in line.split(','):
                anticipation.append(word.lower().strip())
        else:
                anticipation.append(line.replace('\n',''))
    file5 = open('fear.txt','r')
    for line in file5:
        if(',' in line):
            for word in line.split(','):
                fear.append(word.lower().strip())
        else:
                fear.append(line.replace('\n',''))
    file6 = open('enjoyment.txt','r')
    for line in file6:
        if(',' in line):
            for word in line.split(','):
                enjoyment.append(word.lower().strip())
        else:
                enjoyment.append(line.replace('\n',''))
    file7 = open('trust.txt','r')
    for line in file7:
        if(',' in line):
            for word in line.split(','):
                trust.append(word.lower().strip())
        else:
                trust.append(line.replace('\n',''))
    file8 = open('surprise.txt','r')
    for line in file8:
        if(',' in line):
            for word in line.split(','):
                surprise.append(word.lower().strip())
        else:
                surprise.append(line.replace('\n',''))
                
    if sentiment in sad:
        return "sad"
    elif sentiment in disgust:
        return "disgust"
    elif sentiment in anger:
        return "anger"
    elif sentiment in anticipation:
        return "anticipation"
    elif sentiment in fear:
        return "fear"
    elif sentiment in enjoyment:
        return "enjoyment"
    elif sentiment in trust:
        return "trust"
    elif sentiment in surprise:
        return "surprise"

