





class duck:
    def __init__(self,name,sound):
        self.name = name
        self.sound = sound

    def swim(self):
        print(f"{self.name}이 헤엄칩니다.")

    def quack(self):
        print(f"{self.name}이 {self.sound} 하고 웁니다")

    def display(self):
        print(f"앗! 화면에 {self.name}가 나타났어요!")


class Mallard(duck):
    
    def __init__(self):
        self.name = "Mallard"
        self.sound = "청둥청둥"
        self.display_res = "청둥오리 리소스"

class Red(duck):
    
    def __init__(self):
        self.name = "RedheadDuck"
        self.sound = "빨강빨강"
        self.display_res = "빨간머리오리 리소스"


Mallard_duck = Mallard()

Mallard_duck.swim()


