# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.DataReaderXML import DataReaderXML


class TestDataReaderXML:

    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = """
            <root>
                <Хомутцов_Сергей_Викторович>
                    <математика>54</математика>
                    <литература>99</литература>
                </Хомутцов_Сергей_Викторович>
                <Джамбисов_Алексей_Пататович>
                    <математика>1</математика>
                    <химия>2</химия>
                </Джамбисов_Алексей_Пататович>
            </root>
        """

        data = {
            "Хомутцов_Сергей_Викторович": [
                ("математика", 54), ("литература", 99)
            ],
            "Джамбисов_Алексей_Пататович": [
                ("математика", 1), ("химия", 2)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("my_data.xml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = DataReaderXML().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
