# Display Image & text on I2C driven ssd1306 OLED display 
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf
from time import sleep

i2c = I2C(0, sda=Pin(12), scl=Pin(13), freq=40000)
#oled = SSD1306_I2C(width, height, i2c)                  # Init oled display
oled = SSD1306_I2C(128, 64, i2c)
# Raspberry Pi logo as CAR

buffer = bytearray(b"\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xc0\x03\xff\xff\xff\
\xff\xff\xfc\x00\x00\x3f\xff\xff\
\xff\xff\xf0\x00\x00\x0f\xff\xff\
\xff\xff\xc0\x00\x00\x03\xff\xff\
\xff\xff\x80\x00\x00\x01\xff\xff\
\xff\xfe\x00\x00\x00\x00\x7f\xff\
\xff\xfc\x00\x00\x00\x00\x3f\xff\
\xff\xf8\x00\x00\x00\x00\x1f\xff\
\xff\xf0\x00\x00\x00\x00\x1f\xff\
\xff\xf0\x00\x00\x00\x00\x07\xff\
\xff\xe0\x00\x00\x00\x00\x07\xff\
\xff\xc0\x00\x00\x00\x00\x03\xff\
\xff\x80\x00\x00\x00\x00\x01\xff\
\xff\x80\x00\x00\x00\x00\x01\xff\
\xff\x00\x00\x00\x00\x00\x00\xff\
\xff\x00\x00\x00\x00\x00\x00\x7f\
\xfe\x00\x00\x00\x00\x00\x00\x7f\
\xfe\x00\x00\x00\x00\x00\x00\x7f\
\xfe\x00\x00\x00\x00\x00\x00\x7f\
\xfc\x00\x00\x00\x00\x00\x00\x3f\
\xfc\x00\x00\x00\x00\x00\x00\x3f\
\xfc\x00\x00\x00\x00\x00\x00\x3f\
\xfc\x00\x00\x00\x00\x00\x00\x1f\
\xf8\x01\x00\x00\x00\x00\x00\x3f\
\xfc\x03\x80\x00\x00\x00\xe0\x1f\
\xf8\x03\xf0\x00\x00\x07\xf0\x1f\
\xf8\x01\xfe\x00\x00\x1f\xc0\x1f\
\xfc\x00\x3f\x00\x00\x7e\x00\x1f\
\xf8\x00\x0e\x00\x00\x38\x00\x3f\
\xfc\x00\x00\x00\x00\x00\x00\x1f\
\xfc\x00\x00\x00\x00\x00\x00\x3f\
\xfc\x00\x00\x00\x00\x00\x00\x3f\
\xfc\x00\x00\x00\x00\x00\x00\x3f\
\xfc\x00\x00\x00\x00\x00\x00\x3f\
\xfe\x00\x00\x00\x00\x00\x00\x7f\
\xfe\x00\x00\x00\x00\x00\x00\x7f\
\xfe\x00\x00\xaa\xaa\x00\x00\x7f\
\xff\x00\x01\xff\xff\x80\x00\xff\
\xff\x00\x00\xff\xff\x00\x00\xff\
\xff\x80\x00\xff\xff\x00\x01\xff\
\xff\x80\x00\x7f\xfe\x00\x01\xff\
\xff\xc0\x00\x7f\xfc\x00\x03\xff\
\xff\xe0\x00\x1f\xf8\x00\x07\xff\
\xff\xe0\x00\x07\xc0\x00\x07\xff\
\xff\xf8\x00\x00\x00\x00\x0f\xff\
\xff\xf8\x00\x00\x00\x00\x1f\xff\
\xff\xfe\x00\x00\x00\x00\x3f\xff\
\xff\xfe\x00\x00\x00\x00\xff\xff\
\xff\xff\x80\x00\x00\x01\xff\xff\
\xff\xff\xe0\x00\x00\x07\xff\xff\
\xff\xff\xf0\x00\x00\x1f\xff\xff\
\xff\xff\xfe\x00\x00\x7f\xff\xff\
\xff\xff\xff\xc0\x07\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\
\xff\xff\xff\xff\xff\xff\xff\xff\
")

fb = framebuf.FrameBuffer(buffer, 64,64, framebuf.MONO_HLSB)  #50,42為原圖的像素
oled.fill(0)

# Blit the image from the framebuffer to the oled display
oled.blit(fb, 0, 0)

# Add some text
# oled.text("Pico",5,15)

# Finally update the oled display so the image & text is displayed
oled.show()