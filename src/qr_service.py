import segno
import os
import sys

def generate_custom_qr(data: str, filename: str, dark_color="#10b981", light_color="#FFFFFF", scale=10):
    os.makedirs("qrs", exist_ok=True)
    qr = segno.make(data, error='h')
    path = os.path.join("qrs", f"{filename}.png")
    qr.save(path, scale=scale, border=4, dark=dark_color, light=light_color)
    return path

def show_in_terminal(data: str):
    qr = segno.make(data)
    # Basic terminal output to avoid TypeError
    # If it looks 'inverted' on your screen, don't worry—the PNG file is the source of truth.
    qr.terminal(border=2)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        data_input = sys.argv[1]
        file_name = sys.argv[2] if len(sys.argv) > 2 else "custom_qr"
        chosen_color = sys.argv[3] if len(sys.argv) > 3 else "#10b981"
        
        generate_custom_qr(data_input, file_name, dark_color=chosen_color)
        print(f"\n--- Preview for: {data_input} ---")
        show_in_terminal(data_input)
        print(f"--- Saved to qrs/{file_name}.png ---\n")
    else:
        show_in_terminal("PharmaGO-Test")