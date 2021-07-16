# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("乘法口诀表")
for i in range(0,10):
    for j in range(0,10):
        print('{}X{}={}'.format(i,j,i*j))

print("遮挡号码后几位")
phone_number = '1386-666-0006'
hid_number = phone_number.replace(phone_number[:9],'*'*9)
print(hid_number)

search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print("*"*30)
print('{} a word {}'.format('with','came'))
print('{pre} a word {verb}'.format(pre="with",verb="came"))
print('{0} a word {1}'.format("with","came"))
print("*"*30)
def text_f(word,censored_word='lame',changed_word='awesome'):
    return word.replace(censored_word,changed_word)
print(text_f('Python is lame'))



city = input("城市\n")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
print(url)




