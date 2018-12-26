from textblob import TextBlob

# For reading input files in CSV format
import csv


# For sorting dictionaries
import operator

n1=0
n2=0
# Intialize an empty list to hold all of our tweets
reviews= []
print"Choose options: \n 1:Check if your hospital is Recommended!!\n 2.Check Hospitals for a particular speciality!!\n 3.Exit"
print"Enter:"
choice=input();
if choice==1:
    print "Enter Hospital Name:" 
    val=raw_input()
elif choice==2:
    print "Enter Speciality:"  
    val=raw_input()  
else:
    print "Exitinggg..."
count=0
# A helper function that removes all the non ASCII characters
# from the given string. Retuns a string with only ASCII characters.
def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)




#
# We create a data structure for each review:


with open('syn.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    reader.next()
    for row in reader:

        review= dict()
        review['id'] = int(row[0])
        review['hospital'] = row[1]
        review['speciality']= row[2]
        review['review']= row[3]
     
        review['clean'] = review['review']

        # Remove all non-ascii characters
        review['clean'] = strip_non_ascii(review['clean'])
    

        # Create textblob object
        review['TextBlob'] = TextBlob(review['clean'])

    
        reviews.append(review)


# DEVELOP MODELS

for review in reviews:
    review['polarity'] = float(review['TextBlob'].sentiment.polarity)
    review['subjectivity'] = float(review['TextBlob'].sentiment.subjectivity)

    if review['polarity'] >= 0.1:
        review['sentiment'] = 'positive'
    elif review['polarity'] <= -0.1:
        review['sentiment'] = 'negative'
    else:
        review['sentiment'] = 'neutral'
reviews_sorted = sorted(reviews, key=lambda k: k['polarity'])

for review in reviews:
    if review['hospital']== val:
        print"polarity=%.2f %s" % (review['polarity'], review['review'])

# EVALUATE RESULTS
#print "\n\nTOP NEGATIVE REVIEWS"
#negative_review = [d for d in reviews_sorted if d['sentiment'] == 'negative']
#for review in negative_review[0:5] :

 #    print "id=%d,polarity=%.2f %s" % (review['id'], review['polarity'], review['hospitalname'])


if choice==2:
     positive_review = [d for d in  reviews_sorted if d['sentiment'] == 'positive']
     for review in positive_review[0:71]:
            if review['speciality']== val:
                   if review['polarity']<=1.0 and review['polarity']>=0.8:
                         print "%s *5 STAR*" % (review['hospital'])
                   if review['polarity']<0.8 and review['polarity']>=0.6:
                         print "%s *4 STAR*" % (review['hospital'])
                   if review['polarity']<0.6 and review['polarity']>=0.4:
                         print "%s *3 STAR*" % (review['hospital'])
                   if review['polarity']<0.4 and review['polarity']>=0.1:
                         print "%s *2 STAR*" % (review['hospital'])                  
    
if choice==1:
     for review in reviews:
	      if review['hospital']== val:
               if review['polarity']>=0.1:
         	     n1=n1+1
               else:
         	     n2=n2+1
     if n1>n2 :
          print "No. Of positive Reviews: %d \n No. Of negative Reviews: %d \n Recommended" % (n1,n2) 
     else:
          print "No. Of positive Reviews: %d \n No. Of negative Reviews: %d \n Not Recommended" % (n1,n2)              	  
              





