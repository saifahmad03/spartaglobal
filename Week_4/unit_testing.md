# Unit Testing Notes

## What is unit testing?

Testing the **smallest pieces of code** (a function or method) **in isolation** to check they behave as expected. Each test checks one behaviour.

**Good unit tests are:**
- **Fast**: run in milliseconds
- **Isolated**: don't depend on databases, files or networks (use mocks instead)
- **Repeatable**: same result every time
- **Self-checking**: pass or fail without manual inspection
- **Focused**: one behaviour per test

## Structure of a test: Arrange, Act, Assert

```python
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add_positive_numbers(self):
        # Arrange
        a, b = 2, 3
        # Act
        result = add(a, b)
        # Assert
        self.assertEqual(result, 5)

if __name__ == "__main__":
    unittest.main()
```

## Common tools in Python

| Tool | Notes |
|---|---|
| `unittest` | Built in, class-based |
| `pytest` | Popular, simpler syntax (plain `assert`) |
| `unittest.mock` | Replace real dependencies with fakes |

Common assertions: `assertEqual`, `assertTrue`, `assertRaises`, `assertIn`.

## What is TDD (Test-Driven Development)?

A development approach where you **write the test before the code**. It follows a short cycle called **Red → Green → Refactor**.

1. **Red**: write a small test for a feature that doesn't exist yet. It fails.
2. **Green**: write the *minimum* code needed to make the test pass.
3. **Refactor**: clean up the code while keeping all tests passing.
4. **Repeat** for the next small behaviour.

## TDD example

**Step 1: Red** (test first, fails because `square` doesn't exist)

```python
def test_square():
    assert square(4) == 16
```

**Step 2: Green** (simplest code that passes)

```python
def square(n):
    return n * n
```

**Step 3: Refactor** (tidy up if needed, then re-run tests)

Next, add another test (e.g. `square(-3) == 9`), and repeat.

## Benefits of TDD

- Catches bugs early, when they're cheapest to fix
- Forces you to think about requirements and design first
- Gives a safety net for refactoring
- Tests double as living documentation
- Produces high test coverage naturally

## Drawbacks

- Slower at the start
- Needs discipline and practice
- Poorly written tests can be brittle or give false confidence
- Hard to apply to UI-heavy or exploratory work

## Key terms

- **Test case**: a single test of one behaviour
- **Test suite**: a collection of test cases
- **Mock/stub**: a fake object standing in for a real dependency
- **Test coverage**: the percentage of code executed by tests
- **Regression**: a bug where something that used to work breaks. Unit tests help catch these.
- **Fixture**: setup code that prepares the state a test needs

## Where it fits

Unit tests form the base of the **testing pyramid**: many unit tests at the bottom, fewer integration tests in the middle, and few end-to-end tests at the top. TDD is also a core practice in **Extreme Programming (XP)** and other Agile methods.