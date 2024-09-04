---
aliases: 
checked: false
course: "[[CS6200 Graduate introduction to Operating Systems]]"
created: 2024-09-04
last_edited: 2024-09-04
publish: true
tags:
  - OMSCS
type: lecture
week: 4
---
# Week 4 - PThreads

![[Portable operating system interface (POSIX)|POSIX]]

![[POSIX threads (PThreads)|PThreads]]

## Thread interface

The core [[Data structure|data structure]] in the [[POSIX threads (PThreads)|PThreads]] library is `pthread_t` which represents a thread. This can be created through:
``` c
int pthread_create(
	pthread_t *thread,
	const pthread_attr_t *attr,
	void * (*start_routine)(void *),
	void *arg
)
```

>[!note] Void is C's any type

The first argument `thread` will be filled with the thread once it is created. (We will come back to `pthread_attr_t` later - if you pass `NULL` you will get default behaviour.) The third argument `start_routine` is a function to call this arguments `arg`. It will return the status code of the operation.

This can be joined to the main thread using:
``` c
int pthread_join(
	pthread_t thread,
	void **status
)
```
where `thread` is the thread you want to join and `status` will be the return object. It will return the status code of the operation.

### Pthread attributes

The `pthread_attr_t` type controls the type of thread created with the properties:
- Stack size,
- Scheduling policy, 
- Priority,
- System/process thread,
- inheritance (if it should inherit attributes from the parent thread), and
- joinable.
The object can be created and destroyed through the following interface.
``` c
int pthread_attr_init(pthread_attr_t *attr)
int pthread_attr_destroy(pthread_attr_t *attr)
```
You can then set/get attribute values through the following function.
```c
pthread_attr_{set/get}{attribute}
```
For example `pthread_attr_setjoinable`. 

### Detachable threads

Threads that are created from a parent need to be joined by that parent in order for them to be cleaned up by the [[Operating system (OS)|OS]]. Though if the parent thread exits before this happens it can create zombie threads that can not be cleaned up.

If you need to create a child thread that will outlive its parent then you can make it detachable. This means it is no longer needs to be joined to exit - it can instead use the following function.
```c
void pthread_exit()
```
Threads can be made detachable using the `joinable` property or by calling detach from within the executing function.
```c
pthread_attr_setjoinable(attr, PTHREAD_CREATE_DETACHED)
int pthread_detach()
```

### Example

```c
#include <stdio.h>
#include <pthread.h>

void *foo (void *arg) {		/* thread main */
	printf("Foobar!\n");
	pthread_exit(NULL);
}

int main (void) {

	int i;
	pthread_t tid;
	
	pthread_attr_t attr;
	pthread_attr_init(&attr); // Required!!!
	pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_DETACHED);
	pthread_attr_setscope(&attr, PTHREAD_SCOPE_SYSTEM);
	pthread_create(&tid, &attr, foo, NULL);

	return 0;
}
```

When using Pthreads:
- Include the pthread library `#include <pthread.h>`
- Compile code using the pthreads flag: either `-lpthread` or `-pthread`.
- Check the return value of pthread function calls in case of errors.


