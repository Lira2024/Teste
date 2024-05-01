import flet as ft
from flet import colors

botoes = [
    {'operador': 'AC', 'corfont': colors.BLACK, 'corfundo': colors.BLUE_GREY_100},
    {'operador': '±', 'corfont': colors.BLACK, 'corfundo': colors.BLUE_GREY_100},
    {'operador': '%', 'corfont': colors.BLACK, 'corfundo': colors.BLUE_GREY_100},
    {'operador': '/', 'corfont': colors.WHITE, 'corfundo': colors.ORANGE},
    {'operador': '7', 'corfont': colors.WHITE, 'corfundo': colors.WHITE24},
    {'operador': '8', 'corfont': colors.WHITE, 'corfundo': colors.WHITE24},
    {'operador': '9', 'corfont': colors.WHITE, 'corfundo': colors.WHITE24},
    {'operador': '*', 'corfont': colors.WHITE, 'corfundo': colors.ORANGE},
    {'operador': '4', 'corfont': colors.WHITE, 'corfundo': colors.WHITE24},
    {'operador': '5', 'corfont': colors.WHITE, 'corfundo': colors.WHITE24},
    {'operador': '6', 'corfont': colors.WHITE, 'corfundo': colors.WHITE24},
    {'operador': '-', 'corfont': colors.WHITE, 'corfundo': colors.ORANGE},
    {'operador': '1', 'corfont': colors.WHITE, 'corfundo': colors.WHITE24},
    {'operador': '2', 'corfont': colors.WHITE, 'corfundo': colors.WHITE24},
    {'operador': '3', 'corfont': colors.WHITE, 'corfundo': colors.WHITE24},
    {'operador': '+', 'corfont': colors.WHITE, 'corfundo': colors.ORANGE},
    {'operador': '0', 'corfont': colors.WHITE, 'corfundo': colors.WHITE24},
    {'operador': '.', 'corfont': colors.WHITE, 'corfundo': colors.WHITE24},
    {'operador': '=', 'corfont': colors.WHITE, 'corfundo': colors.ORANGE},
]


def main(page: ft.Page):
    page.bgcolor = '#000'
    page.window_resizable = False
    page.window_width = 270
    page.window_height = 390
    page.title = 'My Calc'
    page.window_always_on_top = True

    resultado = ft.Text(value='0', color=colors.WHITE, size=20)

    def calculator():
        expression = resultado.value

        try:
            result = str(eval(expression))
            return result
        except Exception as e:
            return "Error"

    def Select(e):
        value_atual = resultado.value if resultado.value != '0' else ''
        value = e.control.content.value
        if value.isdigit() or value == '.':
            value = value_atual + value
        elif value in ('+', '-', '*', '/'):
            value = value_atual + ' ' + value + ' '
        elif value == '=':
            value = calculator()
        elif value == 'AC':
            value = '0'
        elif value == '±':
            pass
        elif value == '%':
            pass
        resultado.value = value
        resultado.update()

    display = ft.Row(
        width=250,
        controls=[resultado],
        alignment='end',
    )

    botao = [ft.Container(
        content=ft.Text(value=botao['operador'], color=botao['corfont']),
        width=50,
        height=50,
        bgcolor=botao['corfundo'],
        border_radius=100,
        alignment=ft.alignment.center,
        on_click=Select

    ) for botao in botoes]

    keyboard = ft.Row(
        width=250,
        wrap=True,
        controls=botao,
        alignment='end',
    )

    page.add(display, keyboard)


ft.app(target=main)