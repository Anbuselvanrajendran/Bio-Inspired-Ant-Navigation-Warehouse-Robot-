# Ant-Inspired GPS-Free Warehouse Navigation

## Overview
This project presents a bio-inspired navigation strategy for autonomous warehouse robots, inspired by the path integration behavior of desert ants. The objective is to demonstrate how a robot can navigate to a storage shelf and return to a docking station without using GPS, global maps, or external localization infrastructure.

The work is motivated by indoor warehouse environments where GPS signals are unreliable or unavailable.

---

## Biological Inspiration
Desert ants are capable of navigating long distances in featureless environments by continuously integrating their movement and orientation. They estimate distance traveled and heading direction to compute a direct return path to their nest after locating food.

This project abstracts that biological behavior and applies it to a warehouse automation scenario.

---

## Algorithm Summary
- Robot starts from a docking station (nest)
- Performs biased random exploration to locate a shelf (food source)
- Uses inertial sensing (IMU-inspired dead reckoning) to estimate position
- Upon reaching the shelf, computes a home vector
- Returns directly to the docking station using the shortest path

The navigation does not rely on GPS, pre-built maps, or vision-based localization.

---

## Simulation Description
The simulation is implemented in Python using NumPy and Matplotlib.

The animation visualizes:
- Random exploration path (outbound)
- Shelf contact detection
- Direct return trajectory to the dock
- Warehouse-relevant spatial layout

Additionally, trajectory plots are generated to verify path integration behavior.

---

## How to Run
Install required dependencies:
```bash
pip install numpy matplotlib
