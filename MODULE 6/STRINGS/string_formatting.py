'''name = 'Mike'
number = len(name) * 3
print("Hello {}, your luckey number is {}.".format(name,number))'''

'''example = 'format {} method'
string = "This is an example of {} on a string.".format(example)
print(string)'''


'''first = 'apple'
second = 'ball'
third = 'cat'
four = 'dog'
string = "{} {} {} {}".format(first,second,third,four)
print(string)'''

price = 150
with_tax = 150 + 50
print(price,with_tax)
print("Price: Rs{:.2f}. With tax: Rs{:.2f}".format(price,with_tax))