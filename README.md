# 🌙 Whisper Programming Language

A truly unique programming language with conversational, natural English syntax that makes coding feel like storytelling.

[![PyPI version](https://img.shields.io/pypi/v/whisper-lang)](https://pypi.org/project/whisper-lang/)
[![VS Code](https://img.shields.io/visual-studio-marketplace/v/ibrahimmustafaopu.whisper-lang-support?color=blue&label=VS%20Code&logo=visualstudiocode)](https://marketplace.visualstudio.com/items?itemName=ibrahimmustafaopu.whisper-lang-support)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![Downloads](https://pepy.tech/badge/whisper-lang)](https://pepy.tech/project/whisper-lang)

## 🌐 Website

**Official Website:** [https://whisper.ibrahimmustafaopu.com](https://whisper.ibrahimmustafaopu.com)

- 📚 [Documentation](https://whisper.ibrahimmustafaopu.com/documentation.html)
- 📖 [Tutorial](https://whisper.ibrahimmustafaopu.com/tutorial.html)
- 💻 [Examples](https://whisper.ibrahimmustafaopu.com/examples.html)
- 🤝 [Contribute](https://whisper.ibrahimmustafaopu.com/contribute.html)

## ✨ What Makes Whisper Unique?

- **File Extensions**: `.wsp` or `.whisper` - your choice!
- **Conversational Syntax**: Write code like you're having a conversation
- **Question-Based Logic**: Ask questions with yes/no answers
- **Story Objects**: Create characters and objects with properties
- **Natural Commands**: Multiple ways to express the same thing
- **Beginner-Friendly**: Read and write code in plain English
- **Fully Featured**: Functions, loops, lists, file I/O, and more

## 🚀 Quick Start

### Installation

```bash
pip install whisper-lang
```

### Hello World

Create `hello.wsp` (or `hello.whisper`):

```whisper
hey whisper, remember that name is "World"
tell me "Hello, " + name + "!"
```

Run it:

```bash
whisper hello.wsp
# Both .wsp and .whisper extensions are supported
```

## 🎯 Examples

### 1. Conversational Variables

```whisper
# Talk to Whisper naturally
hey whisper, remember that score is 0
whisper, so lives is 3

# Or use traditional syntax
let player be "Alice"
set level to 1
```

### 2. Question-Based Conditions

```whisper
is age greater than 18?
    yes:
        tell me "You can vote!"
    no:
        tell me "Too young to vote"
```

### 3. Story-Like Programming

```whisper
# Create objects with properties
there is a hero with health 100, power 50
there is a dragon with health 200, damage 30

# Perform actions
the hero loses 20 health
the dragon loses 30 health
the hero gains 10 power
```

### 4. Natural Loop Control

```whisper
do 10 times:
    let num be randint(1, 10)
    
    when num is 5:
        skip  # Skip 5
    
    when num is 9:
        end loop  # Exit loop
    
    show num
```

### 5. Functions & Logic

```whisper
define greet with name, age:
    whisper "Hello, " + name + "!"
    
    is age greater than 18?
        yes:
            tell me "Welcome, adult!"
        no:
            tell me "Welcome, young one!"
    
    give back "Greeting complete"

call greet with "Alice", 25
```

## 📚 Core Features

### Variables (Multiple Ways!)
```whisper
remember that x is 10        # Conversational
let y be 20                  # Traditional
set z to 30                  # Alternative
so w is 40                   # Shorthand
forget about old_var         # Delete
```

### Output (Choose Your Style!)
```whisper
whisper "Hello"              # Classic
show value                   # Simple
tell me "Message"            # Conversational
just say "Quick"             # Casual
announce "No newline"        # Inline
```

### Conditionals
```whisper
# When/Otherwise (if/elif/else)
when x greater than 10:
    show "Big"
or when x greater than 5:
    show "Medium"
otherwise:
    show "Small"

# Question format
is x equals 10?
    yes:
        show "Perfect!"
    no:
        show "Try again"
```

### Loops
```whisper
do 5 times:                  # Repeat N times
    show "Hello"

repeat 10:                   # Alternative syntax
    show "Counting"

while count less than 10:    # While loop
    increase count by 1

for each item in items:      # For-each loop
    show item
```

### Lists
```whisper
make fruits with ["apple", "banana", "orange"]
add "grape" to fruits
remove "banana" from fruits

for each fruit in fruits:
    show fruit
```

### Functions
```whisper
define calculate with a, b:
    let sum be a + b
    let product be a * b
    give back sum

call calculate with 10, 5
show __last_result__
```

### File Operations
```whisper
write "Hello, File!" to "output.txt"
read "input.txt" into content
show content
```

### Error Handling
```whisper
attempt:
    let result be 10 / 0
handle:
    whisper "Error: " + error
```

### Math & Random
```whisper
let x be sqrt(16)           # 4
let y be pow(2, 3)          # 8
let z be randint(1, 100)    # Random 1-100

increase score by 10
decrease lives by 1
```

### String Operations
```whisper
uppercase "hello" into upper    # HELLO
lowercase "WORLD" into lower    # world
```

## 🎮 Complete Example: Number Guessing Game

```whisper
# Number Guessing Game
whisper "=== Guess the Number ==="

let secret be randint(1, 100)
let attempts be 0

while attempts less than 10:
    increase attempts by 1
    ask "Guess (1-100):" into guess
    
    is guess equals secret?
        yes:
            whisper "🎉 Correct! You win!"
            show "Attempts: " + attempts
            end loop
        no:
            when guess greater than secret:
                tell me "Too high!"
            otherwise:
                tell me "Too low!"
    
    let remaining be 10 - attempts
    show "Tries left: " + remaining

whisper "Thanks for playing!"
```

## 📖 Syntax Comparison

| Feature | Python | Whisper |
|---------|--------|---------|
| Variable | `x = 10` | `remember that x is 10` or `let x be 10` |
| Print | `print("Hi")` | `whisper "Hi"` or `tell me "Hi"` |
| Input | `name = input("Name?")` | `ask "Name?" into name` |
| If/Else | `if x > 5:` | `when x greater than 5:` or `is x greater than 5?` |
| For Loop | `for i in items:` | `for each i in items:` |
| While | `while x < 10:` | `while x less than 10:` |
| Function | `def greet(name):` | `define greet with name:` |
| Return | `return value` | `give back value` |
| Break | `break` | `break` or `end loop` or `stop` |
| Continue | `continue` | `continue` or `next` or `skip` |

## 🎨 Why Choose Whisper?

### For Beginners
- **No cryptic symbols**: Read code like English
- **Multiple ways**: Choose syntax that feels natural to you
- **Clear errors**: Understand what went wrong
- **Gentle learning curve**: Start coding immediately

### For Educators
- **Teach concepts**: Focus on logic, not syntax
- **Engaging**: Story-based programming captures imagination
- **Versatile**: Suitable for all age groups
- **Creative**: Build games, stories, and apps

### For Fun Projects
- **Text adventures**: Built-in story object system
- **Quick scripts**: Natural syntax for rapid prototyping
- **Creative coding**: Express ideas conversationally
- **Experimentation**: Try ideas without syntax barriers

## 📦 Installation & Usage

### Requirements
- Python 3.7 or higher

### Install
```bash
pip install whisper-lang
```

### Run a Program
```bash
whisper myprogram.wsp
# Both .wsp and .whisper extensions are supported
```

### VS Code Extension

**Syntax highlighting available!**

Install from VS Code:
1. Open Extensions panel (`Ctrl+Shift+X`)
2. Search "Whisper Language Support"
3. Click Install

Or via command line:
```bash
code --install-extension ibrahimmustafaopu.whisper-lang-support
```

See [DOCUMENTATION.md](DOCUMENTATION.md) for manual installation instructions.

## 📚 Documentation

**Complete documentation available in [DOCUMENTATION.md](DOCUMENTATION.md)**

Includes:
- Full syntax reference
- All features explained
- Dozens of examples
- Best practices
- Common mistakes
- Quick reference card

## 🎓 Learning Path

### Lesson 1: Variables & Output
```whisper
remember that name is "Alice"
let age be 25
whisper "Name: " + name
show "Age: " + age
```

### Lesson 2: Input & Logic
```whisper
ask "Your age?" into age

is age greater than 18?
    yes:
        tell me "Adult"
    no:
        tell me "Minor"
```

### Lesson 3: Loops
```whisper
do 5 times:
    whisper "Hello!"

let count be 0
while count less than 5:
    show count
    increase count by 1
```

### Lesson 4: Functions
```whisper
define add with a, b:
    let sum be a + b
    give back sum

call add with 10, 20
show __last_result__
```

### Lesson 5: Story Objects
```whisper
there is a player with health 100, score 0
the player gains 10 score
the player loses 20 health
show player
```

## 🌟 Example Programs

### Todo List Manager
```whisper
make tasks with []
let running be 1

while running is 1:
    whisper "\n1. Add  2. Show  3. Remove  4. Exit"
    ask "Choice:" into choice
    
    when choice is 1:
        ask "Task:" into task
        add task to tasks
    or when choice is 2:
        for each task in tasks:
            show "- " + task
    or when choice is 3:
        ask "Remove:" into task
        remove task from tasks
    or when choice is 4:
        set running to 0
```

### RPG Battle
```whisper
there is a hero with health 100, attack 25
there is a monster with health 80, attack 15

while hero health > 0 and monster health > 0:
    the monster loses hero attack
    show "You attack! Monster: " + monster health
    
    when monster health less than 1:
        whisper "Victory!"
        break
    
    the hero loses monster attack
    show "Monster attacks! You: " + hero health
```

### Calculator
```whisper
ask "First number:" into a
ask "Second number:" into b

let sum be a + b
let diff be a - b
let product be a * b
let quotient be a / b

show "Sum: " + sum
show "Difference: " + diff
show "Product: " + product
show "Quotient: " + quotient
```

## 🔧 Advanced Features

### Math Functions
```whisper
let x be sqrt(16)        # Square root
let y be pow(2, 8)       # Power
let z be abs(-10)        # Absolute value
let a be round(3.7)      # Rounding
let b be randint(1, 100) # Random integer
```

### File Operations
```whisper
# Write
write "Log entry: Started" to "log.txt"

# Read
read "config.txt" into config
show config
```

### Error Handling
```whisper
attempt:
    read "missing.txt" into data
handle:
    whisper "File not found: " + error
    let data be "default"
```

### List Operations
```whisper
make numbers with [5, 2, 8, 1, 9]
add 3 to numbers
remove 8 from numbers

for each num in numbers:
    when num greater than 5:
        show num + " is big"
```

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Share your Whisper programs

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

## 🔗 Links

- **Website**: https://whisper.ibrahimmustafaopu.com
- **Documentation**: https://whisper.ibrahimmustafaopu.com/documentation.html
- **GitHub**: https://github.com/ibrahim787898m/whisper-lang
- **PyPI**: https://pypi.org/project/whisper-lang/
- **Issues**: https://github.com/ibrahim787898m/whisper-lang/issues

## 💬 Community

Share your Whisper programs! Tag them with `#WhisperLang`

## 🚦 Status

- ✅ Core language features complete
- ✅ Full documentation available
- ✅ VS Code syntax highlighting
- ✅ Error handling
- ✅ File I/O
- 🔄 Coming soon: More built-in functions
- 🔄 Coming soon: Package manager
- 🔄 Coming soon: Standard library

## 🎯 Roadmap

### Version 1.1 (Q2 2026) - Enhanced Features
- [ ] Dictionary/object support
- [ ] Date/time functions
- [ ] Advanced string methods
- [ ] JSON support
- [ ] HTTP requests
- [ ] Improved error messages
- [ ] More built-in functions
- [ ] Performance optimizations

### Version 1.5 (Q3 2026) - Developer Tools
- [ ] Interactive REPL mode
- [ ] Package manager
- [ ] Testing framework
- [ ] More IDE extensions (Sublime, Atom, etc.)
- [ ] Online code playground
- [ ] Enhanced debugging tools

### Version 2.0 (Q4 2026) - Advanced Capabilities
- [ ] Module system
- [ ] Classes/OOP
- [ ] Async operations
- [ ] GUI toolkit
- [ ] Web framework integration
- [ ] Database connectivity
- [ ] API support
- [ ] Multi-language support
- [ ] Community plugins system

## Folder Structure

```
whisper/
│
├── .gitignore
├── CHANGELOG.md
├── DOCUMENTATION.md
├── LICENSE
├── MANIFEST.in
├── README.md
├── requirements.txt
├── setup.py
│
├── whisper/
│   ├── __init__.py
│   └── interpreter.py
│
├── examples/
│   ├── hello_world.wsp
│   ├── calculator.wsp
│   ├── guessing_game.wsp
│   ├── todo_list.wsp
│   ├── story_adventure.wsp
│   └── rpg_battle.wsp
│
├── tests/
│   └── test_all.wsp
│
└── .vscode/
    └── extensions/
        └── whisper/
            ├── LICENSE
            ├── README.md
            ├── package.json
            ├── language-configuration.json
            │
            ├── syntaxes/
            │   └── whisper.tmLanguage.json
            │
            └── images/
                └── whisper-icon.png
```

## ❓ FAQ

**Q: Is Whisper suitable for production?**  
A: Whisper is great for learning, scripting, and fun projects. For production systems, consider Python, JavaScript, etc.

**Q: Can I use Whisper in my project?**  
A: Yes! Whisper is MIT licensed and free to use.

**Q: How do I get syntax highlighting?**  
A: See the VS Code extension setup in DOCUMENTATION.md

**Q: Can I contribute?**  
A: Absolutely! Pull requests are welcome.

**Q: Is there a standard library?**  
A: Currently building one. Basic functions included.

**Q: Can Whisper do [X]?**  
A: Check DOCUMENTATION.md for full feature list.

## 🙏 Acknowledgments

Thanks to all programming language pioneers who made coding more accessible!

## 📞 Contact

- **Author**: Ibrahim Mustafa Opu
- **Email**: ibrahimmustafa787898@gmail.com
- **GitHub**: github.com/ibrahim787898m
- **Website**: v2.ibrahimmustafaopu.com

---

**Made with 🌙 by Ibrahim Mustafa Opu**

*"Programming should feel like telling a story"*
