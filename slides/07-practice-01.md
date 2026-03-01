---
title: Lecture 07
subtitle: Computerized Process Automation with Human Input Devices
date: 2026-03-02
theme: "Frankfurt"
colortheme: "beaver"
fonttheme: "professionalfonts"
mainfont: Font-Regular.otf
mainfont: DejaVuSerif.ttf
sansfont: DejaVuSans.ttf
monofont: DejaVuSansMono.ttf
mathfont: texgyredejavu-math.otf
aspectratio: 169
header-includes:
 - \usepackage{tikz}
 - \usetikzlibrary{arrows.meta, positioning}
---

# Learning Objectives

By the end of this lecture, students will be able to:

- Explain how human input devices communicate with computers
- Describe the operating system input pipeline
- Explain how software simulates human input
- Use AutoHotKey to simulate keyboard input
- Explain hardware keystroke injection attacks
- Use Selenium to automate web input
- Understand security and ethical implications

---

# Lecture Outline

1. Human input device fundamentals
2. Operating system input pipeline
3. Software input simulation
4. Demonstration: AutoHotKey
5. Demonstration: USB keystroke injection
6. Demonstration: Selenium automation
7. Security implications
8. Ethics and defenses

---

# What is a Human Input Device?

A human input device converts human physical actions into digital signals.

Examples:

- Keyboard
- Mouse
- Touchscreen
- Microphone
- Camera
- Game controller
- Biometric reader

Purpose:

Allow humans to control computer systems.

---

# Input Device Architecture

\begin{tikzpicture}[
node distance=2.5cm,
every node/.style={draw, rectangle, minimum width=2.5cm, minimum height=1cm}
]

\node (human) {Human};
\node (device) [right of=human] {Input Device};
\node (driver) [right of=device] {Device Driver};
\node (os) [right of=driver] {Operating System};
\node (app) [right of=os] {Application};

\draw[->] (human) -- (device);
\draw[->] (device) -- (driver);
\draw[->] (driver) -- (os);
\draw[->] (os) -- (app);

\end{tikzpicture}

---

# Keyboard Example: Pressing a Key

When you press the "A" key:

1. Keyboard hardware detects press
2. Keyboard firmware generates scan code
3. USB transmits scan code
4. Device driver receives scan code
5. Operating system converts scan code to event
6. Application receives event

---

# Input Events

Operating systems use abstract input events.

Examples:

- KEYDOWN(A)
- KEYUP(A)
- MOUSEMOVE(x,y)
- CLICK(left)

Applications respond to events, not hardware directly.

---

# Event Queue Architecture

\begin{tikzpicture}[
node distance=4cm,
every node/.style={draw, rectangle, minimum width=3cm, minimum height=1cm}
]

\node (device) {Input Device};
\node (queue) [right of=device] {Event Queue};
\node (app) [right of=queue] {Application};

\draw[->] (device) -- (queue);
\draw[->] (queue) -- (app);

\end{tikzpicture}

---

# Critical Insight

If hardware can generate input events...

Software can generate input events too.

This enables:

- Automation
- Accessibility tools
- Testing frameworks
- Macros

And also:

- Malware
- Keystroke injection attacks

---

# Two Categories of Input Simulation

## Software-Level Simulation

Software tells OS to generate input events.

Examples:

- AutoHotKey
- xdotool
- AppleScript
- Selenium

---

## Hardware-Level Simulation

Device pretends to be keyboard.

Examples:

- Arduino Leonardo
- USB Rubber Ducky
- Malicious USB device

OS trusts the device automatically.

---

# Demonstration 1: AutoHotKey

AutoHotKey is a scripting language for input automation.

Example script:

```ahk
; demo.ahk
^j::
Send, Hello students!
Send, {Enter}
Send, This text was generated automatically.
Send, {Enter}
Send, Automation is powerful.
return
```

Press CTRL+J → automatic typing occurs.

---

# AutoHotKey Architecture

\begin{tikzpicture}[
node distance=4cm,
every node/.style={draw, rectangle, minimum width=3cm, minimum height=1cm}
]

\node (script) {AutoHotKey Script};
\node (os) [right of=script] {Operating System};
\node (app) [right of=os] {Application};

\draw[->] (script) -- (os);
\draw[->] (os) -- (app);

\end{tikzpicture}

---

# AutoHotKey Demo Project Structure

```
autohotkey-demo/
  demo.ahk
  Makefile
```

---

# AutoHotKey Makefile

```makefile
OS := $(shell uname)

install:
ifeq ($(OS),Linux)
        sudo apt install autohotkey || sudo dnf install autohotkey
endif
ifeq ($(OS),Darwin)
        brew install --cask autohotkey
endif
ifeq ($(OS),Windows_NT)
        choco install autohotkey
endif

run:
        autohotkey demo.ahk || AutoHotkey.exe demo.ahk

clean:
        rm -f *.log
```

---

# Demonstration Steps

Instructor demonstration:

1. Open text editor
2. Run AutoHotKey script
3. Press CTRL+J
4. Observe automatic typing

Explain: Software injected keyboard events.

---

# Hardware Input Simulation

USB devices can impersonate keyboards.

Operating system cannot distinguish:

- Real keyboard
- Fake keyboard

---

# USB Injection Architecture

\begin{tikzpicture}[
node distance=4cm,
every node/.style={draw, rectangle, minimum width=3.5cm, minimum height=1cm}
]

\node (device) {Malicious USB Device};
\node (os) [right of=device] {Operating System};
\node (app) [right of=os] {Application};

\draw[->] (device) -- (os);
\draw[->] (os) -- (app);

\end{tikzpicture}

---

# Demonstration 2: USB Keystroke Injection

Arduino Leonardo example:

```c
#include <Keyboard.h>

void setup()
{
    Keyboard.begin();

    delay(2000);

    Keyboard.print("echo Device compromised");

    Keyboard.press(KEY_RETURN);
    Keyboard.releaseAll();

    Keyboard.end();
}

void loop()
{
}
```

This executes automatically when plugged in.

---

# USB Demo Project Structure

```
usb-injection-demo/
  attack.c
  Makefile
```

---

# USB Demo Makefile

```makefile
OS := $(shell uname)

install:
ifeq ($(OS),Linux)
        sudo apt install arduino-cli
endif
ifeq ($(OS),Darwin)
        brew install arduino-cli
endif
ifeq ($(OS),Windows_NT)
        choco install arduino-cli
endif

compile:
        arduino-cli compile --fqbn arduino:avr:leonardo .

upload:
        arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:leonardo .

clean:
        rm -rf build
```

---

# Why This Attack Works

USB protocol has no authentication.

Operating system trusts all keyboards.

This is a fundamental security limitation.

---

# Demonstration 3: Selenium Automation

Selenium automates web browsers.

Capabilities:

- Typing text
- Clicking buttons
- Navigating pages

---

# Selenium Architecture

\begin{tikzpicture}[
node distance=4cm,
every node/.style={draw, rectangle, minimum width=3cm, minimum height=1cm}
]

\node (script) {Python Script};
\node (driver) [right of=script] {Browser Driver};
\node (browser) [right of=driver] {Browser};

\draw[->] (script) -- (driver);
\draw[->] (driver) -- (browser);

\end{tikzpicture}

---

# Selenium Example Script

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

driver.get("https://example.com")

time.sleep(2)

body = driver.find_element(By.TAG_NAME, "body")

body.send_keys("Hello from Selenium automation!")

time.sleep(5)

driver.quit()
```

---

# Selenium Demo Project Structure

```
selenium-demo/
  demo.py
  Makefile
```

---

# Selenium Makefile

```makefile
OS := $(shell uname)

install:
ifeq ($(OS),Linux)
        sudo apt install python3 python3-pip firefox-geckodriver
endif
ifeq ($(OS),Darwin)
        brew install python geckodriver firefox
endif
ifeq ($(OS),Windows_NT)
        pip install selenium webdriver-manager
endif

pip-install:
        pip install selenium

run:
        python3 demo.py

clean:
        rm -rf __pycache__
```

---

# Legitimate Uses

Input simulation enables:

- Automated testing
- Accessibility tools
- Workflow automation
- Repetitive task automation

Widely used in industry.

---

# Malicious Uses

Input simulation can enable:

- Malware installation
- Credential theft
- Unauthorized commands
- Privilege escalation

Example tools:

- USB Rubber Ducky
- BadUSB

---

# Security Defenses

Software defenses:

- Endpoint protection
- Behavior monitoring

Hardware defenses:

- USB device control
- Physical security

Policy defenses:

- User education
- Device restrictions

---

# Ethical Considerations

Automation tools are powerful.

Use responsibly.

Always obtain authorization.

Never perform unauthorized attacks.

---

# Key Takeaways

Human input devices generate events.

Operating systems abstract input events.

Software and hardware can simulate input.

Simulation enables automation and attacks.

Security awareness is essential.

---

# End of Lecture

Questions?
