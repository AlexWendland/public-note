---
aliases:
checked: false
course: "[[CS6210 Advanced Operating Systems]]"
created: 2025-11-20
last_edited: 2025-11-20
draft: true
tags:
  - OMSCS
type: lecture
week: 9
---

# Week 9 - RT and Multimedia

## Time sensitive Linux (TS-Linux)

Historically, OS systems have been optimised to handle 'throughput orientated' tasks such as databases and scientific applications.
Though in modern OS's we have to prioritise 'latency orientated' tasks such as playing games and synchronous AB players.
These tasks need guarantees that events can happen at a given time.

### Sources of latency

There are 3 categories of latency between an event happening and us switching to the application to handle that event:

1. Timer latency: Due to the inaccuracy of the timer mechanism there is a difference between when the timer should have gone off and when the interrupt was actually thrown.
For example, periodic timers tend to have a 10ms granularity for when they can be scheduled.

2. Preemption latency: After the interrupt has happened the kernel may be stuck doing a task that can not be interrupted, such as manipulating core kernel data structures or handling a higher priority interrupt.

3. Scheduler latency: When the scheduler takes control after the interrupt is processed it may not choose to schedule the task that needs to handle the interrupt as there may be a higher priority task waiting.
So we need to wait for this task to be the highest priority task on a queue.

The difference between when the event should have been scheduled and the actual time the processes was switched into is called the `event to activation distance`.
A time sensitive OS wants to reduce the event to activation distance as much as possible for tasks that are time sensitive.

![Sources of latency](../../images/sources_of_latency_ts.png)

### Choice of timer

There are different types of timers we can choose from.
These each come with pros and cons.

- Periodic timers: These timers fire on a particular periodicity.
  - Pro: Periodic timers.
  - Con: Event recognition latency caused by the granularity of this timer.
- One shot timers: These timers fire once and then are disabled.
  - Pro: No event recognition latency.
  - Con: There may be added overhead switching at a given point to handle the event instead of in a natural break.
- Soft timers: These timers fire at convenient points in time, such as when the kernel is switched to for system calls or scheduling.
  - Pro: Zero overhead for handling the timer.
  - Con: Polling overhead on each switch and latency as there are no guarantees the kernel will be switched to.

It would be good if we didn't need to have these payoffs and could get all the upsides.
This is what the 'firm timer' achieves.

### Firm timers

Firm timers take a middle stance between one-shot timers and soft timers.
They are configured to happen at a particular time, but they have an *overshoot* window in which it is allowed to be late.
Within the window between when it was supposed to go off and the overshoot value, if we kernel is switched to then we handle the timer.
However, if we reach the end of the overshoot window we handle the timer like a one-shot timer.

This has the advantage of the soft-timers low overhead in most cases but the advantage that we know it will happen at a given time.

#### Implementation

There is a timer queue data structure which is a sorted list of timer tasks.
These have a key for the time they are meant to trigger at and a value as the entry point for the task they are supposed to run.

The one-shot timers are supported by the APIC timer hardware.
This is a hardware timer that gets decremented each clock cycle and throws an interrupt when it reaches zero.
Reprogramming these timers takes only a couple of cycles so they offer a efficient one-shot implementation.
Using a 100hz processor, this effectively drops the timer latency to 10 nanoseconds - but functionally the time taken to field the interupt takes longer than this and is a bigger source of the timer latency.

**Note**: The soft timer part of the implementation means that a lot of these one-shot timers are reprogrammed and never raise an interrupt.

#### Preempting one-shot timers with periodic timers

If we have one-shot timers with large distance between them and a periodic timer running then we can use the periodic timers to trigger the one-shot timers early.
This way we stop the overhead from happening from the one-shot timers.

**Question**: Won't the periodic timer going off trigger the soft timer mechanism anyway? Why is this a special case?

The firm timer mechanic reduces the timer latency - next we look at other forms of latency.

### Preemption latency

There are different approaches to reducing this latency:

- Explicit insertion of preemption points in the kernel.

- Allow preemption anytime the kernel is not manipulating shared data structures.

These two approaches can be combined to define lock-breaking preemptible kernel.
This idea is to break all kernel critical sections into smaller blocks:

- Manipulating shared data structures.

- All other actions taken in the critical section.

This breaks the critical section into smaller parts allowing the timers to interrupt these actions.

### Scheduling latency

This latency is caused by not being able to switch to the timer task fast enough.
TS-Linux reduces this in two ways.

#### Proportional period scheduling

In the OS we have defined time quantums we allow tasks to run for, T.
In addition to this we let tasks define the 'proportion' of a time quantum they need to run for, Q.
With this knowledge the OS can schedule tasks together that fit into one time quantum.

This allows TS-Linux to reserve a proportion of each time quantum for latency sensitive tasks.
This reduces the scheduling latency by timer based tasks get a boost in their priority relative to time insensitive tasks.

#### Priority scheduling

Suppose we have 3 tasks T1 > T2 > T3 which are ordered by priority.
Priority inversion, is where T1 gets blocked by T2 as it has a blocking section where it reaches out to T3.
Here the desired behaviour would be to run T1 until it blocks on T3 - then run that until T1 completes.
However, as T3 is lower priority than T2 the correct operation of T1 gets blocked by T2 jumping in the middle.

Priority scheduling accounts for this.
If a high priority tasks blocks on another - the lower priority task takes the priority of the task that is waiting for it.
This ensures the highest priority tasks complete first and do not get blocked by medium priority tasks.

