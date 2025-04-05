# Описание класса




class Chocolate:
    name = "Nuts"
    company = "Nestle"
    parameters = "Расчет параметров"
    def __init__(self, nutritional_value: int =100, energy_value: int = 2124, proteins: float = 5.7, fats: int = 26, carbohydrates: int = 62 ) -> None:
        self.nutritional_value = nutritional_value
        self.energy_value = energy_value
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __len__(self) -> int:
        return 20

    def get_nutritional_value(self) -> str:
        return f"Пищевая ценность на {self.nutritional_value} гр порции"

    def get_energy_value(self) -> str:
        return f"Энергетическая ценность: {self.energy_value} кДж"

    def get_proteins(self) -> str:
        return f"Белки: {self.proteins} г"

    def get_fats(self) -> str:
        return f"Жиры: {self.fats} г"

    def get_carbohydrates(self) -> str:
        return f"Углеводы: {self.carbohydrates} г"

    def update_fats(self, new_fats: str) -> None:
        self.fats = new_fats

def change_name(new_name: str) -> None:
    Chocolate.name = new_name

class Mars(Chocolate):
    name = "Mars"
    company = "Mars"
    def __init__(self, length:int, energy_value: int, proteins: float, fats: int, carbohydrates: int, nutritional_value: int):
        super().__init__(nutritional_value=nutritional_value,  energy_value= energy_value, proteins=proteins, fats=fats, carbohydrates=carbohydrates)
        self.length = length

    def get_length(self):
        return f"Длина шоколадки: {self.length} см"



nuts = Chocolate()
nuts_mini = Chocolate(50, 1061, 2.6, 11, 32)
mars = Mars(7, 1913, 3.8, 15, 68, 100)
mars.update_fats("18")
change_name("Nuts XXL")
print(f" {Chocolate.parameters} для шоколадки {Chocolate.name} от компании {Chocolate.company}:"
      f"\n {nuts.get_nutritional_value()} "
      f"\n {nuts.get_energy_value()} "
      f"\n {nuts.get_proteins()}"
      f"\n {nuts.get_fats()}"
      f"\n {nuts.get_carbohydrates()}"
      f"\n Длина шоколадки: {len(nuts)} см")
print(f"\n {nuts_mini.get_nutritional_value()} "
      f"\n {nuts_mini.get_energy_value()} "
      f"\n {nuts_mini.get_proteins()}"
      f"\n {nuts_mini.get_fats()}"
      f"\n {nuts_mini.get_carbohydrates()}")

print(f" \n"
      f"\n {Chocolate.parameters} для шоколадки {Mars.name} от компании {Mars.company}:"
      f"\n {mars.get_nutritional_value()} "
      f"\n {mars.get_energy_value()} "
      f"\n {mars.get_proteins()}"
      f"\n {mars.get_fats()}"
      f"\n {mars.get_carbohydrates()}"
      f"\n {mars.get_length()}")


# Пояснение кода:
# создаю базовый класс Chocolate с 3-мя атрибутами класса названием/вложенной строкой по умолчанию
# затем в классе переопределяем метод init который принимает параметры со значениями по умолчанию (а также делаем аннотацию типов параметров и
# выводимого значения) которые
# потом становятся атрибутами объекта тк создаются внутри метода с помощью self а не принадлежат классу в целом
# далее определяем магический метод len который рассматривался в лекции и задаем ему возврат фиксированного значения
# далее создаем 5 методов для получения информации и 2 для изменения атрибутов (один для атрибута объекта, другой для атрибута класса)
# методы - это функция/процедура которая принадлежит классу/экземпляру класса
#
# также я решила на основе лекций создать наследуемый от родительского класса класс Mars
# в котором также создаем свои атрибуты класса и сливаем метод init с init из родительского класса (передаем параметры и с помощью
# функции super вызываем метод родит. Класса в который также передаем наши параметры) также в параметрах добавила новый параметр и
# сделала его атрибутом объекта с помощью self
#
# ниже создаю 3 объекта
# nuts и nuts_mini - объекты по классу Chocolate, nuts обращается к классу и когда мы вызываем методы и атрибуты в print он выводит
# дефолтные значения, вызывая методы через nuts_mini у параметров уже выводятся новые переопределенные значения
# mars объект по дочернему классу Mars
# в данном случае у нас нет дефолтных значений поэтому мы должны вписать их в скобках чтобы они присвоились параметрам
# ниже мы переопределяем значение fats для mars и тк объект по наследуемому классу он берет метод из родительского класса
# и меняет значение
# при этом get_length() мы не сможем использовать для объектов по классу Chocolate тк этот метод создан в дочернем классе
# и относится только к нему
#
# далее вызываю методы из класса объектов и вывожу, для наглядности вывела все значения что были
#
# функция change_name() принимает новое имя в качестве аргумента
# сначала я написала это на основе того как было написано в примере но
# программа выделяла это желтым цветом и предложила свое исправление
# и убрала функцию из класса
# тем не менее функция изменяет имя именно для класса Chocolate обращаясь к атрибуту класса name в Chocolate
# для экземпляров nuts и nuts_mini при обращении к name будет возвращаться новое значение, так как они наследуют атрибут класса
# для экземпляра mars ничего не изменится, так как класс Mars имеет собственный атрибут name, который переопределяет атрибут родительского класса
# также change_name определена как отдельная функция, а не как метод класса Chocolate
# поэтому её нужно вызывать напрямую