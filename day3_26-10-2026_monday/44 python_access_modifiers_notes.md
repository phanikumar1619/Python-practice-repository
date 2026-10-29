# Python Access Modifiers: Public, Protected, and Private

## 1. What are access modifiers?

Access modifiers describe how class attributes and methods are intended
to be accessed from inside or outside a class.

They are useful for organizing a class's interface, communicating which
parts other programmers should use, and protecting internal
implementation details from accidental misuse.

**Important Python detail:** Python does not enforce `public`,
`protected`, and `private` access in the same strict way that languages
such as Java do. Instead, Python mainly uses naming conventions and name
mangling.

## 2. Public members

A public member can be accessed from outside the class. In Python, a
name without a leading underscore is public by convention.

### Example

``` python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)


student = Student("Ravi", 90)

print(student.name)
print(student.marks)
student.display()
```

### Output

``` text
Ravi
90
Name: Ravi
Marks: 90
```

### Explanation

-   `name` and `marks` are public attributes.
-   `display()` is a public method.
-   Code outside the class can access these members directly.

### When are public members useful?

Use public members for information or operations that are meant to be
available to users of the class.

Examples include a student's name, a product's title, or a method that
displays an object's details.

## 3. Protected members

A name beginning with one underscore, such as `_marks`, is treated as
non-public by convention. It signals: **"This is an internal
implementation detail; use it carefully."**

Python does not strictly prevent outside code from accessing a
single-underscore member.

### Example

``` python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self._marks = marks

    def display_marks(self):
        print("Marks:", self._marks)


student = Student("Ravi", 90)

student.display_marks()
print(student._marks)  # Possible in Python, but usually discouraged
```

### Output

``` text
Marks: 90
90
```

### Explanation

-   `name` is public.
-   `_marks` is a protected-style attribute by convention.
-   The method `display_marks()` accesses `_marks` from inside the
    class.
-   The final line demonstrates that Python still permits outside
    access. The underscore is a warning to programmers, not a strict
    access barrier.

### Why use protected-style members?

They can communicate that an attribute or method is intended mainly for
the class's internal use or for use by subclasses. This helps maintain a
clear public interface and gives developers room to change
implementation details.

## 4. Private-style members

A name beginning with two underscores and not ending with two
underscores, such as `__password`, triggers Python's **name mangling**
when it appears in a class definition.

Name mangling changes the internal name to include the class name. For
example, `__password` in a class named `Account` is transformed to
`_Account__password`.

This helps avoid accidental name clashes, particularly with subclasses.
It does **not** make the attribute completely inaccessible or provide
strong security.

### Example

``` python
class Account:
    def __init__(self, owner, password):
        self.owner = owner
        self.__password = password

    def check_password(self, entered_password):
        return self.__password == entered_password


account = Account("Ravi", "abc123")

print(account.owner)
print(account.check_password("abc123"))
print(account.check_password("wrong"))
```

### Output

``` text
Ravi
True
False
```

### Explanation

-   `owner` is public and can be accessed directly.
-   `__password` is name-mangled.
-   `check_password()` provides a public method for checking the
    password without exposing it as part of the intended public
    interface.
-   `account.__password` will normally raise `AttributeError`, because
    that exact attribute name is not stored on the object.

For demonstration, Python's name mangling can be seen with:

``` python
print(account._Account__password)
```

This can access the value, which proves that double underscores do not
create absolute privacy. **Do not use this technique to store real
secrets securely.** Access modifiers are about class design, not
security or encryption.

### Why use private-style members?

Use double-underscore names when you specifically want to reduce
accidental name clashes with subclasses or make internal attributes less
likely to be accessed unintentionally. For many ordinary internal
attributes, a single leading underscore is the usual Python convention.

## 5. Comparison table

  -----------------------------------------------------------------------
  Type              Naming pattern    Meaning           Is outside access
                                                        prevented?
  ----------------- ----------------- ----------------- -----------------
  Public            `name`            Intended for      No
                                      general use       

  Protected-style   `_name`           Intended for      No; convention
                                      internal or       only
                                      subclass use      

  Private-style     `__name`          Name-mangled to   No; name mangling
                                      reduce accidental is not strict
                                      clashes           privacy
  -----------------------------------------------------------------------

## 6. Why are these conventions useful?

1.  **Clear interface:** Other developers can tell which methods and
    attributes are intended for general use.
2.  **Encapsulation:** A class can expose a small set of public methods
    while keeping implementation details separate.
3.  **Safer maintenance:** Users of a class are less likely to depend on
    internal details that may change.
4.  **Subclassing:** Name mangling helps avoid accidental collisions
    between base-class and subclass attributes.
5.  **Readability:** Naming conventions make the programmer's intentions
    easier to understand.

Remember: these conventions reduce accidental misuse; they do not
guarantee that code cannot access an attribute.

## 7. A practical example

Imagine a `BankAccount` class:

-   `owner` --- public, because users may need to see the account
    holder's name.
-   `_transaction_count` --- protected-style, indicating internal
    tracking information.
-   `__pin` --- private-style, reducing accidental access and name
    clashes.

A real banking application must **not** rely on underscores or name
mangling to secure a PIN. Real security requires appropriate
authentication, access controls, and secure storage.

## 8. Common mistakes

### Mistake 1: Saying Python has strict protected access

Incorrect: "A `_value` attribute cannot be accessed outside the class."

Correct: A single leading underscore is a convention. Outside access is
still possible.

### Mistake 2: Saying double underscores make a value completely private

Incorrect: "No code outside the class can access `__value`."

Correct: Python name-mangles the name to help avoid accidental access
and naming conflicts. It is still possible to access the mangled name.

### Mistake 3: Confusing `__name` with `__name__`

-   `__value` is a double-leading-underscore name that is generally
    name-mangled inside a class.
-   `__init__` is a special method name (often called a "dunder" method)
    and is not treated as a private attribute by this rule.

## 9. Interview-ready answer

**Python access modifiers** describe the intended accessibility of class
attributes and methods. Python commonly uses naming conventions rather
than strict access enforcement:

-   **Public:** `name` --- available for normal access from inside and
    outside the class.
-   **Protected-style:** `_name` --- a convention indicating that the
    member is intended for internal or subclass use; Python does not
    block outside access.
-   **Private-style:** `__name` --- Python applies name mangling,
    changing it to a form such as `_ClassName__name`. This helps avoid
    accidental name clashes but does not provide absolute privacy.

These conventions support encapsulation, improve readability, clarify a
class's public interface, and reduce accidental misuse. They should not
be treated as security mechanisms.

## 10. Quick revision

-   No leading underscore: **public**
-   One leading underscore: **non-public by convention**
-   Two leading underscores: **name mangling**
-   Python does not provide strict access control using these naming
    patterns.
-   Use public methods to expose intended operations; do not rely on
    underscores to protect secrets.

## Official reference

-   Python Tutorial --- Private Variables:
    https://docs.python.org/3/tutorial/classes.html#private-variables
-   Python Programming FAQ --- Name mangling:
    https://docs.python.org/3/faq/programming.html
