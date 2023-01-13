first = 'Karan singh rathore'
last = 'Rathore'
"Karan (Rathore) is a learner"
"print (first+last+'is a learner')"
msg = f'{first} [{last}] is a learner'
print(msg)
print(first+' ['+last+'] is a learner')  #fromatted string
print(type(last))                        #calling type of variable
print(first[0:3])                        #slice string by calling []
print(first.title())                     #capitalize the first letter of every word
print(last.replace(last[-1],'q'))        #replace any word or letter from string
print(last.find('a'))                    #returns the index of first occurence of letter
contains = 'singh' in first              #in operator to check if a string contains a character
print(contains)                          #or sequence of character