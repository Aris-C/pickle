'''
***********************************************
* program: telephone_book.py                  *
* author: Aris Carter                         *
* date: 1/28/21                               *
* The Hidden Genius Project                   *
* Cohort: OAk8                                *
***********************************************
'''

import pickle

# 1 Leader Numbers
leader = {}
leader['Jacore Baptiste'] = '(845) 200-6250'
leader['Gabriel Reader'] = '(510) 326-5834'
leader['Aris Carter'] = '(510) 229-6359'
leader['Andrew Lubega'] = '(925) 727-4611'
leader['Richard Kamau'] = '(510) 228-5623'

# 2. create/open pod_nbrs.pkl file
pod_file = open('pod_nrbs.pkl', 'wb')

#3. Write POD Leader number to a file
pickle.dump(leader,pod_file)

#4. Member Numbers
member = {}
member['Aris Carter'] = '(510) 229-6359'
member['Zyion Williams'] = '(510) 480-5785'
member['Maurice Richardson'] = '(510) 424-7789'
member['Hyab Isayas'] = '(510) 612-3737'

#5 Write Member numbers to pod_file
pickle.dump(member,pod_file)

#6 Close pod_file
pod_file.close()

#7. Open pod.file
pod_file = open('pod_nrbs.pkl', 'rb')

#8. LEader numbers
print('Leaders: ')
for key,value in leader.items():
    print(key,value)

print('\n')

#9. Print POD members
print('Members: ')
for key,value in member.items():
    print(key,value)


print('\n')


#10 Close pod_file
pod_file.close()








