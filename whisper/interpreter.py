import sys
import re
import math
import random

__version__ = "1.0.0"

# ======== Whisper Language Interpreter (Truly Unique Edition) ========
# A revolutionary language with conversational, natural, and fun syntax

# Global storage
functions = {}
story_objects = {}

def evaluate(expr, variables):
    """Safely evaluate math or variable expressions."""
    safe_dict = {
        "sqrt": math.sqrt,
        "pow": math.pow,
        "abs": abs,
        "round": round,
        "floor": math.floor,
        "ceil": math.ceil,
        "random": random.random,
        "randint": random.randint,
        "min": min,
        "max": max,
        "sum": sum,
        "len": len,
        "str": str,
        "list": list,
    }

    # If expr is already a list or dict, just return it
    if isinstance(expr, (list, dict)):
        return expr
    
    expr_str = str(expr).strip()
    
    # Check if this is a list literal like [1, 2, 3] or ["a", "b"]
    # Just evaluate it directly without variable replacement
    if expr_str.startswith('[') and expr_str.endswith(']'):
        try:
            result = eval(expr_str, {"__builtins__": {}}, safe_dict)
            return result
        except:
            pass  # If it fails, continue with normal processing
    
    # Check if this is just a simple variable name - return it immediately
    if re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", expr_str):
        var_name = expr_str
        if var_name in variables:
            # Return the variable value directly without any processing
            return variables[var_name]
        elif var_name in safe_dict:
            # It's a function, continue to eval
            pass
        else:
            raise NameError(f"Variable '{var_name}' is not defined")
    
    # Handle array/list indexing: variable[index]
    array_index_match = re.match(r"^([a-zA-Z_][a-zA-Z0-9_]*)\[(.+)\]$", expr_str)
    if array_index_match:
        var_name = array_index_match.group(1)
        index_expr = array_index_match.group(2)
        
        if var_name in variables:
            # Get the array/list
            array = variables[var_name]
            # Evaluate the index expression
            index = evaluate(index_expr, variables)
            
            # Return the indexed value
            if isinstance(array, (list, tuple, str)):
                try:
                    return array[int(index)]
                except (IndexError, ValueError, TypeError) as e:
                    raise IndexError(f"Index out of range or invalid: {index}")
            elif isinstance(array, dict):
                return array.get(index)
        else:
            raise NameError(f"Variable '{var_name}' is not defined")
    
    # Handle simple dictionary property access: "hero health" (entire expression)
    for var_name in sorted(variables.keys(), key=len, reverse=True):
        if isinstance(variables[var_name], dict):
            for prop_name in variables[var_name]:
                pattern = r'^' + re.escape(var_name) + r'\s+' + re.escape(prop_name) + r'$'
                if re.match(pattern, expr_str):
                    return variables[var_name][prop_name]
        
    # Helper functions for string detection
    def get_string_regions(text):
        """Build a list of (start, end) tuples for string regions."""
        regions = []
        i = 0
        while i < len(text):
            if text[i] == '"':
                j = i + 1
                while j < len(text):
                    if text[j] == '\\' and j + 1 < len(text):
                        j += 2
                        continue
                    if text[j] == '"':
                        regions.append((i, j + 1))
                        i = j + 1
                        break
                    j += 1
                else:
                    i += 1
            elif text[i] == "'":
                j = i + 1
                while j < len(text):
                    if text[j] == '\\' and j + 1 < len(text):
                        j += 2
                        continue
                    if text[j] == "'":
                        regions.append((i, j + 1))
                        i = j + 1
                        break
                    j += 1
                else:
                    i += 1
            else:
                i += 1
        return regions
    
    def is_inside_string(pos, regions):
        """Check if position is inside a string literal."""
        for start, end in regions:
            if start < pos < end - 1:
                return True
        return False
    
    # Replace dictionary property access
    for var_name in sorted(variables.keys(), key=len, reverse=True):
        if isinstance(variables[var_name], dict):
            for prop_name in variables[var_name]:
                pattern = r'\b' + re.escape(var_name) + r'\s+' + re.escape(prop_name) + r'\b'
                
                while True:
                    string_regions = get_string_regions(expr_str)
                    match = re.search(pattern, expr_str)
                    if not match:
                        break
                    
                    if is_inside_string(match.start(), string_regions):
                        marker = f"__SKIP_{var_name}_{prop_name}__"
                        expr_str = expr_str[:match.start()] + marker + expr_str[match.end():]
                        continue
                    
                    prop_value = variables[var_name][prop_name]
                    if isinstance(prop_value, str):
                        replacement = f'"{prop_value}"'
                    else:
                        replacement = str(prop_value)
                    
                    expr_str = expr_str[:match.start()] + replacement + expr_str[match.end():]
    
    # Restore any skipped property accesses
    for var_name in variables:
        if isinstance(variables[var_name], dict):
            for prop_name in variables[var_name]:
                marker = f"__SKIP_{var_name}_{prop_name}__"
                expr_str = expr_str.replace(marker, f"{var_name} {prop_name}")
    
    # Handle regular variables (including dicts that aren't property accesses)
    for var_name in sorted(variables.keys(), key=len, reverse=True):
        # Skip if this is a dict and we're accessing its properties
        is_property_access = False
        if isinstance(variables[var_name], dict):
            for prop_name in variables[var_name]:
                if re.search(rf'\b{re.escape(var_name)}\s+{re.escape(prop_name)}\b', expr_str):
                    is_property_access = True
                    break
        
        if is_property_access:
            continue
            
        pattern = r'\b' + re.escape(var_name) + r'\b'
        
        while True:
            string_regions = get_string_regions(expr_str)
            match = re.search(pattern, expr_str)
            if not match:
                break
            
            if is_inside_string(match.start(), string_regions):
                marker = f"__SKIP_{var_name}__"
                expr_str = expr_str[:match.start()] + marker + expr_str[match.end():]
                continue
            
            var_value = variables[var_name]
            if isinstance(var_value, str):
                # Escape special characters in strings
                escaped_value = var_value.replace('\\', '\\\\').replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t').replace('"', '\\"')
                replacement = f'"{escaped_value}"'
            elif isinstance(var_value, dict):
                replacement = f'"{str(var_value)}"'
            elif isinstance(var_value, list):
                # Handle lists/arrays properly
                def format_list_item(item):
                    if isinstance(item, str):
                        return f'"{item}"'
                    else:
                        return str(item)
                formatted_items = [format_list_item(item) for item in var_value]
                replacement = '[' + ', '.join(formatted_items) + ']'
            else:
                replacement = str(var_value)
            
            expr_str = expr_str[:match.start()] + replacement + expr_str[match.end():]
    
    # Restore any skipped variables
    for var_name in variables:
        marker = f"__SKIP_{var_name}__"
        expr_str = expr_str.replace(marker, var_name)
    
    # Handle string concatenation - but ONLY when there's actual concatenation
    # Check if there are comparison operators - if so, skip concatenation logic
    has_comparison = bool(re.search(r'(==|!=|<=|>=|<|>|\band\b|\bor\b|\bnot\b|\bin\b)', expr_str))
    
    if not has_comparison and ('"' in expr_str or "'" in expr_str):
        parts = re.split(r'("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\')', expr_str)
        
        result = []
        i = 0
        while i < len(parts):
            if i % 2 == 1:
                # String literal
                if result and not result[-1].endswith(' + '):
                    result.append(' + ')
                result.append(parts[i])
                i += 1
            else:
                # Non-string segment
                segment = parts[i].strip()
                if not segment:
                    i += 1
                    continue
                
                # Remove leading/trailing + from segment
                segment = re.sub(r'^\+\s*', '', segment)
                segment = re.sub(r'\s*\+$', '', segment)
                segment = segment.strip()
                
                if not segment:
                    i += 1
                    continue
                
                # Collect consecutive non-string parts
                numeric_parts = [segment]
                j = i + 1
                
                while j < len(parts):
                    if j % 2 == 1:
                        break
                    next_seg = parts[j].strip()
                    next_seg = re.sub(r'^\+\s*', '', next_seg)
                    next_seg = re.sub(r'\s*\+$', '', next_seg)
                    next_seg = next_seg.strip()
                    if next_seg:
                        numeric_parts.append(next_seg)
                    j += 1
                
                if numeric_parts:
                    numeric_expr = ' + '.join(numeric_parts)
                    if result and not result[-1].endswith(' + '):
                        result.append(' + ')
                    result.append(f'str({numeric_expr})')
                
                i = j
        
        expr_str = ''.join(result)
        expr_str = expr_str.strip()
    
    # Check if this is a simple identifier that doesn't exist
    simple_id = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", expr_str.strip())
    if simple_id:
        var_name = expr_str.strip()
        if var_name not in variables and var_name not in safe_dict:
            raise NameError(f"Variable '{var_name}' is not defined")
    
    try:
        result = eval(expr_str, {"__builtins__": {}}, safe_dict)
        return result
    except NameError as e:
        match = re.search(r"name '(\w+)' is not defined", str(e))
        if match:
            var_name = match.group(1)
            raise NameError(f"Variable '{var_name}' is not defined")
        raise NameError(f"Variable '{expr}' is not defined")
    except ZeroDivisionError:
        raise
    except SyntaxError:
        raise
    except Exception as e:
        if isinstance(expr_str, str):
            if (expr_str.startswith('"') and expr_str.endswith('"')) or \
               (expr_str.startswith("'") and expr_str.endswith("'")):
                return expr_str[1:-1]
        raise

def indent_level(line):
    """Return the indentation level of a line."""
    return len(line) - len(line.lstrip('\t '))

def collect_block(lines, start_index, base_indent):
    """Collect consecutive lines that belong to a block."""
    block = []
    i = start_index
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        ni = indent_level(line)
        if ni <= base_indent:
            break
        block.append(line)
        i += 1
    return block, i

def parse_when_group(lines, start_index):
    """Parse when/or when/otherwise group."""
    branches = []
    i = start_index
    base_indent = indent_level(lines[start_index])

    def parse_branch(idx):
        header_line = lines[idx]
        header_indent = indent_level(header_line)
        stripped = header_line.lstrip()
        
        if stripped.startswith("when "):
            rest = stripped[5:].strip()
        elif stripped.startswith("or when "):
            rest = stripped[8:].strip()
        elif stripped.startswith("otherwise"):
            rest = ""
        else:
            raise RuntimeError(f"Expected when/or when/otherwise")
        
        if rest.endswith(":"):
            rest = rest[:-1].strip()
        
        condition = None if not rest else rest
        block, next_idx = collect_block(lines, idx + 1, header_indent)
        
        return condition, block, next_idx
    
    cond, block, i = parse_branch(i)
    branches.append((cond, block))
    
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        
        current_indent = indent_level(line)
        if current_indent != base_indent:
            break
        
        stripped = line.lstrip()
        
        if stripped.startswith("or when ") and stripped.rstrip().endswith(":"):
            cond, block, i = parse_branch(i)
            branches.append((cond, block))
        elif stripped.startswith("otherwise") and stripped.rstrip().endswith(":"):
            cond, block, i = parse_branch(i)
            branches.append((cond, block))
            break
        else:
            break
    
    return branches, i

def parse_question_group(lines, start_index):
    """Parse is/are question format with yes/no branches."""
    branches = []
    i = start_index
    base_indent = indent_level(lines[start_index])
    
    # Extract question (condition)
    question_line = lines[i].lstrip()
    condition = question_line.strip().rstrip("?").strip()
    
    # Remove "is" or "are" from beginning if present
    if condition.startswith("is "):
        condition = condition[3:].strip()
    elif condition.startswith("are "):
        condition = condition[4:].strip()
    
    i += 1
    
    # Look for yes: and no: branches
    yes_block = []
    no_block = []
    
    while i < len(lines):
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        
        current_indent = indent_level(line)
        if current_indent <= base_indent:
            break
        
        stripped = line.lstrip()
        
        if stripped.startswith("yes:"):
            # Collect yes block
            yes_block, i = collect_block(lines, i + 1, current_indent)
        elif stripped.startswith("no:"):
            # Collect no block
            no_block, i = collect_block(lines, i + 1, current_indent)
        else:
            i += 1
    
    # Create branches: yes = condition true, no = condition false
    branches.append((condition, yes_block))
    if no_block:
        branches.append((None, no_block))  # None means else/no
    
    return branches, i

def parse_function_definition(lines, start_index):
    """Parse function definition."""
    header_line = lines[start_index]
    stripped = header_line.lstrip()
    header_indent = indent_level(header_line)
    
    if " with " in stripped:
        parts = stripped[7:].split(" with ", 1)
        func_name = parts[0].strip()
        params_str = parts[1].strip().rstrip(":")
        params = [p.strip() for p in params_str.split(",")]
    else:
        func_name = stripped[7:].strip().rstrip(":")
        params = []
    
    block, next_idx = collect_block(lines, start_index + 1, header_indent)
    
    return func_name, params, block, next_idx

def call_function(func_name, args, variables):
    """Call a user-defined function."""
    if func_name not in functions:
        raise RuntimeError(f"Function '{func_name}' not defined")
    
    params, block = functions[func_name]
    
    func_vars = variables.copy()
    for i, param in enumerate(params):
        if i < len(args):
            func_vars[param] = args[i]
    
    result = None
    func_vars['__return__'] = None
    run_lines(block, func_vars)
    
    return func_vars.get('__return__')

def run_lines(lines, variables):
    """Execute Whisper code lines."""
    i = 0
    length = len(lines)
    
    while i < length:
        raw = lines[i]
        line = raw.rstrip("\n")
        stripped = line.lstrip()
    
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        
        # Remove inline comments (but not # inside strings)
        if '#' in stripped:
            in_string = False
            quote_char = None
            for idx, char in enumerate(stripped):
                if char in ('"', "'") and (idx == 0 or stripped[idx-1] != '\\'):
                    if not in_string:
                        in_string = True
                        quote_char = char
                    elif char == quote_char:
                        in_string = False
                elif char == '#' and not in_string:
                    stripped = stripped[:idx].rstrip()
                    break
        
        # Break and Continue
        if stripped in ("break", "end while", "end loop", "end for", "stop"):
            raise StopIteration("break")
        
        if stripped in ("continue", "resume while", "resume loop", "resume for", "next", "skip"):
            raise StopIteration("continue")
        
        indent = indent_level(line)

        # Conversational: hey whisper, remember that x is 5
        if stripped.startswith("hey whisper,") or stripped.startswith("whisper,"):
            rest = stripped.split(",", 1)[1].strip()
            # Check if this is just a comment/statement, not a command
            if not any(rest.startswith(cmd) for cmd in ["remember that", "let ", "set ", "so ", "whisper ", "show ", "tell me", "ask ", "when ", "if ", "while ", "do ", "repeat ", "for each", "call ", "define ", "make ", "add ", "remove ", "write ", "read ", "uppercase ", "lowercase ", "there is", "the ", "is ", "are ", "forget about"]):
                # It's just a conversational comment, skip it
                i += 1
                continue
            # Process the rest as a normal command
            stripped = rest

        # Remember (variable assignment): remember that x is 5
        if stripped.startswith("remember that "):
            rest = stripped[14:].strip()
            if " is " in rest:
                parts = rest.split(" is ", 1)
                name = parts[0].strip()
                value = parts[1].strip()
                variables[name] = evaluate(value, variables)
                i += 1
                continue

        # Forget (delete variable): forget about x
        if stripped.startswith("forget about "):
            var_name = stripped[13:].strip()
            if var_name in variables:
                del variables[var_name]
            i += 1
            continue

        # Story objects: there is a hero with health 100
        if stripped.startswith("there is a ") or stripped.startswith("there is an "):
            rest = stripped[11:].strip() if stripped.startswith("there is a ") else stripped[12:].strip()
            if " with " in rest:
                parts = rest.split(" with ", 1)
                obj_name = parts[0].strip()
                # Parse properties
                props_str = parts[1].strip()
                props = {}
                for prop in props_str.split(","):
                    if " " in prop:
                        prop_parts = prop.strip().split(" ", 1)
                        prop_name = prop_parts[0].strip()
                        prop_value = prop_parts[1].strip() if len(prop_parts) > 1 else ""
                        props[prop_name] = evaluate(prop_value, variables)
                story_objects[obj_name] = props
                variables[obj_name] = props
            i += 1
            continue

        # Story action: the hero loses 20 health
        if stripped.startswith("the ") and " loses " in stripped:
            parts = stripped[4:].split(" loses ", 1)
            obj_name = parts[0].strip()
            rest = parts[1].strip()
            # Parse: "20 health"
            amount_prop = rest.rsplit(" ", 1)
            amount = evaluate(amount_prop[0].strip(), variables)
            prop = amount_prop[1].strip() if len(amount_prop) > 1 else "value"
            
            if obj_name in story_objects and prop in story_objects[obj_name]:
                story_objects[obj_name][prop] -= amount
                variables[obj_name] = story_objects[obj_name]
            i += 1
            continue

        # Story action: the hero gains 10 health OR the hero gains dragon treasure gold
        if stripped.startswith("the ") and " gains " in stripped:
            parts = stripped[4:].split(" gains ", 1)
            obj_name = parts[0].strip()
            rest = parts[1].strip()
            
            # Check if it's "object property property" format
            rest_parts = rest.split(" ")
            if len(rest_parts) == 3:
                # Format: "dragon treasure gold" -> gain dragon's treasure and add to gold
                source_obj = rest_parts[0]
                source_prop = rest_parts[1]
                target_prop = rest_parts[2]
                if source_obj in story_objects and source_prop in story_objects[source_obj]:
                    amount = story_objects[source_obj][source_prop]
                    if obj_name in story_objects and target_prop in story_objects[obj_name]:
                        story_objects[obj_name][target_prop] += amount
                        variables[obj_name] = story_objects[obj_name]
            else:
                # Format: "10 health" -> regular gains
                amount_prop = rest.split(" ", 1)
                amount = evaluate(amount_prop[0].strip(), variables)
                prop = amount_prop[1].strip() if len(amount_prop) > 1 else "value"
                
                if obj_name in story_objects and prop in story_objects[obj_name]:
                    story_objects[obj_name][prop] += amount
                    variables[obj_name] = story_objects[obj_name]
            i += 1
            continue

        # Question-based condition: is x greater than 5?
        if (stripped.startswith("is ") or stripped.startswith("are ")) and stripped.endswith("?"):
            branches, nxt = parse_question_group(lines, i)
            
            # branches[0] is the yes branch (condition, block)
            # branches[1] is the no branch (None, block) if it exists
            
            if len(branches) > 0:
                cond, yes_block = branches[0]
                no_block = branches[1][1] if len(branches) > 1 else []
                
                try:
                    # Process condition
                    cond = cond.replace(" is ", " == ")
                    cond = cond.replace(" equals ", " == ")
                    cond = cond.replace(" greater than ", " > ")
                    cond = cond.replace(" less than ", " < ")
                    cond = cond.replace(" bigger than ", " > ")
                    cond = cond.replace(" smaller than ", " < ")
                    cond = cond.replace(" not ", " != ")
                    
                    res = evaluate(cond, variables)
                    
                    if res:
                        # Execute yes branch
                        run_lines(yes_block, variables)
                    else:
                        # Execute no branch if it exists
                        if no_block:
                            run_lines(no_block, variables)
                            
                except StopIteration:
                    raise
                except Exception as e:
                    print(f"Error: {e}")
            
            i = nxt
            continue

        # Function definition
        if stripped.startswith("define ") and stripped.endswith(":"):
            func_name, params, block, nxt = parse_function_definition(lines, i)
            functions[func_name] = (params, block)
            i = nxt
            continue
        
        # Function call
        if stripped.startswith("call "):
            rest = stripped[5:].strip()
            if " with " in rest:
                parts = rest.split(" with ", 1)
                func_name = parts[0].strip()
                args_str = parts[1].strip()
                args = [evaluate(arg.strip(), variables) for arg in args_str.split(",")]
            else:
                func_name = rest
                args = []
            
            result = call_function(func_name, args, variables)
            if result is not None:
                variables['__last_result__'] = result
            i += 1
            continue
        
        # Return statement
        if stripped.startswith("give back "):
            value_expr = stripped[10:].strip()
            variables['__return__'] = evaluate(value_expr, variables)
            return

        # Try-catch
        if stripped.startswith("attempt:"):
            attempt_block, next_i = collect_block(lines, i + 1, indent)
            handle_block = []
            if next_i < length:
                next_line = lines[next_i].lstrip()
                if next_line.startswith("handle:"):
                    handle_block, next_i = collect_block(lines, next_i + 1, indent)
            
            try:
                run_lines(attempt_block, variables)
            except StopIteration:
                raise
            except Exception as e:
                if handle_block:
                    variables['error'] = str(e)
                    run_lines(handle_block, variables)
            
            i = next_i
            continue

        # Variable assignment: let x be 5
        if stripped.startswith("let "):
            parts = stripped[4:].split(" be ", 1)
            if len(parts) == 2:
                name = parts[0].strip()
                value = parts[1].strip()
                variables[name] = evaluate(value, variables)
                i += 1
                continue
        
        # Conversational: so x is 5
        if stripped.startswith("so "):
            rest = stripped[3:].strip()
            if " is " in rest:
                parts = rest.split(" is ", 1)
                name = parts[0].strip()
                value = parts[1].strip()
                variables[name] = evaluate(value, variables)
                i += 1
                continue
        
        # Alternative assignment: set x to 5
        if stripped.startswith("set "):
            parts = stripped[4:].split(" to ", 1)
            if len(parts) == 2:
                name = parts[0].strip()
                value = parts[1].strip()
                variables[name] = evaluate(value, variables)
                i += 1
                continue
        
        # Increment
        if stripped.startswith("increase "):
            parts = stripped[9:].split(" by ", 1)
            if len(parts) == 2:
                name = parts[0].strip()
                value = parts[1].strip()
                if name in variables:
                    variables[name] = variables[name] + evaluate(value, variables)
                else:
                    variables[name] = evaluate(value, variables)
                i += 1
                continue
        
        # Decrement
        if stripped.startswith("decrease "):
            parts = stripped[9:].split(" by ", 1)
            if len(parts) == 2:
                name = parts[0].strip()
                value = parts[1].strip()
                if name in variables:
                    variables[name] = variables[name] - evaluate(value, variables)
                else:
                    variables[name] = -evaluate(value, variables)
                i += 1
                continue

        # User input
        if stripped.startswith("ask "):
            rest = stripped[4:].strip()
            if " into " in rest:
                parts = rest.split(" into ", 1)
                prompt = parts[0].strip().strip('"').strip("'")
                var_name = parts[1].strip()
                user_input = input(prompt + " ")
                try:
                    if '.' in user_input:
                        variables[var_name] = float(user_input)
                    else:
                        variables[var_name] = int(user_input)
                except ValueError:
                    variables[var_name] = user_input
                i += 1
                continue

        # Output: whisper "text", show x, tell me x, just say x
        if stripped.startswith("whisper "):
            expr = stripped[8:].strip()
            try:
                result = evaluate(expr, variables)
                # Format dictionaries nicely
                if isinstance(result, dict):
                    result = str(result)
                print(result)
            except NameError as e:
                print(f"Error: {e}")
            i += 1
            continue
        
        if stripped.startswith("show "):
            expr = stripped[5:].strip()
            try:
                result = evaluate(expr, variables)
                # Format dictionaries nicely, but keep lists as-is
                if isinstance(result, dict):
                    result = str(result)
                print(result)
            except NameError as e:
                print(f"Error: {e}")
            i += 1
            continue
        
        if stripped.startswith("tell me "):
            expr = stripped[8:].strip()
            try:
                result = evaluate(expr, variables)
                # Format dictionaries nicely
                if isinstance(result, dict):
                    result = str(result)
                print(result)
            except NameError as e:
                print(f"Error: {e}")
            i += 1
            continue
        
        if stripped.startswith("just say ") or stripped.startswith("just tell "):
            expr = stripped[9:].strip() if "say" in stripped else stripped[10:].strip()
            try:
                result = evaluate(expr, variables)
                # Format dictionaries nicely
                if isinstance(result, dict):
                    result = str(result)
                print(result)
            except NameError as e:
                print(f"Error: {e}")
            i += 1
            continue
        
        # Announce
        if stripped.startswith("announce "):
            expr = stripped[9:].strip()
            try:
                result = evaluate(expr, variables)
                print(result, end='')
            except NameError as e:
                print(f"Error: {e}")
            i += 1
            continue

        # File operations
        if stripped.startswith("write ") and " to " in stripped:
            parts = stripped[6:].split(" to ", 1)
            if len(parts) == 2:
                content_expr = parts[0].strip()
                filename_expr = parts[1].strip()
                content = str(evaluate(content_expr, variables))
                filename = str(evaluate(filename_expr, variables))
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                i += 1
                continue
        
        if stripped.startswith("read ") and " into " in stripped:
            parts = stripped[5:].split(" into ", 1)
            if len(parts) == 2:
                filename_expr = parts[0].strip()
                var_name = parts[1].strip()
                filename = str(evaluate(filename_expr, variables))
                with open(filename, 'r', encoding='utf-8') as f:
                    variables[var_name] = f.read()
                i += 1
                continue

        # String operations
        if stripped.startswith("uppercase ") and " into " in stripped:
            parts = stripped[10:].split(" into ", 1)
            if len(parts) == 2:
                text_expr = parts[0].strip()
                var_name = parts[1].strip()
                text = str(evaluate(text_expr, variables))
                variables[var_name] = text.upper()
                i += 1
                continue
        
        if stripped.startswith("lowercase ") and " into " in stripped:
            parts = stripped[10:].split(" into ", 1)
            if len(parts) == 2:
                text_expr = parts[0].strip()
                var_name = parts[1].strip()
                text = str(evaluate(text_expr, variables))
                variables[var_name] = text.lower()
                i += 1
                continue

        # While loop
        if stripped.startswith("while ") and stripped.endswith(":"):
            condition = stripped[6:-1].strip()
            block, nxt = collect_block(lines, i + 1, indent)
            
            cond_check = condition.replace(" is ", " == ")
            cond_check = cond_check.replace(" equals ", " == ")
            cond_check = cond_check.replace(" greater than ", " > ")
            cond_check = cond_check.replace(" less than ", " < ")
            cond_check = cond_check.replace(" bigger than ", " > ")
            cond_check = cond_check.replace(" smaller than ", " < ")
            cond_check = cond_check.replace(" not ", " != ")
            
            max_iterations = 10000
            iterations = 0
            
            while iterations < max_iterations:
                try:
                    if not evaluate(cond_check, variables):
                        break
                    run_lines(block, variables)
                    iterations += 1
                except StopIteration as e:
                    if str(e) == "break":
                        break
                    elif str(e) == "continue":
                        continue
                except Exception as e:
                    print(f"Error in while loop: {e}")
                    break
            
            i = nxt
            continue

        # For-each loop
        if stripped.startswith("for each ") and " in " in stripped and stripped.endswith(":"):
            parts = stripped[9:-1].split(" in ", 1)
            if len(parts) == 2:
                var_name = parts[0].strip()
                list_expr = parts[1].strip()
                
                try:
                    items = evaluate(list_expr, variables)
                    if isinstance(items, str):
                        items = list(items)
                    elif not isinstance(items, (list, tuple, range)):
                        items = [items]
                except:
                    items = []
                
                block, nxt = collect_block(lines, i + 1, indent)
                
                for item in items:
                    variables[var_name] = item
                    try:
                        run_lines(block, variables)
                    except StopIteration as e:
                        if str(e) == "break":
                            break
                        elif str(e) == "continue":
                            continue
                
                i = nxt
                continue

        # Loops
        if stripped.startswith("do ") and " times:" in stripped:
            parts = stripped[3:].split(" times:", 1)
            count_expr = parts[0].strip()
            count = int(evaluate(count_expr, variables))
            block, nxt = collect_block(lines, i + 1, indent)
            for _ in range(count):
                try:
                    run_lines(block, variables)
                except StopIteration as e:
                    if str(e) == "break":
                        break
                    elif str(e) == "continue":
                        continue
            i = nxt
            continue
        
        if stripped.startswith("repeat ") and stripped.endswith(":"):
            count_expr = stripped[7:-1].strip()
            count = int(evaluate(count_expr, variables))
            block, nxt = collect_block(lines, i + 1, indent)
            for _ in range(count):
                try:
                    run_lines(block, variables)
                except StopIteration as e:
                    if str(e) == "break":
                        break
                    elif str(e) == "continue":
                        continue
            i = nxt
            continue
        
        # List operations
        if stripped.startswith("make ") and " with " in stripped:
            parts = stripped[5:].split(" with ", 1)
            if len(parts) == 2:
                list_name = parts[0].strip()
                list_expr = parts[1].strip()
                variables[list_name] = evaluate(list_expr, variables)
                i += 1
                continue
        
        if stripped.startswith("add ") and " to " in stripped:
            parts = stripped[4:].split(" to ", 1)
            if len(parts) == 2:
                item_expr = parts[0].strip()
                list_name = parts[1].strip()
                item = evaluate(item_expr, variables)
                if list_name in variables:
                    if isinstance(variables[list_name], list):
                        variables[list_name].append(item)
                    else:
                        variables[list_name] = [variables[list_name], item]
                else:
                    variables[list_name] = [item]
                i += 1
                continue
        
        if stripped.startswith("remove ") and " from " in stripped:
            parts = stripped[7:].split(" from ", 1)
            if len(parts) == 2:
                item_expr = parts[0].strip()
                list_name = parts[1].strip()
                item = evaluate(item_expr, variables)
                if list_name in variables and isinstance(variables[list_name], list):
                    try:
                        variables[list_name].remove(item)
                    except ValueError:
                        pass
                i += 1
                continue

        # Conditionals
        if stripped.startswith("when ") and stripped.endswith(":"):
            branches, nxt = parse_when_group(lines, i)
            executed_any = False
            
            for cond, block in branches:
                if cond is None:
                    if not executed_any:
                        run_lines(block, variables)
                    break
                else:
                    try:
                        cond = cond.replace(" is ", " == ")
                        cond = cond.replace(" equals ", " == ")
                        cond = cond.replace(" greater than ", " > ")
                        cond = cond.replace(" less than ", " < ")
                        cond = cond.replace(" bigger than ", " > ")
                        cond = cond.replace(" smaller than ", " < ")
                        cond = cond.replace(" not ", " != ")
                        
                        res = evaluate(cond, variables)
                        if res:
                            run_lines(block, variables)
                            executed_any = True
                            break
                    except StopIteration:
                        raise
                    except Exception as e:
                        print(f"Error evaluating condition '{cond}': {e}")
                        break
            
            i = nxt
            continue

        # Unknown command
        print(f"Unknown command: {stripped}")
        i += 1

def run(code):
    """Run Whisper code."""
    variables = {}
    lines = code.splitlines(keepends=True)
    run_lines(lines, variables)

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print(f"🌙 Whisper v{__version__} - A Truly Unique Programming Language\n")
        print("Usage: whisper <filename>")
        print("\nFile extensions: .wsp or .whisper")
        print("\nExample: whisper hello.wsp")
        print("\nFeatures:")
        print("  • Conversational syntax")
        print("  • Question-based conditions")
        print("  • Story-like programming")
        print("  • Natural English commands")
        print("\nLearn more: https://whisper.ibrahimmustafaopu.com")
        print("Documentation: https://whisper.ibrahimmustafaopu.com/documentation.html")
        return
    
    # Add --help flag
    if sys.argv[1] in ('--help', '-h', 'help'):
        print(f"🌙 Whisper v{__version__} - A Truly Unique Programming Language\n")
        print("Usage: whisper <filename>")
        print("       whisper [options]")
        print("\nOptions:")
        print("  --version, -v    Show version number")
        print("  --help, -h       Show this help message")
        print("\nFile extensions: .wsp or .whisper")
        print("\nExamples:")
        print("  whisper hello.wsp")
        print("  whisper myprogram.whisper")
        print("\nWebsite: https://whisper.ibrahimmustafaopu.com")
        print("Documentation: https://whisper.ibrahimmustafaopu.com/documentation.html")
        print("GitHub: https://github.com/ibrahim787898m/whisper-lang")
        return
    
    if sys.argv[1] in ('--version', '-v'):
        print(f"Whisper v{__version__}")
        return
    
    filename = sys.argv[1]

    try:
        with open(filename, "r", encoding="utf-8") as f:
            code = f.read()
        run(code)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()