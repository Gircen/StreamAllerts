import dearpygui.dearpygui as dpg

with dpg.font_registry():
    with dpg.font("resources/NotoSerifCJKjp-Medium.otf", 20, default_font=True) as font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        dpg.bind_font(font)
