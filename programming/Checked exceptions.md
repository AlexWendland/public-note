---
aliases: []
type: str
publish: false
created: 2023-08-20
last_edited: 2023-08-20
tags: programming, clean-code
chatgpt: true
---
# Checked exceptions

Checked exceptions are a feature of some programming languages, most notably [[Java]], that enforce a strong contract between a method that can fail (throw an exception) and the caller that must handle that failure. When a method might throw a checked exception, the language requires that the method declare this fact in its method signature using a `throws` clause. Any calling method is then obligated either to catch the exception and handle it or to declare that it, too, throws the [[Exception|exception]], propagating it up the call stack.

### Example in Java

Here's a simple example in Java to illustrate how checked exceptions work:

```java
import java.io.*;

public class CheckedExample {
    // This method declares that it may throw an IOException
    public void readFile(String fileName) throws IOException {
        BufferedReader reader = new BufferedReader(new FileReader(fileName));
        // Reading file
    }

    public static void main(String[] args) {
        CheckedExample example = new CheckedExample();

        try {
            // readFile() may throw IOException, so we're obligated to catch it
            example.readFile("somefile.txt");
        } catch (IOException e) {
            // Handle the exception
            e.printStackTrace();
        }
    }
}
```

### Distinguishing Features

The core features that distinguish checked exceptions from their unchecked counterparts are:

1. **Explicit Contract**: The `throws` clause in the method signature clearly specifies the types of exceptions that can be thrown, making it part of the method's contract.
    
2. **Compile-time Checking**: The Java compiler checks to ensure that any method that could throw a checked exception is either surrounded by a try-catch block or declares the exception in its own `throws` clause. This ensures that error-handling is not forgotten, thereby reducing runtime errors.
    
3. **Intentionality**: The explicit nature of checked exceptions forces developers to think about the exceptional conditions a method may encounter, encouraging more robust error handling.

### Criticisms and Limitations

While checked exceptions aim to improve software robustness by enforcing explicit error-handling, they have their critics. Some common criticisms are:

1. **Verbosity**: The need to either catch or declare exceptions can make code more verbose and harder to read.
    
2. **Tight Coupling**: Checked exceptions can tightly couple methods to their callers, making changes to a method's exception-handling behavior more difficult to implement without affecting the callers. This violates the [[Open Closed Principle (OCP)|Open Closed principle]] as any change to a dependencies checked exceptions will force a change in dependent code.
    
3. **Abuse of Exception Handling**: To avoid dealing with checked exceptions, developers sometimes catch the exception and do nothing in the catch block, essentially swallowing the exception, which is considered bad practice.
    
4. **Reduced Flexibility**: The strict contract imposed by checked exceptions may sometimes limit the flexibility to change how errors are handled at runtime.

Because of these limitations, some modern languages like [[C#]], [[Python]], and [[Go]] avoid the concept of checked exceptions altogether. Nevertheless, when used judiciously, checked exceptions can be a useful feature for building reliable and maintainable software.