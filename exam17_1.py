import re

i = "Beautiful is better than ugly"
matches = re.findall("Beautiful", i)
print(matches)

matches = re.findall("beautiful", i, re.IGNORECASE)
print(matches)

zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
ar one honging
great idea -- let's
do more of those!

if if if"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

line = "123 hi 34 hello."
m = re.findall("\d", line, re.IGNORECASE)
print(m)

t = "____ __two__ __three__"
found = re.findall("__.*?__", t)
for match in found:
    print(match)
    
print(zen)


text = """キリンは大昔から __複数名詞__ の興味の対象でした。キリンは __複数名詞__ の中で一番背が高いですが、科学者たちはそのような長い __体の一部__ をどうやって獲得したのか説明できません。キリンの身長は __数値__ __単位__ 近くあり、その高さのほとんどは脚と __体の一部__ によるものです。
"""

def mad_libs(mls):
    """
:param mils: 文字列でユーザーに検索してもらいたい単語(ヒント)の
部分は後を2つのアンダースコアで挟んでください。ヒントの単語には
 アンダースコアを含めないでください。__hint__hint__ はダメです。__hint__ はOKです。

"""
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "{}を入力:".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("引数mlsが無効でs")
mad_libs(text)
