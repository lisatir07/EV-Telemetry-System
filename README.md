# STM32 EV Telemetry System

A miniature electric vehicle telemetry system designed to demonstrate how embedded systems can collect, transmit, process, and visualize real-time vehicle data.

## Project Overview

This project is a small-scale EV telemetry system built around an **STM32 microcontroller**. The system collects vehicle data such as battery voltage, motor temperature, and throttle position, then transmits the data to a computer for processing and visualization.

The goal is to recreate, on a smaller scale, the data pipeline used in real-world vehicles:

**Sensors → Embedded Firmware → Serial Communication → Data Processing → Live Dashboard**

The project combines **embedded systems, sensor interfacing, serial communication, Python data processing, and data visualization**.

## Features

- Collects vehicle telemetry from multiple sensors
- Reads and processes sensor data using an STM32 microcontroller
- Transmits telemetry data through UART
- Processes incoming data using Python
- Displays telemetry through a live Streamlit dashboard
- Visualizes battery voltage and motor temperature
- Records telemetry data to CSV for later analysis
- Displays system status based on vehicle data

## Technologies Used

### Software

- **C** — Embedded firmware development
- **Python** — Telemetry processing and data handling
- **Pandas** — Data processing and CSV logging
- **Streamlit** — Interactive telemetry dashboard
- **STM32CubeIDE** — STM32 development
- **STM32CubeMX** — Microcontroller configuration
- **VS Code** — Python development
- **Git & GitHub** — Version control and project management

### Hardware

- **STM32F103C8T6 "Blue Pill"** — Main microcontroller
- **ST-Link V2** — Programming and debugging
- **Temperature sensor** — Motor temperature measurement
- **Voltage sensor** — Battery voltage measurement
- **Potentiometer** — Simulated throttle input
- **Breadboard and jumper wires** — Hardware prototyping


## System Architecture

```text
┌──────────────┐
│    Sensors   │
│              │
│ • Voltage    │
│ • Temperature│
│ • Throttle   │
└──────┬───────┘
       │
       ▼
┌─────────────────┐
│  STM32F103C8T6  │
│                 │
│ Embedded        │
│ Firmware        │
└──────┬──────────┘
       │
      UART
       │
       ▼
┌─────────────────┐
│ Python          │
│ Telemetry       │
│ Processing      │
└──────┬──────────┘
       │
       ├──────────────► CSV Data Logging
       │
       ▼
┌─────────────────┐
│ Streamlit       │
│ Dashboard       │
│                 │
│ • Voltage       │
│ • Temperature   │
│ • System Status │
└─────────────────┘
```

## Current Status

### Completed

- [x] Python telemetry pipeline
- [x] Simulated vehicle telemetry
- [x] CSV data logging
- [x] Streamlit dashboard
- [x] Battery voltage visualization
- [x] Motor temperature visualization
- [x] System status indicator

### In Progress

- [ ] STM32 firmware implementation
- [ ] Sensor wiring and testing
- [ ] STM32-to-PC UART communication
- [ ] Integration of live hardware data with the Python dashboard
- [ ] Hardware validation and testing

> **Note:** The software side of the project is currently functional using simulated telemetry data. The hardware integration is still in development.