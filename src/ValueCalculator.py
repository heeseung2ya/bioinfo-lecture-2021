class ValueCalculator:
    def __init__(self, val: str):
        self.val = val
    def __add__(self, other):
        return self.val + other.val

#print("hi") # 얘가 다른 곳에서 import할 때는 출력되지 않도록 하려면 어떻게 해야할까?

# 이렇게 하면 된다.
# import가 아닌 main에서 실행했을 때만 실행되도록 함.
if __name__ == "__main__":
    print("hi")
