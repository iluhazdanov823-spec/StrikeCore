# StrikeCore Beta 0.1 — сборка APK прямо на Android

## Важно

Pydroid 3 удобен для разработки и запуска Python, но полноценная сборка APK
через Buildozer требует Linux-инструменты. На самом телефоне это обычно делают
через Termux + Linux-среду.

Этот архив уже содержит:
- buildozer.spec
- Android-friendly main.py
- Kivy dependency list
- landscape orientation
- ARM64 + ARMv7
- Android API 35 / min API 23
- LAN/Wi-Fi permissions
- исключение build/cache папок
- готовую структуру проекта

## Вариант через Termux

1. Установи Termux из F-Droid или официального источника проекта.
2. Дай Termux доступ к памяти:
   termux-setup-storage
3. Перейди в папку проекта.
4. Подготовь Linux-среду, Python, Java и Buildozer.
5. В корне StrikeCore выполни:
   buildozer android debug

Первую сборку не прерывай: Android SDK/NDK и другие компоненты могут
скачиваться и занимать много места.

## После сборки

APK должен появиться в:

    bin/

Его можно установить на Android для тестирования.

## Если Buildozer на телефоне не собирается

Это не означает, что проект сломан. На некоторых Android-конфигурациях
сборка Buildozer/NDK непосредственно на устройстве упирается в ограничения
Termux, архитектуры или свободного места. В таком случае Pydroid 3 оставляем
для разработки, а APK собираем в Linux/WSL.

## Следующий этап StrikeCore

Текущий APK-launcher специально минимальный: он проверяет, что Kivy-приложение
собирается и запускается на Android. После успешной проверки подключаем
реальное меню, локальный сервер/лобби и затем 3D-клиент.
