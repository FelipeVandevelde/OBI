# Linguagens de programação

As linguagens de programação aceitas pela OBI são:

1. C
2. C++
3. Python
4. Java
5. JavaScript

# Qual delas é a melhor?

Para os problemas apresentados nas fases, todas as linguagens são adequadas. Você deve escolher aquela cuja sintaxe lhe **proporcione maior *conforto* e *familiaridade***.

A recomendação, para quem já está acostumado e aprecia o **C#**, é o **Java**, pois possui uma sintaxe bastante semelhante em diversos aspectos.

Outra recomendação válida é o Python, que apresenta uma **curva de aprendizado** mais suave por ser uma linguagem de alto nível.

# Exemplos de cada linguagem

##### Os exemplos apresentados abaixo foram elaborados utilizando um compilador online: ([myCompiler](https://www.mycompiler.io/pt)).

## Imprimir um output

### C#

```cs
using System;

namespace MyCompiler {
    class Program {
        public static void Main(string[] args) {
            Console.WriteLine("Hello world!");
        }
    }
}
```

### C

```c
#include <stdio.h>

int main() {
    printf("Hello world!\n");
    return 0;
}
```

### C++

```cpp
#include <iostream>

int main() {
    std::cout << "Hello world!" << std::endl;
    return 0;
}
```

### Python

```python
print('Hello world!')
```

### Java

```java
import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}
```

### JavaScript

```js
console.log("Hello world!");
```

## Armazenar um input

### C#

```cs
using System;

class Program
{
    static void Main()
    {
        string input = Console.ReadLine();
        Console.WriteLine("Você digitou: " + input);
    }
}

```

### C

```c
#include <stdio.h>

int main() {
    char input[100];
    fgets(input, sizeof(input), stdin);
    printf("Você digitou: %s", input);
    return 0;
}
```

### C++

```cpp
#include <iostream>
#include <string>

int main() {
    std::string input;
    std::getline(std::cin, input);
    std::cout << "Você digitou: " << input << std::endl;
    return 0;
}

```

### Python

```python
input = input()
print("Você digitou:", input)
```

### Java

```java
import java.util.*;
import java.lang.*;
import java.io.*;

class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
    }
}
```

### JavaScript

```js
var input = require("fs").readFileSync("/dev/stdin", "utf8");

console.log("Você digitou: " + input);
```
