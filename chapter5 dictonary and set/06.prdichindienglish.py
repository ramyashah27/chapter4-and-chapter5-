dictonary={
'hii/hello':'नमस्ते'  ,
'ramya': 'sundar',
"how are you":"आप कैसे हैं ",
"My name is ":"मेरा नाम ... है ",
'Thank you': 'धन्यवाद - (Dhanyabaad)',
'gopesh': 'krishna'


}

print(dictonary.keys())
meaning= input(" enter the english word\n")
print("meaning is",[dictonary[meaning]])
print("meaning is",dictonary.get(meaning))