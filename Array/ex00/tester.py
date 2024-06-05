from give_bmi import give_bmi, apply_limit


try:
    height = [2.71, 1.58]
    weight = [165.3, 55]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 22.5))
except Exception as e:
    print(e)
