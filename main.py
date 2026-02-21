from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.metrics import dp

# تنظیمات پنجره
Window.size = (350, 500)
Window.clearcolor = (0, 0, 0, 1)

class CalculatorApp(App):
    def build(self):
        # layout اصلی
        main_layout = BoxLayout(orientation='vertical', spacing=dp(5), padding=dp(10))
        
        # نمایشگر - فقط با HOSSEIN HAMIDY
        self.display = TextInput(
            text='HOSSEIN HAMIDY',
            font_size=dp(25),
            halign='center',
            readonly=True,
            background_color=(0.1, 0.1, 0.1, 1),
            foreground_color=(0, 1, 0, 1),
            size_hint_y=0.3
        )
        main_layout.add_widget(self.display)
        
        # دکمه‌ها
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['C', '0', '=', '+']
        ]
        
        grid = GridLayout(cols=4, spacing=dp(3), size_hint_y=0.7)
        
        for row in buttons:
            for text in row:
                if text == 'C':
                    color = (0.8, 0, 0, 1)  # قرمز
                elif text == '=':
                    color = (0, 0.8, 0, 1)  # سبز
                elif text in ['/', '*', '-', '+']:
                    color = (0, 0.5, 0.8, 1)  # آبی
                else:
                    color = (0.2, 0.2, 0.2, 1)  # خاکستری
                
                btn = Button(
                    text=text,
                    font_size=dp(25),
                    background_normal='',
                    background_color=color,
                    color=(1, 1, 1, 1),
                    bold=True
                )
                btn.bind(on_press=self.button_pressed)
                grid.add_widget(btn)
        
        main_layout.add_widget(grid)
        return main_layout
    
    def button_pressed(self, instance):
        text = instance.text
        
        # اگه صفحه HOSSEIN HAMIDY هست
        if self.display.text == 'HOSSEIN HAMIDY':
            if text == 'C':
                return  # میمونه HOSSEIN HAMIDY
            else:
                self.display.text = ''  # پاک میشه برای شروع محاسبه
                self.display.halign = 'right'
        
        # دکمه C
        if text == 'C':
            self.display.text = 'HOSSEIN HAMIDY'
            self.display.halign = 'center'
            return
        
        # دکمه مساوی
        if text == '=':
            try:
                result = eval(self.display.text)
                self.display.text = str(result)
            except:
                self.display.text = 'HOSSEIN HAMIDY'  # برگشت به اسم
                self.display.halign = 'center'
            return
        
        # اضافه کردن عدد یا عملگر
        if self.display.text == '0' or self.display.text == '':
            self.display.text = text
        else:
            self.display.text += text

if __name__ == '__main__':
    CalculatorApp().title = 'Calculator'
    CalculatorApp().run()