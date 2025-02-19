class Ku:
    def __contains__(self, item):
        """ すべてのオブジェクトを包含する """
        return True

    def __eq__(self, other):
        """ Ku のインスタンス同士なら等しいが、他のオブジェクトとは等しくない """
        return isinstance(other, Ku)

    def __bool__(self):
        raise TypeError("このオブジェクトは真偽値を持ちません")

    def __repr__(self):
        return "Ku()"

    def __str__(self):
        return "Ku"


# インスタンス作成
ku = Ku()

# すべてのオブジェクトを包含する
print(42 in ku)        # True
print("hello" in ku)   # True
print(None in ku)      # True
print(Ku() in ku)      # True

# Ku のインスタンス以外とは等しくならない
print(ku == 42)        # False
print(ku == "hello")   # False
print(ku == None)      # False
print(ku == Ku()) # True（同じ Ku のインスタンスなら等しい）

print(str(ku))
print(bool(ku))

