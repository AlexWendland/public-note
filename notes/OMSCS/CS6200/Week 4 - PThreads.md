---
aliases:
checked: false
course: '[[CS6200 Graduate introduction to Operating Systems]]'
created: 2024-09-04
draft: false
last_edited: 2024-09-04
tags:
  - OMSCS
type: lecture
week: 4
---
# Week 4 - PThreads

## Additional reading

- ["An Introduction to Programming with Threads"](https://s3.amazonaws.com/content.udacity-data.com/courses/ud923/references/ud923-birrell-paper.pd)
- [PThreads Programming Resource](https://computing.llnl.gov/tutorials/pthreads/)

## Background

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

## [[Mutex]]

The [[POSIX threads (PThreads)|PThreads]] library allows you to create and use [[Mutex|mutexes]].

```c
pthread_mutex_t aMutex;
int pthread_mutex_lock(pthread_mutex_t *mutex);
int pthread_mutex_unlock(pthread_mutex_t *mutex);
```

For example to implement safe lock and unlock using this would be:

```c
list<int> my_list;
pthread_mutex_t list_mutex;

void safe_insert(int to_add){
	pthread_lock(list_mutex);
	my_list.insert(to_add);
	pthread_unlock(list_mutex);
}
```

You must initialise and cleanup mutexes.

```c
int pthread_mutex_init(
	pthread_mutex_t *mutex,
	pthread_mutexattr_t *attr,
);
int pthread_mutex_destroy(pthread_mutex_t *mutex);
```

[[Mutex]] have 3 attributes:
- Mutex Type: can be changed to allow for [[Deadlock|deadlock]] detection.
- Mutex Protocol: Determines the thread priority when holding the mutex.
- Process-Shared Attribute: Determines if the mutex applies just to this process or can be shared.
- Robustness Attribute: Determines if the mutex should be recoverable from a crash or not.

Another nice feature is the trylock which allows a thread to check if a mutex is free without getting blocked by it.

```c
int pthread_mutex_trylock(pthread *mutex);
```

This will return 0 if it is free or `EBUSY` if not.

Lastly a couple reminders about working with mutexes:
- Shared data must be accessed through a single mutex.
- A mutex must be visible to all threads. i.e. declare them as global variables.
- Globally order locks to prevent [[Deadlock|deadlock]].
- Always unlock the correct mutex.

## [[Conditional variables (Mutex)|Conditional variables]]

[[POSIX threads (PThreads)|PThreads]] supports the [[Application Programming Interface (API)|API]] we saw in the last lecture.

```c
pthread_cond_t aCond;
int pthread_cond_wait(pthread_cond_t *cond, pthread_mutex_t *mutex);
int pthread_cond_signal(pthread_cond_t *cond);
int pthread_cond_broadcast(pthread_cond_t *cond);
```

Conditional variables need to be created and destroyed.

```c
int pthread_cond_init(
	pthread_cond_t *cond,
	pthread_condattr_t *attr,
);
int pthread_cond_destroy(pthread_cond_t *cond);
```

The attributes you can provide are:
- **Process-Shared (`PTHREAD_PROCESS_SHARED`, `PTHREAD_PROCESS_PRIVATE`)**: Determines whether the condition variable is shared between processes or only within a single process.
- **Clock (`CLOCK_REALTIME`, `CLOCK_MONOTONIC`)**: Specifies which clock to use for timed wait operations on the condition variable.

Some notes on [[Conditional variables (Mutex)|conditional variables]]:
- Make sure any predicate change is followed by the required signal/broadcast.
- If you do not know whether to use signal or broadcast, use broadcast (though check this later as you will lose performance).
- To avoid [[Spurious wakeups|spurious wakeups]] think about if you need to hold the [[Mutex|mutex]] when doing your signal or broadcast.
