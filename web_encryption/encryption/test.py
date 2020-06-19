
custom_word = "##RANDOM_WORD_10##"

text = "abccd defg.? $%&"
res = ''
for _ in text:
    res += str(_) + "<span style='color:transparent;font-size: 0%;'>"+ str(custom_word) + "</span>"   
print(res)
