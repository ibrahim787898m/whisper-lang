# Changelog

All notable changes to Whisper will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Dictionary/object support (planned)
- Date/time functions (planned)
- Advanced string methods (planned)
- JSON support (planned)

## [1.0.0] - 2025-10-26

### Added
- **Initial Release** of Whisper Programming Language
- Conversational syntax with natural English commands
  - `hey whisper, remember that x is 5`
  - `tell me`, `show`, `whisper`, `just say`
- Question-based conditionals
  - `is x greater than 5?` with `yes:` and `no:` branches
- Story-like programming
  - `there is a hero with health 100, power 50`
  - `the hero loses 20 health`
  - `the hero gains 10 power`
- Control flow
  - `when/or when/otherwise` conditionals
  - `while` loops with natural comparisons
  - `do N times` and `repeat N` loops
  - `for each item in list` loops
- Variables with multiple syntax options
  - `remember that`, `let ... be`, `set ... to`, `so ... is`
  - `forget about` to delete variables
  - `increase/decrease by` for increment/decrement
- Functions
  - `define function_name with param1, param2:`
  - `call function_name with arg1, arg2`
  - `give back value` for returns
- Lists and arrays
  - `make list_name with [items]`
  - `add item to list_name`
  - `remove item from list_name`
- User input: `ask "prompt" into variable`
- File operations
  - `write content to "filename"`
  - `read "filename" into variable`
- String operations
  - `uppercase text into variable`
  - `lowercase text into variable`
- Math functions
  - Built-in: `sqrt`, `pow`, `abs`, `round`, `floor`, `ceil`
  - Random: `random()`, `randint(min, max)`
- Error handling
  - `attempt:` / `handle:` blocks
- Natural language comparisons
  - `greater than`, `less than`, `bigger than`, `smaller than`
  - `is`, `equals`, `not`
- Loop control with alternatives
  - `break`, `end loop`, `end while`, `stop`
  - `continue`, `next`, `skip`, `resume loop`
- VS Code syntax highlighting extension
- Comprehensive documentation (100+ pages)
- 8 example programs demonstrating all features
- Complete test suite

### Features
- Natural, conversational syntax - multiple ways to express the same concept
- Story-based object system with property manipulation
- Dictionary/object property access with dot notation
- Beginner-friendly error messages with helpful suggestions
- Zero external dependencies - pure Python implementation
- Cross-platform support (Windows, macOS, Linux)
- File extension: `.wsp` or `.whisper` for Whisper programs

### Documentation
- Complete syntax reference with examples
- 25+ feature demonstrations
- Quick start guide for beginners
- Progressive learning path (5 lessons)
- Best practices and style guide
- Common mistakes and troubleshooting
- Quick reference card

[Unreleased]: https://github.com/ibrahim787898m/whisper-lang/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/ibrahim787898m/whisper-lang/releases/tag/v1.0.0

---

**Learn More:**
- Website: https://whisper.ibrahimmustafaopu.com
- GitHub: https://github.com/ibrahim787898m/whisper-lang
- Documentation: https://whisper.ibrahimmustafaopu.com/documentation.html