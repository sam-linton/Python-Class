import math
import tkinter as tk
from tkinter import ttk


# --- Safe evaluation environment ---
SAFE_ENV = {
    name: getattr(math, name) for name in dir(math)
    if not name.startswith("_")
}
SAFE_ENV["x"] = 0  # placeholder


def safe_eval(expr, x):
    """Safely evaluates the expression with x."""
#     SAFE_ENV["x"] = x
#     return eval(expr, {"__builtins__": {}}, SAFE_ENV)
    return eval(expr)


# --- Graphing App ---
class GraphApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Graphing App")
        self.geometry("700x500")

        # Layout frame
        control = ttk.Frame(self, padding=10)
        control.pack(side="top", fill="x")

        ttk.Label(control, text="f(x) =").pack(side="left")
        self.expr_var = tk.StringVar(value="x*x")
        ttk.Entry(control, textvariable=self.expr_var, width=30).pack(side="left", padx=5)
        ttk.Button(control, text="Graph", command=self.draw_graph).pack(side="left")

        # Canvas
        self.canvas = tk.Canvas(self, background="white")
        self.canvas.pack(fill="both", expand=True)

        # Graph settings
        self.x_min = -10
        self.x_max = 10
        self.y_min = -10
        self.y_max = 10

        # Redraw axes on window resize
        self.canvas.bind("<Configure>", lambda e: self.draw_graph())

    def draw_axes(self):
        self.canvas.delete("axes")

        w = self.canvas.winfo_width()
        h = self.canvas.winfo_height()

        # X axis
        x0 = self.world_to_screen_x(self.x_min)
        x1 = self.world_to_screen_x(self.x_max)
        y = self.world_to_screen_y(0)
        self.canvas.create_line(x0, y, x1, y, fill="gray", tags="axes")

        # Y axis
        y0 = self.world_to_screen_y(self.y_min)
        y1 = self.world_to_screen_y(self.y_max)
        x = self.world_to_screen_x(0)
        self.canvas.create_line(x, y0, x, y1, fill="gray", tags="axes")

    def world_to_screen_x(self, x):
        w = self.canvas.winfo_width()
        return (x - self.x_min) / (self.x_max - self.x_min) * w

    def world_to_screen_y(self, y):
        h = self.canvas.winfo_height()
        return h - (y - self.y_min) / (self.y_max - self.y_min) * h

    def draw_graph(self, *_):
        expr = self.expr_var.get()
        self.canvas.delete("graph")

        # Draw axes
        self.draw_axes()

        w = self.canvas.winfo_width()
        points = []

        for pixel_x in range(w):
            # Convert canvas x → math world x
            x = self.x_min + pixel_x * (self.x_max - self.x_min) / w
            try:
                y = safe_eval(expr, x)
            except Exception:
                continue

            px = pixel_x
            py = self.world_to_screen_y(y)
            points.append((px, py))

        # Draw line segments
        for i in range(len(points) - 1):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            self.canvas.create_line(x1, y1, x2, y2, fill="blue", tags="graph")


if __name__ == "__main__":
    app = GraphApp()
    app.mainloop()
