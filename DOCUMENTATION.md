# 🌙 Whisper Programming Language - Complete Documentation

**Official Website:** [https://whisper.ibrahimmustafaopu.com](https://whisper.ibrahimmustafaopu.com)

---

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Getting Started](#getting-started)
4. [Variables](#variables)
5. [Output](#output)
6. [Input](#input)
7. [Comments](#comments)
8. [Conditionals](#conditionals)
9. [Loops](#loops)
10. [Functions](#functions)
11. [Lists & Arrays](#lists--arrays)
12. [Story Objects](#story-objects)
13. [Math Operations](#math-operations)
14. [String Operations](#string-operations)
15. [File Operations](#file-operations)
16. [Error Handling](#error-handling)
17. [Complete Examples](#complete-examples)

---

## Introduction

Whisper is a truly unique programming language with conversational, natural English syntax. It's designed to be:
- **Easy to learn** - Read like plain English
- **Conversational** - Write code like you're talking
- **Fun** - Story-like programming with objects and actions
- **Powerful** - All essential programming features

### File Extensions
Both extensions are supported. Use whichever you prefer:
- `.wsp` - Recommended (shorter)
- `.whisper` - More descriptive

---

## Installation

### Install via pip
```bash
pip install whisper-lang
```

### Verify installation
```bash
whisper --help
```

### Run a Whisper program
```bash
whisper myprogram.whisper
```

---

## VS Code Syntax Highlighting

### Install from VS Code Marketplace (Recommended)

1. Open VS Code
2. Go to Extensions (`Ctrl+Shift+X` or `Cmd+Shift+X` on Mac)
3. Search for "**Whisper Language Support**"
4. Click **Install**
5. Restart VS Code (if needed)
6. Open any `.wsp` or `.whisper` file to see syntax highlighting!

### Install from Command Line
```bash
code --install-extension ibrahimmustafaopu.whisper-lang-support
```

### Manual Installation (Alternative)

If the extension isn't published yet, or you want to install locally:

1. Download the extension from the [GitHub repository](https://github.com/ibrahim787898m/whisper-lang)
2. Copy the `.vscode/extensions/whisper/` folder to:
   - **Windows**: `%USERPROFILE%\.vscode\extensions\whisper-lang-support\`
   - **macOS/Linux**: `~/.vscode/extensions/whisper-lang-support\`
3. Restart VS Code
4. Syntax highlighting will activate for `.wsp` and `.whisper` files

---

## Getting Started

### Your First Program

Create a file `hello.wsp` (or `hello.whisper`):

```whisper
# My first Whisper program
whisper "Hello, World!"
tell me "Welcome to Whisper!"
```

Run it:
```bash
whisper hello.whisper
```

---

## Variables

### Declaring Variables

**Method 1: `remember that`** (Conversational)
```whisper
remember that age is 25
remember that name is "Alice"
remember that pi is 3.14
```

**Method 2: `let ... be`** (Traditional)
```whisper
let score be 100
let is_ready be 1
let temperature be 98.6
```

**Method 3: `set ... to`** (Alternative)
```whisper
set count to 0
set message to "Hello"
```

**Method 4: `so`** (Conversational shorthand)
```whisper
so x is 10
so y is 20
```

**Method 5: Conversational prefix**
```whisper
hey whisper, remember that color is "blue"
whisper, so size is "large"
```

### Deleting Variables

```whisper
forget about old_variable
```

### Variable Naming
- Use letters, numbers, and underscores
- Start with a letter or underscore
- Case-sensitive: `Name` and `name` are different

**Examples:**
```whisper
remember that player_score is 100
let user_name be "John"
so total_amount is 500
```

---

## Output

### Display Text or Values

**Method 1: `whisper`**
```whisper
whisper "Hello, World!"
whisper "Score: " + score
```

**Method 2: `show`**
```whisper
show x
show "Value: " + y
```

**Method 3: `tell me`**
```whisper
tell me "The answer is 42"
tell me result
```

**Method 4: `just say`** or **`just tell`**
```whisper
just say "Simple message"
just tell "Another way"
```

**Method 5: `announce`** (No newline)
```whisper
announce "Loading"
announce "."
announce "."
whisper "Done!"
# Output: Loading..Done!
```

### Combining Text and Variables

```whisper
let name be "Alice"
let age be 25

whisper "Name: " + name
show "Age: " + age
tell me name + " is " + age + " years old"
```

---

## Input

### Getting User Input

**Syntax:** `ask "prompt" into variable_name`

```whisper
ask "What is your name?" into name
ask "How old are you?" into age
ask "Enter a number:" into num

whisper "Hello, " + name + "!"
show "You are " + age + " years old"
```

**Auto-conversion:**
- Integer if input is whole number: `42` → `42`
- Float if input has decimal: `3.14` → `3.14`
- String otherwise: `hello` → `"hello"`

---

## Comments

Use `#` for single-line comments:

```whisper
# This is a comment
let x be 10  # Inline comment

# Multi-line comments:
# Line 1
# Line 2
# Line 3
```

---

## Conditionals

### When/Otherwise (if/else)

**Basic When:**
```whisper
when x greater than 5:
    show "x is big"
```

**When with Otherwise:**
```whisper
when age greater than 18:
    whisper "Adult"
otherwise:
    whisper "Minor"
```

**Multiple Conditions (or when):**
```whisper
when score greater than 90:
    show "Grade: A"
or when score greater than 80:
    show "Grade: B"
or when score greater than 70:
    show "Grade: C"
otherwise:
    show "Grade: F"
```

### Question-Based Conditions

**Syntax:** `is condition?` followed by `yes:` and `no:`

```whisper
is age greater than 18?
    yes:
        tell me "You can vote"
    no:
        tell me "Too young"

is x equals 10?
    yes:
        show "Correct!"
    no:
        show "Wrong!"
```

**Only yes branch:**
```whisper
is ready equals 1?
    yes:
        whisper "Let's go!"
```

### Comparison Operators

**Natural Language:**
- `greater than` → `>`
- `less than` → `<`
- `bigger than` → `>`
- `smaller than` → `<`
- `is` or `equals` → `==`
- `not` → `!=`

**Symbolic (also work):**
- `>` greater than
- `<` less than
- `>=` greater than or equal
- `<=` less than or equal
- `==` equal
- `!=` not equal

**Examples:**
```whisper
when x greater than 5:
    show "Big"

when age is 18:
    show "Exactly 18"

when score not 0:
    show "Not zero"
```

---

## Loops

### Do N Times

**Syntax:** `do N times:`

```whisper
do 5 times:
    whisper "Hello!"

let count be 10
do count times:
    show "Counting"
```

### Repeat N

**Syntax:** `repeat N:`

```whisper
repeat 3:
    tell me "Repeating"

let loops be 5
repeat loops:
    show "Loop"
```

### While Loop

**Syntax:** `while condition:`

```whisper
let count be 0
while count less than 5:
    show count
    increase count by 1

let running be 1
while running is 1:
    ask "Continue? (1/0)" into running
```

### For Each Loop

**Syntax:** `for each item in list:`

```whisper
make numbers with [1, 2, 3, 4, 5]
for each num in numbers:
    show num

make names with ["Alice", "Bob", "Charlie"]
for each name in names:
    whisper "Hello, " + name
```

### Loop Control

**Break (Exit loop):**
```whisper
while 1:
    ask "Enter 'quit' to exit:" into input
    when input is "quit":
        break
    show "You entered: " + input
```

**Break alternatives:**
- `break`
- `end while`
- `end loop`
- `end for`
- `stop`

**Continue (Skip to next iteration):**
```whisper
do 10 times:
    let num be randint(1, 10)
    when num is 5:
        continue  # Skip 5
    show num
```

**Continue alternatives:**
- `continue`
- `resume while`
- `resume loop`
- `resume for`
- `next`
- `skip`

---

## Functions

### Defining Functions

**Without parameters:**
```whisper
define greet:
    whisper "Hello, World!"
    tell me "How are you?"
```

**With parameters:**
```whisper
define greet with name:
    whisper "Hello, " + name + "!"

define add with a, b:
    let result be a + b
    give back result
```

### Calling Functions

**Without parameters:**
```whisper
call greet
```

**With parameters:**
```whisper
call greet with "Alice"

call add with 10, 20
show __last_result__  # Shows 30
```

### Returning Values

**Syntax:** `give back value`

```whisper
define multiply with x, y:
    let product be x * y
    give back product

call multiply with 5, 6
show __last_result__  # Shows 30

define is_adult with age:
    when age greater than 18:
        give back 1
    otherwise:
        give back 0
```

---

## Lists & Arrays

### Creating Lists

**Syntax:** `make list_name with [items]`

```whisper
make numbers with [1, 2, 3, 4, 5]
make names with ["Alice", "Bob", "Charlie"]
make mixed with [1, "hello", 3.14, 0]
make empty with []
```

### Adding Items

**Syntax:** `add item to list_name`

```whisper
make fruits with ["apple", "banana"]
add "orange" to fruits
add "grape" to fruits
show fruits  # ["apple", "banana", "orange", "grape"]
```

### Removing Items

**Syntax:** `remove item from list_name`

```whisper
make numbers with [1, 2, 3, 4, 5]
remove 3 from numbers
show numbers  # [1, 2, 4, 5]
```

### Looping Through Lists

```whisper
make colors with ["red", "green", "blue"]

for each color in colors:
    show color
```

### List Examples

```whisper
# Shopping list
make shopping with []

add "milk" to shopping
add "bread" to shopping
add "eggs" to shopping

whisper "Shopping List:"
for each item in shopping:
    show "- " + item

# Remove an item
remove "bread" from shopping
```

---

## Story Objects

Story objects let you create things with properties and perform actions on them.

### Creating Objects

**Syntax:** `there is a/an object_name with property value, property value`

```whisper
there is a hero with health 100, power 50
there is a dragon with health 200, damage 30
there is an item with name "sword", value 100
```

### Story Actions

**Losing values:** `the object loses amount property`
```whisper
the hero loses 20 health
the dragon loses 50 health
```

**Gaining values:** `the object gains amount property`
```whisper
the hero gains 10 power
the hero gains 25 health
```

### Accessing Object Properties

```whisper
there is a player with health 100, score 0

show player  # Shows all properties
the player loses 30 health
the player gains 10 score

show player  # Updated values
```

### Story Example

```whisper
# RPG Battle System
there is a knight with health 100, attack 25
there is a goblin with health 80, attack 15

whisper "=== Battle Start ==="

while knight health > 0 and goblin health > 0:
    # Knight attacks
    the goblin loses knight attack health
    show "Knight attacks! Goblin health: " + goblin health
    
    when goblin health less than 1:
        whisper "Goblin defeated!"
        break
    
    # Goblin attacks
    the knight loses goblin attack health
    show "Goblin attacks! Knight health: " + knight health
    
    when knight health less than 1:
        whisper "Knight defeated!"
        break
```

---

## Math Operations

### Basic Arithmetic

```whisper
let a be 10
let b be 3

let sum be a + b          # 13
let difference be a - b   # 7
let product be a * b      # 30
let quotient be a / b     # 3.333...
let remainder be a % b    # 1
let power be pow(a, b)    # 1000
```

### Math Functions

**Available functions:**
- `sqrt(x)` - Square root
- `pow(x, y)` - x to the power of y
- `abs(x)` - Absolute value
- `round(x)` - Round to nearest integer
- `floor(x)` - Round down
- `ceil(x)` - Round up
- `min(a, b, ...)` - Minimum value
- `max(a, b, ...)` - Maximum value

**Examples:**
```whisper
let x be sqrt(16)        # 4
let y be pow(2, 3)       # 8
let z be abs(-10)        # 10
let a be round(3.7)      # 4
let b be floor(3.9)      # 3
let c be ceil(3.1)       # 4

let smallest be min(5, 2, 8, 1)  # 1
let largest be max(5, 2, 8, 1)   # 8
```

### Random Numbers

**Random float (0.0 to 1.0):**
```whisper
let chance be random()
show chance
```

**Random integer:**
```whisper
let dice be randint(1, 6)      # Random 1-6
let lottery be randint(1, 100)  # Random 1-100
show dice
```

### Increment/Decrement

**Increase:**
```whisper
let score be 0
increase score by 10
increase score by 5
show score  # 15
```

**Decrease:**
```whisper
let lives be 3
decrease lives by 1
show lives  # 2
```

---

## String Operations

### Concatenation

```whisper
let first be "Hello"
let second be "World"
let message be first + " " + second
show message  # "Hello World"
```

### Uppercase/Lowercase

**Uppercase:**
```whisper
let text be "hello world"
uppercase text into upper
show upper  # "HELLO WORLD"
```

**Lowercase:**
```whisper
let text be "HELLO WORLD"
lowercase text into lower
show lower  # "hello world"
```

### String Examples

```whisper
ask "Enter your name:" into name
uppercase name into caps
lowercase name into lower

tell me "Uppercase: " + caps
tell me "Lowercase: " + lower

# Format messages
let score be 100
let message be "Your score is: " + score
show message
```

---

## File Operations

### Writing to Files

**Syntax:** `write content to "filename"`

```whisper
let message be "Hello, File!"
write message to "output.txt"

write "Line 1\nLine 2\nLine 3" to "multiline.txt"
```

### Reading from Files

**Syntax:** `read "filename" into variable`

```whisper
read "input.txt" into content
show content

read "data.txt" into data
whisper "File contents: " + data
```

### File Example

```whisper
# Create a log file
let timestamp be "2025-10-23"
let log be timestamp + ": Program started\n"

write log to "app.log"

# Read it back
read "app.log" into contents
show contents

# Append more (manual approach)
let new_entry be timestamp + ": Task completed\n"
let full_log be contents + new_entry
write full_log to "app.log"
```

---

## Error Handling

### Try-Catch (Attempt-Handle)

**Syntax:**
```whisper
attempt:
    # Code that might fail
handle:
    # Code to run if error occurs
    # Error message is in 'error' variable
```

**Example:**
```whisper
attempt:
    let result be 10 / 0
    show result
handle:
    whisper "Error occurred: " + error
    whisper "Cannot divide by zero!"

attempt:
    read "missing.txt" into data
handle:
    show "File not found: " + error
    let data be "Default content"
```

---

## Complete Examples

### Example 1: Calculator

```whisper
# Simple Calculator
whisper "=== Calculator ==="

ask "Enter first number:" into a
ask "Enter second number:" into b

let sum be a + b
let diff be a - b
let prod be a * b
let quot be a / b

show "Sum: " + sum
show "Difference: " + diff
show "Product: " + prod
show "Quotient: " + quot
```

### Example 2: Number Guessing Game

```whisper
# Number Guessing Game
whisper "=== Guess the Number ==="

let secret be randint(1, 100)
let attempts be 0
let max_tries be 10

while attempts less than max_tries:
    increase attempts by 1
    ask "Guess (1-100):" into guess
    
    is guess equals secret?
        yes:
            whisper "🎉 Correct! You win!"
            show "Attempts: " + attempts
            break
        no:
            when guess greater than secret:
                tell me "Too high!"
            otherwise:
                tell me "Too low!"
    
    let remaining be max_tries - attempts
    show "Tries left: " + remaining

when attempts equals max_tries:
    whisper "Game Over! Number was " + secret
```

### Example 3: Todo List Manager

```whisper
# Todo List Application
make tasks with []
let running be 1

whisper "=== Todo List Manager ==="

while running is 1:
    whisper "\n1. Add task"
    whisper "2. Show tasks"
    whisper "3. Remove task"
    whisper "4. Exit"
    
    ask "Choose option (1-4):" into choice
    
    when choice is 1:
        ask "Enter task:" into task
        add task to tasks
        tell me "✓ Task added!"
    
    or when choice is 2:
        is tasks equals []?
            yes:
                show "No tasks yet!"
            no:
                whisper "\nYour Tasks:"
                let num be 0
                for each task in tasks:
                    increase num by 1
                    show num + ". " + task
    
    or when choice is 3:
        ask "Task to remove:" into task
        remove task from tasks
        tell me "✓ Task removed!"
    
    or when choice is 4:
        set running to 0
        whisper "Goodbye!"
    
    otherwise:
        show "Invalid option!"
```

### Example 4: Story-Based Adventure

```whisper
# Text Adventure Game
hey whisper, remember that message is "This is a RPG Battle Game"
show message

there is a player with health 100, gold 0, items 0

whisper "=== The Quest Begins ==="
ask "What is your name, traveler?" into name

tell me "Welcome, " + name + "!"

there is a dragon with health 150, treasure 100

let in_battle be 1

while in_battle is 1:
    whisper "\n1. Attack dragon"
    whisper "2. Defend"
    whisper "3. Run away"
    
    ask "Your action:" into action
    
    when action is 1:
        let damage be randint(10, 50)
        the dragon loses damage health
        show "You dealt " + damage + " damage!"
        
        is dragon health less than 1?
            yes:
                whisper "🎉 Dragon defeated!"
                the player gains dragon treasure gold
                set in_battle to 0
            no:
                let counter be randint(5, 20)
                the player loses counter health
                show "Dragon hits you for " + counter + " damage!"
                
                is player health less than 1?
                    yes:
                        whisper "💀 You have been defeated!"
                        stop
    
    or when action is 2:
        tell me "You defend carefully"
        let damage be randint(1, 10)
        the player loses damage health
        show "You took " + damage + " damage"

        is player health less than 1?
            yes:
                whisper "💀 You have been defeated!"
                stop
    
    or when action is 3:
        whisper "You fled from battle!"
        stop
    
    show "Your health: " + player health
    show "Dragon health: " + dragon health

show "\nFinal Stats:"
show "Gold: " + player gold
```

### Example 5: Function-Based Program

```whisper
# Function Examples

# Function: Greet user
define greet with name:
    let greeting be "Hello, " + name + "!"
    whisper greeting
    give back greeting

# Function: Check if adult
define is_adult with age:
    when age greater than 18:
        give back 1
    otherwise:
        give back 0

# Function: Calculate circle area
define circle_area with radius:
    let pi be 3.14159
    let area be pi * radius * radius
    give back area

# Main program
ask "What is your name?" into user_name
call greet with user_name

ask "What is your age?" into user_age
call is_adult with user_age

is __last_result__ equals 1?
    yes:
        show "You are an adult"
    no:
        show "You are a minor"

ask "Enter circle radius:" into r
call circle_area with r
show "Circle area: " + __last_result__
```

---

## Quick Reference Card

### Variables
```whisper
remember that x is 10
let y be 20
set z to 30
so w is 40
forget about x
```

### Output
```whisper
whisper "text"
show value
tell me "message"
just say "simple"
announce "no newline"
```

### Input
```whisper
ask "prompt" into var
```

### Conditionals
```whisper
when condition:
    # code
or when condition:
    # code
otherwise:
    # code

is condition?
    yes:
        # code
    no:
        # code
```

### Loops
```whisper
do 5 times:
    # code

repeat 10:
    # code

while condition:
    # code

for each item in list:
    # code

break / end loop
continue / next
```

### Functions
```whisper
define func_name with param1, param2:
    # code
    give back result

call func_name with arg1, arg2
```

### Lists
```whisper
make list with [1, 2, 3]
add item to list
remove item from list
```

### Story Objects
```whisper
there is a hero with health 100, power 50
the hero loses 20 health
the hero gains 10 power
```

### Math
```whisper
let x be 10 + 5
let y be sqrt(16)
let z be randint(1, 100)
increase x by 5
decrease y by 2
```

### Files
```whisper
write "content" to "file.txt"
read "file.txt" into data
```

### Errors
```whisper
attempt:
    # risky code
handle:
    show error
```

---

## Tips & Best Practices

### 1. **Indentation**
Always use consistent indentation (4 spaces or 1 tab):
```whisper
when x greater than 5:
    show "Big"  # ← Indented
    show "Yes"  # ← Same level
```

### 2. **Comments**
Add comments to explain complex logic:
```whisper
# Calculate player damage based on level and equipment
let base_damage be level * 5
let bonus be equipment_power * 2
let total be base_damage + bonus
```

### 3. **Variable Names**
Use descriptive names:
```whisper
# Good
let player_health be 100
let max_attempts be 5

# Avoid
let h be 100
let ma be 5
```

### 4. **Functions**
Break complex code into functions:
```whisper
define calculate_damage with attacker, defender:
    let damage be attacker power - defender defense
    when damage less than 0:
        set damage to 0
    give back damage
```

### 5. **Error Handling**
Use `attempt/handle` for file operations and risky code:
```whisper
attempt:
    read "config.txt" into config
handle:
    whisper "Using default config"
    let config be "default settings"
```

---

## Common Mistakes

### ❌ Wrong: Single-line question syntax
```whisper
is x greater than 5?
    yes: show "Big"  # Won't work!
```

### ✅ Correct: Multi-line
```whisper
is x greater than 5?
    yes:
        show "Big"  # Works!
```

### ❌ Wrong: Missing indentation
```whisper
when x is 10:
show "Ten"  # Error!
```

### ✅ Correct: Proper indentation
```whisper
when x is 10:
    show "Ten"  # Correct!
```

### ❌ Wrong: Missing colons
```whisper
do 5 times  # Missing ':'
    show "Hi"
```

### ✅ Correct: Include colons
```whisper
do 5 times:
    show "Hi"
```

---

## Conclusion

Whisper is designed to make programming accessible, fun, and natural. The conversational syntax helps beginners understand programming concepts while remaining powerful enough for real applications.

**Next Steps:**
- Try the examples above
- Create your own programs
- Experiment with combining features
- Share your creations!

**Happy Coding with Whisper! 🌙**

---

**Version:** 1.0.0  
**License:** MIT  
**Author:** Ibrahim Mustafa Opu  

## 🔗 Useful Links

- **Website**: https://whisper.ibrahimmustafaopu.com
- **GitHub**: https://github.com/ibrahim787898m/whisper-lang
- **Tutorial**: https://whisper.ibrahimmustafaopu.com/tutorial.html
- **Examples**: https://whisper.ibrahimmustafaopu.com/examples.html