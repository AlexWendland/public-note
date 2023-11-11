---
aliases: []
chatgpt: true
created: 2023-08-20
last_edited: 2023-08-20
publish: true
tags: programming, clean-code
type: practice
---
# Wrap 3rd party libraries

It is generally good practice to wrap 3rd party libraries with your own [[API]] to be used within your code bases. However, this does come with some downsides. There is a [[Balance between library providers and users|balance between library providers and users]] and depending on how well they have managed this balance also effects the decision on whether to wrap the library or not.

## Advantages of Wrapping

1. **API Control**: Wrapping allows you to define your own API, giving you greater control over how you interact with the 3rd party library. This can simplify usage and make it easier to implement across your codebase.
2. **Easy Transition**: If the 3rd party library becomes obsolete, gets deprecated, or you find a better alternative, wrapping allows you to switch to a different library with minimal effort. You only have to update the wrapper instead of changing every instance where the library is used.
3. **Exception Handling**: Wrapping allows you to handle exceptions in a way that's more aligned with your application's needs. This can improve robustness and make it easier to debug issues.
4. **Isolation**: Wrapping isolates the 3rd party library, making it easier to mock for unit testing, monitor its behaviour, or switch out for a different library.

## Caveats and Considerations

1. **Overhead**: Wrapping adds another layer to your code, which can introduce bugs, increase complexity, and potentially reduce performance.
2. **Maintenance**: The wrapper needs to be updated whenever the 3rd party library is updated, especially if there are breaking changes. This can become a maintenance burden over time.
3. **Learning Curve**: New team members will need to understand both the wrapper and the underlying library, which can increase the time needed to become productive.
4. **Feature Utilization**: It's easy to create a wrapper that only exposes the subset of the library's features you initially need, making it harder to take advantage of the library's full capabilities later on.
5. **[[Premature Abstraction]]**: For very small projects or prototypes, wrapping might be overkill and could unnecessarily complicate the codebase.

## Summary

While wrapping 3rd party libraries can provide benefits in terms of API control, transition ease, and tailored exception handling, it's essential to weigh these advantages against the potential downsides of increased complexity, maintenance burden, and a steeper learning curve. The decision should be made based on the project's size, long-term maintenance outlook, and the criticality of the 3rd party library to the application.
