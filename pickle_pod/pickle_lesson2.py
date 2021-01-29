'''
***********************************************
* program: pickle_lesson2.py                  *
* author: Aris Carter                         *
* date: 1/28/21                               *
* The Hidden Genius Project                   *
* Cohort: OAk8                                *
***********************************************
'''

import pickle

#1 Initialize an empty dictionary variable, name it all_pod_members
all_pod_members = {}

#2 Initialize a file variable to write data to, name it pod_file, that will
# open a file named hgp_pods that you will write data to the file. 
pod_file = open('all_pods.pkl', 'wb')

#3  Initialize empty dictionary variables, name it as such;
jacore_members = {}
andrew_members = {}
aris_members = {}
gabe_members = {}
richard_members = {}



#4 Create an empty dictionary for the other 3 PODs; Aris, Gabriel and Richard

#5 Add the names and telephone numbers of each member POD  
jacore_members['Jacore Baptiste'] = '(845) 200-6250'
jacore_members['Moussa Ndiaye'] = '(123) 456-7890'
jacore_members['Morris Jones'] = '(925) 286-5922'
jacore_members['Prince Fields'] = '(510) 472-0804'
jacore_members['Akari Johnson'] = '(510) 500-2206'

andrew_members['Andrew Lubega'] = '(925) 727-4611'
andrew_members['Mallick Abdullah'] = '(510) 409-8755' 
andrew_members['Ronin Youngjones'] = '(415) 910-3415'
andrew_members['Glenn Ivory'] = '(510) 328-8290'

aris_members['Aris'] = '(510) 229-6359'
aris_members['Hyab'] = '(510) 612-3737'
aris_members['Milan'] = '(510) 816-3232'
aris_members['Maurice'] = '(510) 424-7789'
aris_members['Zyion'] = '(510) 480-5785'

gabe_members['Gabe'] = '(510) 326-5834'
gabe_members['Emmanuel'] = '(510) 934-4133)'
gabe_members['David'] = '(510) 6316288'
gabe_members['Myles'] = '(510) 500-7266'


richard_members['Richard'] = '(510) 2280-5623'
richard_members['Kymari'] = '(510) 575-1982'
richard_members['Josiah'] = '(510) 860-5112'
richard_members['matthew'] = '(510) 846-2411'

#6 Add all the PODS to the all_pod_members dictionary
all_pod_members['Jacore'] = jacore_members
all_pod_members['Andrew'] = andrew_members
all_pod_members['Aris'] = aris_members
all_pod_members['Gabe'] = gabe_members
all_pod_members['Richard'] = richard_members

#7 Dump all the 
pickle.dump(jacore_members,pod_file)
pickle.dump(andrew_members,pod_file)
pickle.dump(aris_members,pod_file)
pickle.dump(gabe_members,pod_file)
pickle.dump(richard_members,pod_file)

#8 Open the pod_file to read data
pod_file = open('all_pods.pkl', 'rb')
print(all_pod_members,'\n')

#9 Print all the Pod leaders and POD membership
for key,value in all_pod_members.items():
  print('This POD Leader is',key)
  for key2, value2 in value.items():
    print(key2,value2)
  print('\n')
pod_file.close()
