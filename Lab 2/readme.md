# Лабораторная работа №2 Docker
# Выполнил Андреев Александр, студент группы 6233

## Задание 1

1. Был собран докер файл и образ.
```cmd
docker image build -t lab2:0.0.1 .
docker run -dit -v .\data:/usr/app/src --name mycontainer lab2:0.0.1
```
2. Был написан python скрипт, который выделял контуры методом согласования.
3. Была выбрана стандартная картинка для выделения конуторов
![input](https://github.com/SashkaShashka/Technologies_AI/assets/62326372/2ad277b8-2fb6-4870-90f3-099309a356dc)
4. Был запущен скрипт
```cmd
docker exec -it mycontainer python3 /usr/app/src/imageprocess.py
```

### Результат работы программы: ![output](https://github.com/SashkaShashka/Technologies_AI/assets/62326372/c34e0dfc-da5d-4e7a-8096-78fb15e7ddc1)

## Задание 2

1. Был собран докер файл
2. Написан python с использованием intel-isl/MiDaS модели.
3. Был запущен скрипт

### Результат работы программы: ![output_depth_map](https://github.com/SashkaShashka/Technologies_AI/assets/62326372/eb41482a-02ff-40ef-ae65-8344857584f1)
