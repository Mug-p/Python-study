"""类的基础练习。"""


class Student:
    """保存学生的姓名和成绩。"""

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def introduce(self):
        """打印学生的自我介绍。"""
        print(f"大家好，我叫{self.name}，我的成绩是{self.score}分。")


if __name__ == "__main__":
    student = Student("小明", 88)
    student.introduce()
