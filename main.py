def find_narcissistic_numbers():
    print("正在寻找水仙花数（100-999）...")
    results = []

    for num in range(100, 1000):
        # 拆分个、十、百位
        hundreds = num // 100
        tens = (num // 10) % 10
        ones = num % 10

        # 判断：各位数字的立方和是否等于原数
        if num == (hundreds**3 + tens**3 + ones**3):
            results.append(num)

    return results

if __name__ == "__main__":
    numbers = find_narcissistic_numbers()
    print(f"找到的水仙花数: {numbers}")