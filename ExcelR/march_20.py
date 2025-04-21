
#Dict

A = {
    "Rupesh" : "Desai",
    "om" : "D",
    "S" : "M",
    "Rupesh" : "DD"
}
# print(type(A)) #Dict
# print(A)
# print(A['Rupesh']) #desai

B = {
    "Roll Num" : 12,
    "Name" : "ABC",
    "Sub" : 'English'
}

# B.update({"Name": "Rupes"}) #अपडेट करेल abc to  RUpes. Dict  मधील Value  बडल्यानसाठी हिसतरीकक ओन्ली 
# print(B.keys()) # gives ओन्ली keys name 
print(B.get("Roll Num")) #it give the specific data`s key value.



