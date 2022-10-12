# 1
print("*   *      **      ****      ****     *     *    /////")
print("*   *     *  *     *    *    *    *    *   *    | O O | ")
print("*****    *    *    ****      ****       * *    (|  ^  |) ")
print("*   *   ********   *    *    *    *      *      | [_] | ")
print("*   *  *        *  *     *   *     *     *       ----- ")
print("\n\n")
print("            +---+")
print("            |   |")
print("        +---+---+")
print("        |   |   |")
print("    +---+---+---+       /\\_/\\       -----")
print("    |   |   |   |      ( ' ' )    / Hello \\")
print("+---+---+---+---+      (  -  )   <  Junior |")
print("|   |   |   |   |       | | |     \\ Coder!/")
print("+---+---+---+---+      (__|__)      -----")
# 3
# 1stPlayer
# myprogram.java

# 4
x, y, z = 1, 2, 3
s0, v0, t, g = 4, 5, 6, 9.8
print(3 * x, 3 * x + y)
print(s0 + v0*t + (1/2) * g * t**2)
#6
x, y, m, n = 2.5, 1.5, 18, 4

print(x + n * y(x+n) * y)
print(m / n + m % n)
print(5 * x - n / 5)
print(1 - (1 - (1 - (1 - (1 - n)))))

#7
print(3 + 4.5 * 2 +27 /8)
# 논리연산시 경우에 따라 단축식 평가가 적용되기도 함.
print(True or False and 3 < 4 or not (5==7))

#print (not True > 'A')
print (not True > bool('A')) # print(not True > True)

#print(7 % 4 + 3 - 2 / 6 * 'Z')
print(7 % 4 + 3 - 2 / 6 * bool('Z'))

#print('D' + 1 + 'M' % 2 / 3)
print(bool('D') + 1 + bool('M') % 2 / 3)  #(1 + 1 + 1 % 2 / 3)

print(5.0 / 3. + 3 / 3)
print(53 % 21 < 45 / 18)

print((4 < 6) or True and False and (2 > 3)) # ((4 < 6) or False and False)

print((2 < 3) or (5 > 2) and not (4 == 4) or 9 != 4)
print(6 == 9 or 5 < 6 and 8 < 4 or 4 > 3)

#10
print(27 / 13 + 4)
print(27 / 13 + 4.0)
print(42.7 % 3 + 18)

# 논리식과 산술식이 결합된 수식에서는
# 논리식의 결과가 True면 값이 출력
# 논리식의 결과가 False면 0이 출력

print(23 / 5 + 23 / 5.0)

#print(2.0 + 'a') # 문자와 정수/실수간 산술연산 불가
#print(2 + 'a')

print('a' + 'b')
#print('a' / 'b') # 문자간 산술연산 불가

print('a' and not 'b')
print('a' and 'b')

#print((float)'a' / 'b') # 문자는 실수로의 형변환 불가

# 11
name = 'Harry'
weight = 65
age = 28
print(name, weight, age)

# 12
birthYear = 1990
currentYear = 2022
isPassBirth = True

age = currentYear - birthYear

print('연나이', age)
print('세는나이', age + 1)
print('만나이', age + 1 if isPassBirth else age )
#13
for j in range(1, 10) :
    val = 7 * j
    print(f'7 * {j:d} = {val:d}')


