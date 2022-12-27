# Rachel Nelson
# Module 6
# 11/12/22
# English to Spanish Dictionary

EngToSpan = {'dog':'perro','cat':'gato','milk':'leche','flower':'flor','water':'agua','beach':'playa','house':'casa','book':'libro','sun':'sol','moon':'luna' }
Keys = []
for key in EngToSpan:
    Keys.append(key)
print(Keys)
UserSelection = input('Please select one key from the displayed list ').strip().lower()
# UserSelection=UserSelection.strip()
# print(UserSelection)
# print(type(UserSelection))
for key in EngToSpan:
    if UserSelection == key:
        UserSelection=str(UserSelection)
        # print(UserSelection)
        print('The word you selected:',UserSelection,'in Spanish is', EngToSpan[UserSelection])












# print('Your English word:',(UserSelection))

# for key,value in EngToSpan:
#     if key == UserSelection:
#         print(key,value)

# # print('is translated to:',(Keys[str(UserSelection)]),('in Spanish.'))


