# -*- coding: utf-8 -*-
from Types import DataType

RatingType = dict[str, bool]


class CalcLowRating:

    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
        self.tmp_student_dict: RatingType = {}
        self.res_names: list[str] = []

    # Возвращает список хорошистов и их количество
    def calc(self, needCount) -> (list[str], int):
        # Временный словарь, Имя студента -> Является ли хорошистом
        for key in self.data:
            self.tmp_student_dict[key] = False
            count = 0
            for (subject_name, subject_score) in self.data[key]:
                if subject_score < 61:
                    count += 1
                self.tmp_student_dict[key] = count == needCount

        # Результирующий словарь, оставляющий только студентов хорошистов
        for (key, value) in self.tmp_student_dict.items():
            if value:
                self.res_names.append(key)
        return self.res_names, len(self.res_names)
