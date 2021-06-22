import time

try:
    while True:
        hora_actual = time.strftime('%H:%M:%S')
        print(hora_actual)

        time.sleep(1)

except KeyboardInterrupt:
    print('El Reloj se detuvo.')
