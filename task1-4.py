# 1. 基本的な変数の宣言
# 以下の指定された条件に合うような値を変数に代入して宣言してください。
# また宣言した変数を出力してください。
# 整数（int） number: 5
# 文字列（string） text: "test"
# 論理型（boolean） flag: True
# None型 test: None
# 浮動小数点数（float） pi: 3.14

#宣言
number: int = 5
text: str = "test"
flag: bool = True
test = None
pi: float = 3.14

#出力
print("number:", number)
print("text:", text)
print("flag:", flag)
print("test:", test)
print("pi:", pi)


# 2.  基本的な計算
# 整数型の2つの変数を宣言してください。2つの変数を用いて、
# 足す、引く、かける、割る、割った余りを出力してください。

num1 = 5
num2 = 3

print("足す:", num1 + num2)
print("引く:", num1 - num2)
print("かける:", num1 * num2)
print("割る:", num1 / num2)
print("割った余り:", num1 % num2)


# 3. 条件式と論理型（boolean）について
# 初期値がFalseである論理型の変数を宣言してください。
# 問題2で宣言した2つの変数を足した結果が偶数であれば、論理型の変数にTrueを代入してください。

even_flag: bool = False

if(num1 + num2) % 2 == 0 :
  even_flag = True

# 4. 条件式
# 設問3のboolean型の変数を利用した条件式を作成し、以下のように出力してください。
# 偶数なら「偶数です」
# 奇数なら「奇数です」

  even_flag = True

if(even_flag):
  print("偶数です")
else:
  print("奇数です")
