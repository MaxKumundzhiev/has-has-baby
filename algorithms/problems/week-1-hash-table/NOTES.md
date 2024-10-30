## hash functions
A hash function is any function that can be used to map data of arbitrary size to fixed-size values, though there are some hash functions that support variable-length output. The values returned by a hash function are called hash values, hash codes, hash digests, digests, or simply hashes.

```
примеры хэш функций
- Division Method - h(k)=k mod m, Where k is the key and 𝑚m is a prime number.
- Multiplication Method - h(k)=⌊m(kAmod1)⌋, Where ⌊ ⌋ denotes the floor function.
- Метод цепочек - когда храним несколько значений для 1 хэш ключа
- Метод откртой адресации - метод, когда при колизии мы изем другой индекс в уже аллоцированной памяти. Способ который ищет другую ячейку называется пробированием
    - линейное пробирование
    - квадратичное пробирование
    - двойное хеширование
- Mid-Square Method - ...
- Folding Method - ...
- Cryptographic Hash Functions - ...
- Universal Hashing - ...
- Perfect Hashing - ...
```

## Коллизии в hash functions
Коллизия хеш-функции — это такая пара блоков x и y, результат хеш-функции hash() от которых дает в результате одинаковый блок z. Коллизии возможны абсолютно у любой хеш-функции, так как множество входов на много превышает множетсво выходов хеш-функции.


## Методы разрешения коллизии в hash functions
1. Выбрать другую хэш фкнукцию
2. Метод открытой адресации
3. Метод цепочек

## Разница между хэш-таблицей и хеш-сетом
- Хэш таблица - это структура поддерживающая ключ:значение 
- Хэш сет - это структура поддерживающая только ключ

С точки зрения операций, хэш сет является более богатым и реализовавывает такие операции как "обьеденение", "пересечение", операции со множеством. Часто реализация таких операций сделана через структура данных Union - древовидная структура.

## Основные паттерны для работы с хеш табоицей
1. mapping - сопоставление
    - сразу заполнякм хэш-таблицу
    - постепенно заполнякм хэш-таблицу
2. key:frequency | frequency:key - посчитать k встречающихся элементов
3. elements count
    - hashmap
    - array
4. анаграммы
    - группировка по анаграмме
    - проверка на анаграмму
    - поиск анаграммы
