s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

edit = input(s)
s1 = s.lstrip('@#~')
s2 = s1.rstrip('!>!')
s3 = s2.capitalize()
print(s3)
# ws5_3과 같음.