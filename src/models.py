class Person:
    """人"""
    def __init__(self) -> None:
        self.name: str = ""
        self.age: int = 0
        self.tags: list[str] = []

    def __str__(self) -> str:
        return self.name


class Girl(Person):
    """女孩（继承 Person）"""
    def kiss(self, someone: Person) -> str:
        return f"「{self.name}」亲了下「{someone.name}」。"

    def fall_in_love_with(self, someone: Person) -> str:
        return f"「{self.name}」与「{someone.name}」坠入爱河。"
