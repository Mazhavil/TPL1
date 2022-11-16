# -*- coding: utf-8 -*-
from CalcLowRating import CalcLowRating
from src.Types import DataType
import pytest

RatingType = (list[str], int)


class TestCalcLowRating:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingType]:

        data: DataType = {
            "Прайс_Джон_Сергеевич":
                [
                    ("математика", 60),
                    ("русский язык", 59),
                    ("социология", 100)
                ],

            "Кожухов_Виктор_Денисович":
                [
                    ("математика", 39),
                    ("русский язык", 44),
                    ("программирование", 21),
                    ("литература", 77)
                ]
        }

        # Без split мой список будет не из строк, а из символов...
        classman_output: RatingType = (
            list("Прайс_Джон_Сергеевич".split(sep="dummyseparator")), 1
        )

        return data, classman_output

    def test_init_calc_rating(self, input_data: tuple[DataType,
                                                      RatingType]) -> None:

        calc_classman = CalcLowRating(input_data[0])
        assert input_data[0] == calc_classman.data

    def test_calc(self, input_data: tuple[DataType, RatingType]) -> None:

        classman = CalcLowRating(input_data[0]).calc(2)
        assert pytest.approx(classman) == input_data[1]
