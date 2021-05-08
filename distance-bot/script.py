
import praw

ways_to_express_miles = ['m', 'miles','mi', 'mile']
ways_to_express_km = ['km', 'kilometers', 'kilometer']
ways_to_express_min_per_mi = ['min/mi', 'minutes/mile', 'minutes/miles', 'minute/miles', 'minutes/mi', 'min/mile', 'min/miles']
ways_to_express_min_per_km = ['min/km', 'minutes/kilometer', 'minutes/kilometers', 'minute/kilometers', 'minutes/km', 'min/kilometer', 'min/kilometers']

def main():

    reddit = praw.Reddit(
        # ENTER CREDENTIALS HERE
        user_agent='Distance Converter Bot',
        client_id='', 
        client_secret='',
        username='', 
        password=''
    )
    subreddit = reddit.subreddit('running')
    while(True):
        for submission in subreddit.new():
            output = ''
            submissions = submission.title.split()
            submissions.append(submission.selftext.split())
            for word in (range(len(submissions)-1)):
                #print(submissions[word+1])
                if (type(submissions[word]).__name__ == 'int' or 'float'):
                    if str(submissions[word+1]).lower() in ways_to_express_miles:
                        output += submissions[word]+' '+submissions[word+1]+' = '+ str(int(submissions[word])*1.60934)+' '+'km\n'
                        #submission.reply(submissions[word]+' '+submissions[word+1]+' mi = '+ str(int(submissions[word])*1.60934)+' '+'km')
                    if str(submissions[word+1]).lower() in ways_to_express_km:
                        output += submissions[word]+' '+submissions[word+1]+' = '+ str(int(submissions[word])/1.60934)+' '+'mi\n'
                        #submission.reply(submissions[word]+' '+submissions[word+1]+' km = '+ str(int(submissions[word])/1.60934)+' '+'mi')
                    if str(submissions[word+1]).lower() in ways_to_express_min_per_mi:
                        output += submissions[word]+' '+submissions[word+1]+' = '+ str(int(submissions[word])/1.60934)+' '+'min/km\n'
                        #submission.reply(submissions[word]+' '+submissions[word+1]+' min/mi = '+ str(int(submissions[word])/1.60934)+' '+'min/km')
                    if str(submissions[word+1]).lower() in ways_to_express_min_per_km:
                        output += submissions[word]+' '+submissions[word+1]+' = '+ str(int(submissions[word])*1.60934)+' '+'min/mi\n'
                        #submission.reply(submissions[word]+' '+submissions[word+1]+' min/km = '+ str(int(submissions[word])*1.60934)+' '+'min/mi')
                res =[]
                run = True
                if (submissions[word][0].isdigit()):
                    digit = ''
                    descriptor = ''
                    for i in range(len(submissions[word])):
                        if submissions[word][i].isdigit():
                            digit += submissions[word][i]
                        elif submissions[word][i].isalpha(): 
                            descriptor + submissions[word][i]
                        else:
                            run = False
                    if run:
                        if descriptor.lower() in ways_to_express_miles:
                            output += digit+' '+descriptor.lower()+' = '+ str(int(digit)*1.60934)+' '+'km\n'
                        #submission.reply(submissions[word]+' '+submissions[word+1]+' mi = '+ str(int(submissions[word])*1.60934)+' '+'km')
                        if descriptor.lower() in ways_to_express_km:
                            output += digit+' '+descriptor.lower()+' = '+ str(int(digit)/1.60934)+' '+'mi\n'
                            #submission.reply(submissions[word]+' '+submissions[word+1]+' km = '+ str(int(submissions[word])/1.60934)+' '+'mi')
                        if descriptor.lower()in ways_to_express_min_per_mi:
                            output += digit+' '+descriptor.lower()+' = '+ str(int(digit)/1.60934)+' '+'min/km\n'
                            #submission.reply(submissions[word]+' '+submissions[word+1]+' min/mi = '+ str(int(submissions[word])/1.60934)+' '+'min/km')
                        if descriptor.lower() in ways_to_express_min_per_km:
                            output += digit+' '+descriptor.lower()+' = '+ str(int(digit)*1.60934)+' '+'min/mi\n'
                            #submission.reply(submissions[word]+' '+submissions[word+1]+' min/km = '+ str(int(submissions[word])*1.60934)+' '+'min/mi')
                            


            if len(output) > 0:
                submission.reply(output+'\n^(Wow, that\'s far!)')



'''
#convert = True
##########################
    for submission in subreddit.new():
        submission.comments.replace_more(limit=None, threshold=0)
        ls = submission.comments.list()
        #print()
        for comment in ls:
            #print(comment.body)
            if 'u/distance-bot' in comment.body:
                print("here")
                c = comment.parent().body.split()  
                for word in (range(len(c)-1)):
                #print(submissions[word+1])
                    if (type(c[word]).__name__ == 'int' or 'float'):
                        if c[word+1].lower() in ways_to_express_miles:
                            comment.reply(c[word]+' '+c[word+1]+' = '+ str(int(c[word])*1.60934)+' '+'km')
                        elif c[word+1].lower() in ways_to_express_km:
                            comment.reply(c[word]+' '+c[word+1]+' = '+ str(int(c[word])/1.60934)+' '+'mi')
                        elif c[word+1].lower() in ways_to_express_min_per_mi:
                            comment.reply(c[word]+' '+c[word+1]+' = '+ str(int(c[word])/1.60934)+' '+'min/km')
                        elif c[word+1].lower() in ways_to_express_min_per_km:
                            comment.reply(c[word]+' '+c[word+1]+' = '+ str(int(c[word])*1.60934)+' '+'min/mi')


'''
if __name__ == '__main__':
    main()