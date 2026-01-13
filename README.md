# Desktop Buddy Macropad 🎛️

Desktop Buddy Macropad is a compact **3-key macropad** with a **rotary encoder**, designed to make everyday computer tasks faster and more convenient. Each key launches a specific application, while the rotary dial provides smooth system volume control.

This project is being built as part of the **Hackpad YSWS**, with a focus on simplicity, usability, and learning the fundamentals of PCB and case design.

---

## ✨ Features

- **3 Mechanical Keys**  
  Each key is mapped to open a specific application (for example: browser, music app, or code editor).

- **Rotary Encoder (EC11)**  
  - Rotate: Volume up / down  
  - Press: Mute  

- **Minimal Desktop Design**  
  No display or unnecessary complexity — focused on reliability and fast input.

- **QMK Firmware**  
  Fully programmable key behavior and encoder actions.

---

## 🎯 Project Goals

- Build a **minimal and functional macropad**
- Learn **PCB design using KiCad**
- Learn **basic case design using Fusion 360**
- Create a Hackpad that is **easy to assemble and customize**

---

## 🧩 Hardware Overview

- **Microcontroller:** Seeed XIAO RP2040  
- **Switches:** MX-style mechanical switches (3×)  
- **Encoder:** EC11 Rotary Encoder  
- **LEDs:** Optional WS2812B RGB LEDs (for underglow or status indication)

---

## 🧱 Case Design

The case will be designed in **Fusion 360** and **3D printed**.

- Compact footprint for desk use  
- Designed to securely hold the PCB  
- Fastened using **M3 screws and heat-set inserts**

![Desktop Buddy Macropad CAD](images/CAD.png)

## 🖥️ PCB Design

- Designed in **KiCad**
- Custom PCB including:
  - 3 MX switch footprints  
  - 1 rotary encoder footprint  
  - XIAO RP2040 footprint  
- PCB size kept under **100 mm × 100 mm** for cost efficiency

![Desktop Buddy Macropad PCB](images/images_pcb.png)

![Desktop Buddy Macropad Schematic](images/images_schematic.png)

## 💾 Firmware Overview

Desktop Buddy Macropad uses **QMK firmware**.

Planned behavior:
- **Key 1:** Open Application A  
- **Key 2:** Open Application B  
- **Key 3:** Open Application C  
- **Encoder rotate:** Volume up / down  
- **Encoder press:** Mute  

Key mappings can be updated later through firmware changes.

---

## 📦 Bill of Materials (BOM)

| Quantity | Item |
|--------|------|
| 3× | MX Mechanical Switches |
| 3× | DSA Keycaps |
| 3× | 1N4148 DO-35 Diodes |
| 1× | EC11 Rotary Encoder |
| 1× | Seeed XIAO RP2040 |
| Optional | WS2812B RGB LEDs |
| — | 3D printed case |
| — | M3 screws + heat-set inserts |

---

## 📂 Repository Structure

```text
/pcb        → KiCad schematic & PCB files
/case       → Fusion 360 CAD files
/firmware   → QMK firmware
/images     → Renders and progress images
