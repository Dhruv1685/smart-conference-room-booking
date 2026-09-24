# Smart Conference Room Booking System

An IoT-based automated conference room booking system that scans university ID card barcodes to auto-fill Google Forms, assigns available rooms in real-time, and displays all bookings in a centralized Google Sheets dashboard accessible in the cloud.

## Overview

In many universities, booking a conference room involves manually filling forms and checking room availability, which is time-consuming and inefficient. This system automates the entire workflow:

1. **Scan** - A student scans their university ID card barcode using a webcam-based scanner
2. **Auto-Fill** - The system automatically populates a Google Form with the student's details (name, ID, department, etc.)
3. **Room Assignment** - The backend checks room availability and assigns an available conference room
4. **Cloud Dashboard** - All bookings are reflected in real-time on a Google Sheets dashboard, accessible from anywhere

## Features

- **Real-time Barcode Scanning** - Instantly reads university ID card barcodes using OpenCV and pyzbar
- **Google Form Auto-Fill** - Eliminates manual data entry by automatically filling booking forms with student information
- **Automatic Room Assignment** - Intelligently assigns available conference rooms based on time slots and availability
- **Cloud-Based Dashboard** - Google Sheets integration for real-time visibility of all bookings
- **Duplicate Scan Prevention** - Built-in cooldown mechanism to prevent accidental double scans
- **Visual Feedback** - Live video feed with bounding boxes and decoded student ID displayed on screen
- **IoT Integration** - Raspberry Pi server acts as the bridge between the scanner and Google services

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| OpenCV | Webcam capture and real-time image processing |
| pyzbar | Barcode detection and decoding |
| Requests | HTTP communication with Raspberry Pi server |
| Flask | REST API server running on Raspberry Pi |
| Google Sheets API | Cloud-based booking dashboard and data storage |
| Google Forms | Auto-filled booking form for conference room requests |
| Raspberry Pi | IoT server hosting the backend logic |

## Project Structure

```
smart-conference-room-booking/
├── scanner.py              # Main barcode scanner client (improved)
├── barcode_scanner.py      # Barcode scanner client (base version)
├── .gitignore
└── README.md
```

## System Architecture

```
[University ID Card] 
        │
        ▼
[Webcam + Barcode Scanner] ──► Decodes student ID barcode
        │
        ▼
[Raspberry Pi Server (Flask)] ──► Processes student data
        │
        ├──► Auto-fills Google Form with student details
        │
        ├──► Checks room availability & assigns room
        │
        └──► Updates Google Sheets dashboard (cloud)
```

## Installation

### Prerequisites
- Python 3.7+
- Webcam connected to the client machine
- Raspberry Pi (or any server) with Flask installed
- Google API credentials (for Sheets and Forms integration)
- University ID cards with barcodes on the back

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Dhruv1685/smart-conference-room-booking.git
   cd smart-conference-room-booking
   ```

2. Install dependencies:
   ```bash
   pip install opencv-python pyzbar requests flask gspread google-auth
   ```

3. Configure the Raspberry Pi IP address in the script:
   ```python
   PI_IP = "your_raspberry_pi_ip"
   URL = f"http://{PI_IP}:5000/scan"
   ```

4. Run the scanner:
   ```bash
   python scanner.py
   ```

5. Press **ESC** to exit the scanner.

## How It Works

1. The scanner opens the webcam and continuously captures frames.
2. When a university ID card barcode is detected, it decodes the student ID.
3. The decoded ID is sent via HTTP POST to the Raspberry Pi server.
4. The server maps the student ID to student details (name, department, year).
5. It automatically fills a Google Form with the booking request.
6. The system checks room availability and assigns an available room.
7. The booking is logged to a Google Sheets dashboard visible in real-time.
8. A cooldown timer ensures the same ID card isn't scanned twice within 3 seconds.

## Use Cases

- **University Campuses** - Students scan ID cards to book study rooms, seminar halls, or meeting rooms
- **Corporate Offices** - Employees scan badges to reserve conference rooms
- **Libraries** - Visitors book discussion rooms or private study areas
- **Co-working Spaces** - Members reserve shared meeting rooms on demand

## Resume Description

> Developed an IoT-based Smart Conference Room Booking System using Python, OpenCV, Flask, and Google Sheets API. Implemented real-time barcode scanning of university ID cards to auto-fill Google Forms and automatically assign available conference rooms. Built a cloud-based Google Sheets dashboard for real-time booking visibility. Deployed the backend on Raspberry Pi, enabling seamless integration between hardware and cloud services.

## License

This project is open-source and available for educational and personal use.

---

**Author:** Dhruv Patel  
**GitHub:** [Dhruv1685](https://github.com/Dhruv1685)
