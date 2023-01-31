# Lissajous Curve Table Visualization with Pygame-Zero

A visual representation of the Lissajous Curve Table using the Pygame-Zero library.

## What are Lissajous Curves?

Lissajous curves are a type of parametric curve that is often used in physics, engineering, and mathematics. It is defined by two parametric equations:

```
x = A * sin(at + d)
y = B * sin(bt)
```


where `A`, `B`, `a`, `b`, `t`, and `d` are variables that can be adjusted to generate different Lissajous curves.

## Project Structure

The project consists of two Python scripts:

- `lissajous.py`: This is the main script that runs the visualization. It creates an instance of the `Curve` class for each curve in the Lissajous table and displays them on the screen.

- `curve.py`: This script contains the `Curve` class, which represents each curve in the Lissajous table visualization. It contains properties for the curve's parameters and methods for calculating its position and drawing it on the screen.

## Demo Images

![demo](/demo.gif)
