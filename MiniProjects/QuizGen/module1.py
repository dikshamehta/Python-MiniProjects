import random
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

f= open('capitals.txt','w')
#this one is done to create a file where all the states along with capitals are written
#issue faced was that i was trying to directly write in this format nd maine bahar wale quotes bhi
#single lgaye hue the and ander text mai bhi single quotes the
#lesson: use double quotes in write("  ") if ur text have single quotes and vice versa
f.write("capitals =  {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}")
f.close()

#this loop is to create 35 different sets of ques papers
for n in range(1,36):
    f=open('capitalquiz'+str(n)+'.txt','w')
    f.write("Name:                                  \n\n")
    f.write("Date:                                  \n\n")
    f.write("Period:                                     \n\n")
    f.write('State Capitals Quiz (Form '+str(n)+')\n\n')

    a= open('capitalquiz_answers'+str(n),'w')
    ques=[]
    q=1
    #this loop is to generate 51 random ques in each ques paper
    while len(ques)!=50:
        #random ques generation
        temp=random.choice(list(capitals))
        if(ques.count(temp)==0):
            print(str(q)+"."+str(temp))
            ques.append(temp)
            f.write(str(q)+'.  What is the capital of '+str(temp)+' ?\n')
            a.write(str(q)+'. '+str(capitals[temp])+'\n')
            q=q+1

            #creating list to store 3 random option+ 1 correct option
            options=[]
            options=[capitals[temp]]#correct option stored

            #completing the list with other 3 random options.
            while len(options)!=4:#this condition is applied as hume list mai 4 options dalne hi hai
                key= random.choice(list(capitals))
                if(options.count(key)==0 and temp!=key ):#this condition to put check ki option repeat na ho jae
                    options = options + [capitals[key]]
                else:
                    continue

            #this list is created to show A.option1
            #                             B.option2 and so on
            abc=['l','A','B','C','D']
            for n in range(1,5):
                val= random.choice(options)#this is applied to shuffle the options list, agar ye nai krte to correct
                f.write('\t'+abc[n]+'.  '+str(val)+'\n')
                options.remove(val)#ye krna pda kyuki fir vo random choose krte wakt repeat ho jati hai values.
