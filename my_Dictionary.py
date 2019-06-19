
mylist={1,2,3,4}
myDictionary={'key':'value','key2':'value'}


myPhones={'Iphone X':1000,'Sumsang S9':900 }
print(myPhones)

Iphone_price=myPhones['Iphone X']
print('Iphone price:'+str(Iphone_price))

# change key value
Iphone_price=500
myPhones['Iphone X']=500
print(myPhones)

myPhones.clear()
print(myPhones)