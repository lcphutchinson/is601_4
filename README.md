## SU25 IS601-850 Module 3: Object-Oriented Design & Parameterized Testing
![Coverage Badge](https://github.com/lcphutchinson/is601_3/actions/workflows/ci.yml/badge.svg)

A module of Web Systems Development, by Keith Williams

<details>
<summary>
📦 Environment Setup (Verbose)
</summary>

> This setup guide is copied from the original module, [here](github.com/kaw393939/module3_is601)

---

### 🧩 1. Install Homebrew (Mac Only)

> Skip this step if you're on Windows.

Homebrew is a package manager for macOS.
You’ll use it to easily install Git, Python, Docker, etc.

**Install Homebrew:**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

**Verify Homebrew:**

```bash
brew --version
```

If you see a version number, you're good to go.

---

### 🧩 2. Install and Configure Git

#### Install Git

- **MacOS (using Homebrew)**

```bash
brew install git
```

- **Windows**

Download and install [Git for Windows](https://git-scm.com/download/win).
Accept the default options during installation.

**Verify Git:**

```bash
git --version
```

---

#### Configure Git Globals

Set your name and email so Git tracks your commits properly:

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

Confirm the settings:

```bash
git config --list
```

---

#### Generate SSH Keys and Connect to GitHub

> Only do this once per machine.

1. Generate a new SSH key:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
 
(Press Enter at all prompts.)

2. Start the SSH agent: 

 ```bash
eval "$(ssh-agent -s)"
```

3. Add the SSH private key to the agent:

```bash
ssh-add ~/.ssh/id_ed25519
```

4. Copy your SSH public key:

- **Mac/Linux:**

```bash
cat ~/.ssh/id_ed25519.pub | pbcopy
```

- **Windows (Git Bash):**

```bash
cat ~/.ssh/id_ed25519.pub | clip
```

5. Add the key to your GitHub account:
   - Go to [GitHub SSH Settings](https://github.com/settings/keys)
   - Click **New SSH Key**, paste the key, save.

6. Test the connection:

```bash
ssh -T git@github.com
```

You should see a success message.

---

### 🧩 3. Clone the Repository

Now you can safely clone the course project:

```bash
git clone <repository-url>
cd <repository-directory>
```

---

### 🛠️ 4. Install Python 3.10+

#### Install Python

- **MacOS (Homebrew)**

```bash
brew install python
```

- **Windows**

Download and install [Python for Windows](https://www.python.org/downloads/).
✅ Make sure you **check the box** `Add Python to PATH` during setup.

**Verify Python:**

```bash
python3 --version
```
or
```bash
python --version
```

---
</details>
<details>
<summary>
🛠️ Requirements & Installation
</summary>


Running this project will require:

- Bash or a similar Unix shell
- A Git installation configured for use with Github (see Verbose)
- Python version 3.13+, optionally with an installed venv module

--- 

### 📦 Quick Setup

- **Retrieve the Project**

```bash
git clone git@github.com:lcphutchinson/is601_3.git
cd is601_3.git
```

- **Generate a Virtual Environment (Optional)**

```bash
python3 -m venv venv
source venv/bin/activate
```

- **Install Project Requirements**

```bash
pip install -r requirements.txt
```
</details>

---

### 🚀 Operation

Launch the calculator with Python:

```bash
python3 main.py
```

Module 3's Calculator supports four operations

```bash
add \<x\> \<y\>: Adds two operands, x and y.
subtract \<x\> \<y\>: Subtracts an operand y from another operand x.
multiply \<x\> \<y\>: Multiplies two operands, x and y.
divide \<x\> \<y\>: Divides a non-zero operand y from another operand x.
```

After each valid command, a prefaced result value will be printed to the terminal, followed by another prompt:

```bash
$: add 2 3
Result: 5
$: 
```

If a command is not parsable or otherwise invalid, an error message will be shown, but the program will not terminate:

```bash
$: nonsense
Error: Invalid Command Syntax. Expected <command> <x> <y>
$:
```

To exit the program, type the command `exit`:

```bash
$: exit
Thank you for using Python REPL Calculator. Exiting...
you@yourPC:~/is601_3
```

