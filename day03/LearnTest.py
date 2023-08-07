"""
需求：输入三角形的3边，如果两边的长度大于第三条边，则代表是一个合法三角形
① 要求手工输入三角形的3边，涉及到input()输入，数据类型转换
② 三角形的每2边之后 > 第3条边
"""
side_a = float(input("a边长："))
side_b = float(input("b边长："))
side_c = float(input("c边长："))
result = "可以" if side_a + side_b > side_c and side_b + side_c > side_a and side_c + side_a > side_b else "不可以"
print(f'这三条边{result}组成一个三角形')
