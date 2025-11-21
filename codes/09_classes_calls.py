from codes.classes_fourcals import FourCal # FourCal 클래스를 불러오기

# 클래스를 가져옴.
if __name__ == "__main__":
    forucal = FourCal() # 원본 복제
    print(f"3 + 5 = {forucal.add(3, 5)}") 
    print(f"10 + 4 = {forucal.sub(10, 4)}")
    print(f"2 + 6 = {forucal.mul(2, 6)}")
    print(f"8 + 2 = {forucal.div(8, 2)}")

    pass