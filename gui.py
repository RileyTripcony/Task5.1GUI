import tkinter as tk
import RPi.GPIO as GPIO

LED1_PIN = 13  # red
LED2_PIN = 15  # green
LED3_PIN = 16  # blue

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED1_PIN, GPIO.OUT)
GPIO.setup(LED2_PIN, GPIO.OUT)
GPIO.setup(LED3_PIN, GPIO.OUT)

def update_led(led):
    if led == 1:
        print("Turning on LED 1")
        GPIO.output(LED1_PIN, GPIO.HIGH)
        GPIO.output(LED2_PIN, GPIO.LOW)
        GPIO.output(LED3_PIN, GPIO.LOW)
    elif led == 2:
        print("Turning on LED 2")
        GPIO.output(LED1_PIN, GPIO.LOW)
        GPIO.output(LED2_PIN, GPIO.HIGH)
        GPIO.output(LED3_PIN, GPIO.LOW)
    elif led == 3:
        print("Turning on LED 3")
        GPIO.output(LED1_PIN, GPIO.LOW)
        GPIO.output(LED2_PIN, GPIO.LOW)
        GPIO.output(LED3_PIN, GPIO.HIGH)

def cleanup_gpio():
    print("Cleaning up GPIO")
    GPIO.cleanup()

def on_closing():
    cleanup_gpio()
    root.destroy()

root = tk.Tk()
root.title("LED Controller")
root.protocol("WM_DELETE_WINDOW", on_closing)

selected_led = tk.IntVar()
led1_radio = tk.Radiobutton(root, text="LED 1", variable=selected_led, value=1, command=lambda: update_led(1))
led2_radio = tk.Radiobutton(root, text="LED 2", variable=selected_led, value=2, command=lambda: update_led(2))
led3_radio = tk.Radiobutton(root, text="LED 3", variable=selected_led, value=3, command=lambda: update_led(3))

exit_button = tk.Button(root, text="Exit", command=on_closing)

led1_radio.grid(row=0, column=0)
led2_radio.grid(row=1, column=0)
led3_radio.grid(row=2, column=0)
exit_button.grid(row=3, column=0)

root.mainloop()
