from typing import Optional

from dataclasses import dataclass


@dataclass
class PCModel:
    photo: str
    name: str
    screen: float
    CPU: str
    memory: str
    price: float


@dataclass
class PCMark:
    name: str
    models: list[PCModel]


class Database:
    _PC_MARKS = {
        'LENOVO': PCMark(
            name='LENOVO',
            models=[
                PCModel(
                    photo='LENOVO/1.png',
                    name='IdeaPad 314ITL6',
                    screen=14,
                    CPU='Intel Core i3',
                    memory='SSD 512 ГБ',
                    price=46_015,
                ),
                PCModel(
                    photo='LENOVO/2.png',
                    name='V15-ADA',
                    screen=15.6,
                    CPU='AMD Ryzen 3 3250U',
                    memory='SSD 256 ГБ',
                    price=31_561,
                ),
                PCModel(
                    photo='LENOVO/3.png',
                    name='ThinkBook 15 G2-ARE',
                    screen=15.6,
                    CPU='AMD Ryzen 3 4300U',
                    memory='SSD 256 ГБ',
                    price=44_800,
                ),
            ]
        ),
        'HP': PCMark(
            name='HP',
            models=[
                PCModel(
                    photo='HP/1.png',
                    name='15s-eq2022ur',
                    screen=15,
                    CPU='AMD Ryzen 5',
                    memory='SSD 256 ГБ',
                    price=60_994,
                ),
                PCModel(
                    photo='HP/2.png',
                    name='ProBook 430 G7',
                    screen=13,
                    CPU='Intel Core i3',
                    memory='SSD 256 ГБ',
                    price=42_928,
                ),
                PCModel(
                    photo='HP/3.png',
                    name='14s-dq2007ur',
                    screen=14,
                    CPU='Intel Pentium Gold',
                    memory='SSD 256 ГБ',
                    price=30_990,
                ),
            ]
        ),
        'Asus': PCMark(
            name='Asus',
            models=[
                PCModel(
                    photo='Asus/1.png',
                    name='E410MA-EB338T',
                    screen=14,
                    CPU='Intel Pentium Silver',
                    memory='SSD 256 ГБ',
                    price=33_990,
                ),
                PCModel(
                    photo='Asus/2.png',
                    name='Gaming F15 FX506LH-HN197T',
                    screen=15,
                    CPU='Intel Core i5',
                    memory='SSD 512 ГБ',
                    price=89_073,
                ),
                PCModel(
                    photo='Asus/3.png',
                    name='90NB0RLF-M02400',
                    screen=14,
                    CPU='Intel Core i3',
                    memory='SSD 256 ГБ',
                    price=49_823,
                ),
            ]
        ),
    }

    @classmethod
    def get_names(cls) -> list[str]:
        return [mark.name for mark in cls._PC_MARKS.values()]

    @classmethod
    def get_mark_by_name(cls, name: str) -> Optional[PCMark]:
        return cls._PC_MARKS.get(name)
