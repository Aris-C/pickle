# Initialize Instructor Dictionary
instructor = {}
# Initialize Pod Leader Dictionary
jacore_leader = {}
aris_leader = {}
# Initialize POD Members Dictionary
jacore_member = {}
aris_member = {}
# Add Members to member POD
jacore_member['Jacore Baptiste'] = '(845) 200-6250'
jacore_member['Moussa Ndiaye'] = '(123) 456-7890'
jacore_member['Morris Jones'] = '(925) 286-5922'
jacore_member['Prince Fields'] = '(510) 472-0804'
jacore_member['Akari Johnson'] = '(510) 500-2206'
# Add member POD to POD leader’s Dictionary
jacore_leader['Jacore'] = jacore_member

aris_leader['Aris'] = aris_member
aris_member['Milan'] = '000000000'
aris_member['Maurice'] = '000000000'
aris_member['hyab'] = '0000000000'
aris_member['Zyion'] = '0000008787'



# Add Member POD to Instructor’s Dictionary
instructor['Baba'] = jacore_leader
instructor['Hodari'] = aris_leader
print(instructor)
