import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.font_registry():
    with dpg.font("resources/NotoSerifCJKjp-Medium.otf", 20, default_font=True) as font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        dpg.bind_font(font)

window = dpg.add_window(tag="#Main", label="Главное окно", pos=(10, 40), height=30, width=40)

dpg.create_viewport(title='Сети', min_width=200, min_height=300, height=300, width=200)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("#Main", True)
dpg.start_dearpygui()
dpg.destroy_context()