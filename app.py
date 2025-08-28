import gradio as gr

# Conversion logic
def convert_temperature(value, from_unit, to_unit):
    try:
        value = float(value)
    except ValueError:
        return "Invalid input"

    if from_unit == to_unit:
        return f"{value:.2f} {to_unit}"

    # Convert input to Celsius first
    if from_unit == "Celsius":
        celsius = value
    elif from_unit == "Fahrenheit":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "Kelvin":
        celsius = value - 273.15

    # Convert Celsius to target unit
    if to_unit == "Celsius":
        result = celsius
    elif to_unit == "Fahrenheit":
        result = (celsius * 9 / 5) + 32
    elif to_unit == "Kelvin":
        result = celsius + 273.15

    return f"{result:.2f} {to_unit}"

units = ["Celsius", "Fahrenheit", "Kelvin"]

with gr.Blocks() as demo:
    gr.Markdown("# 🌡️ Temperature Converter")
    
    with gr.Row():
        input_value = gr.Textbox(label="Enter temperature value", placeholder="e.g. 100")
        from_unit = gr.Dropdown(choices=units, label="From Unit", value="Celsius")
        to_unit = gr.Dropdown(choices=units, label="To Unit", value="Fahrenheit")
    
    convert_btn = gr.Button("Convert")
    output = gr.Textbox(label="Converted Temperature")

    convert_btn.click(convert_temperature, inputs=[input_value, from_unit, to_unit], outputs=output)

demo.launch()
