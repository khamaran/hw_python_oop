"""Константа для перевода значений из метров в километры"""
M_IN_KM = 1000

class InfoMessage():
    """Информационное сообщение о тренировке."""
    def __init__(self, training_type: str, duration: float, distance: float, speed: float, calories: float):
        self.training_type = training_type
        self.duration = duration
        self.distance = distance
        self.speed = speed
        self.calories = calories


    def get_message(self):
        return (f'Тип тренировки: {self.training_type}; Длительность: {self.duration} ч.; '
                f'Дистанция: {self.distance} км; Ср. скорость: {self.speed} км/ч; '
                f' Потрачено ккал: {self.calories}.')

class Training:
    """Базовый класс тренировки."""
    LEN_STEP = 0.65 
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action
        self.duration = duration
        self.weight = weight
    

    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        distance: float = self.action * self.LEN_STEP / M_IN_KM
        return f'Преодолённая дистанция за тренировку - {distance:.3f} км.'

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        speed = (self.action * self.LEN_STEP / M_IN_KM)/self.duration
        return f'Средняя скорость движения - {speed:.3f}'
         

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        pass


class Running(Training):
    CALORIES_MEAN_SPEED_MULTIPLIER = 18
    CALORIES_MEAN_SPEED_SHIFT = 1.79 
    """Тренировка: бег."""

    def __init__(self, action: int, duration: float, weight: float,) -> None:
                 super().__init__(action, duration, weight)
    

    def get_distance(self) -> float:
        return super().get_distance()  


    def get_mean_speed(self) -> float:
        return super().get_mean_speed() 

    
    def get_spent_calories(self) -> float:
        speed = (self.action * self.LEN_STEP / M_IN_KM)/self.duration
        spent_calories = ((self.CALORIES_MEAN_SPEED_MULTIPLIER * speed + self.CALORIES_MEAN_SPEED_SHIFT)
 * self.weight / M_IN_KM * self.duration) 
        return f'Количество затраченных калорий - {spent_calories:.3f}'
    
    
    def show_training_info(self):
        return InfoMessage('бег',  self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories())

    

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    CALORIES_WEIGHT_MULTIPLIER = 0.035
    CALORIES_WEIGHT_SHIFT = 0.029
    LEN_STEP = 1.68


    def __init__(self, action: int, duration: float, weight: float, height: float) -> None:
                 super().__init__(action, duration, weight)
                 self.height = height


    def get_distance(self) -> float:
        return super().get_distance()  


    def get_mean_speed(self) -> float:
        return super().get_mean_speed() 

    
    def get_spent_calories(self) -> float:
        speed = (self.action * self.LEN_STEP / M_IN_KM)/self.duration
        spent_calories = ((self.CALORIES_WEIGHT_MULTIPLIER * self.weight + (speed**2 / self.height)
 * self.CALORIES_WEIGHT_SHIFT * self.weight) * self.duration) 
        return f'Количество затраченных калорий - {spent_calories:.3f}'
    
    def show_training_info(self):
        return InfoMessage('ходьба]',  self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories())

class Swimming(Training):
    CALORIES_SPEED_MULTIPLIER = 1.1
    LEN_STEP = 1.68
    """Тренировка: плавание."""
    
    def __init__(self, action: int, duration: float, weight: float, length_pool: float, count_pool: int) -> None:
                 super().__init__(action, duration, weight)
                 self.length_pool = length_pool
                 self.count_pool = count_pool


    def get_distance(self) -> float:
        return super().get_distance()  


    def get_mean_speed(self) -> float:
        speed = self.length_pool * self.count_pool / M_IN_KM / self.duration 
        return f'Средняя скорость движения - {speed:.3f}' 

    
    def get_spent_calories(self) -> float:
        speed = self.length_pool * self.count_pool / M_IN_KM / self.duration 
        spent_calories = ((speed * self.CALORIES_SPEED_MULTIPLIER) * 2 * self.weight * self.duration) 
        return f'Количество затраченных калорий - {spent_calories:.3f}'

    
    def show_training_info(self):
        return InfoMessage('плавание',  self.duration, self.get_distance(), self.get_mean_speed(), self.get_spent_calories())


def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    workout_types = {'SWM': Swimming, 'RUN': Running, 'WLK': SportsWalking}
    return workout_types[workout_type](*data)


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info()
    print(info.get_message())


if __name__ == '__main__':

    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)

