---
aliases: 
checked: false
course: "[[CS6250 Computer Networks]]"
created: 2024-07-24
last_edited: 2024-07-24
publish: true
tags:
  - OMSCS
type: lecture
week: 10
---
pdef# Week 10 - Video applications

## Additional reading

### Important Readings

VoIP: A comprehensive survey on a promising technology  
[https://www.sciencedirect.com/science/article/abs/pii/S1389128609001200Links to an external site.](https://www.sciencedirect.com/science/article/abs/pii/S1389128609001200)

MPEG: A Video Compression Standard for Multimedia Application  
[https://dl.acm.org/doi/pdf/10.1145/103085.103090Links to an external site.](https://dl.acm.org/doi/pdf/10.1145/103085.103090)

The JPEG Compression standard  
[https://ieeexplore.ieee.org/document/125072Links to an external site.](https://ieeexplore.ieee.org/document/125072)

JPEG File Interchange Format  
[https://www.w3.org/Graphics/JPEG/jfif3.pdfLinks to an external site.](https://www.w3.org/Graphics/JPEG/jfif3.pdf)

Watching Video over the Web: Part 1: Streaming Protocols  
[https://ieeexplore.ieee.org/document/5677508Links to an external site.](https://ieeexplore.ieee.org/document/5677508)

A Quest for an Internet Video: Quality-of-Experience Metric  
[https://www.cs.cmu.edu/~xia/resources/Documents/Balachandran-hotnets2012.pdfLinks to an external site.](https://www.cs.cmu.edu/~xia/resources/Documents/Balachandran-hotnets2012.pdf)

Confused, Timid, and Unstable: Picking a Video Streaming Rate is Hard  
[https://dl.acm.org/doi/pdf/10.1145/2398776.2398800Links to an external site.](https://dl.acm.org/doi/pdf/10.1145/2398776.2398800)

### Book References

Kurose-Ross Edition 7, Chapter 9

## Basic requirements

Sounds and video are interesting internet applications due to their interesting requirements. First they have far higher [[Bit|bit]]-rates than other applications.

![[media_bit_rates.png]]

Where facebook is someone flicking through 1 picture per second. 

Whilst video does have a much larger bit-rate you may be ok with skipping [[Bit|bits]] or there being a slight delay - in contrast with voice where skipped  [[Bit|bits]] or delayed audio may make the stream unusable. Therefore they have different dynamics at play.

There are three different types of multi-media applications we will look at:
1. Streaming stored audio/video,
	- This requires to play before the whole file is downloaded.
	- It is interactive skipping forward, pausing going backward.
	- It should have continuous playout i.e. play out as it was recorded without freezing.
2. Conversational audio/video, and
	- Multiple users connecting to the same stream.
	- These are highly delay sensitive - normally 150ms is a bench mark to being acceptable. 
	- They are loss-tolerant. i.e. it is ok if there is a small skip or small sections are scrambled.  
3. Live audio/video.
	- This is similar to streamed but you have a one to many dynamic.
	- The users are geographically displaced.
	- They are very delay sensitive. 

## [[Voice over IP (VoIP)]]

![[Voice over IP (VoIP)|VoIP]]

[[Voice over IP (VoIP)|VoIP]] faces unique challenges as the [[Internet]] is best effort delivery and does not come with built in quality of service gaurentees. Moveover, audio is an analogue form so any [[Voice over IP (VoIP)|VoIP]] will need to send a digital approximation.

- **Encoding**: We normally encode sound by making lots of descrete apprximations of the waves current position this is call **[[Quantization|quantization]]**. There are different categories of encoding schemes, narrowband, broadband, and multimode these each have different trade offs. The encoding hopes to make speech intelligible but also use as little bandwidth as possible.
- **Signalling**: Traditionally this takes care of how calls are set up and torn down. [[Protocol (networks)|Protocols]] such as [[Session Initiation Protocol (SIP)]] had handle this in [[Voice over IP (VoIP)|VoIP]] applications. This has four major responsibilities.
	1. User location - the parties finding one another,
	2. Session establishment - handling the callee accepting, rejecting or redirecting the call,
	3. Session negotiation - endpoint synchronizing on the same standard,
	4. Call participation management - handling people joining or leaving.
	
## Quality of service metrics

There are 3 major quality of service metrics in [[Voice over IP (VoIP)|VoIP]]:
- **End to end delay**: The total time between speaking and hearing.
- **Jitter**: Scrambled or jumpy audio and video.
- **Packet loss**: The amount of missing data there is at the end of the call.

## End to end 

This includes:
- the time it takes to encode the audio,
- the time it takes to put it in packets, 
- all the normal sources of network delay that network traffic encounters such as queueing delays, 
- “playback delay,” which comes from the receiver’s playback buffer (which is a mitigation technique for delay jitter, which we’ll be discussing next),
- and decoding delay, which is the time it takes to reconstruct the signal.

Delay is very important to the end user to stop people talking over one another. Below displays the acceptable levels.

![[e2e_delay.png]]

## Jitter

Due to the [[Internet]] having unreliable network times - packets will be received in a different order than they were sent out. We call this phenomenon *jitter*. This is problematic for [[Voice over IP (VoIP)|VoIP]] as we need to reconstruct a audio signal that has continuous playout - gaps in audio must be kept to less that 30-75ms.

The main way to handle this is keeping a playout buffer or jitter window. This delays the playout on the receivers side to wait to collect all packets before playing out. This has a payoff, the longer you wait the less Jitter but the more end-to-end delay. The less you wait the more Jitter and packet loss.

## Packet loss

Due to the use of the [[Internet|internet]] packet loss is inevitable in [[Voice over IP (VoIP)|VoIP]]. However, [[Voice over IP (VoIP)|VoIP]] uses an even tougher definition of packet loss - which is either it is lost or it arrives after the jitter window. Luckily [[Voice over IP (VoIP)|VoIP]] can tolerate between 1-20% packet loss depending on voice codex used.

To avoid packet loss we might want to use [[Transmission Control Protocol (TCP)|TCP]] however due to the tougher definition the transmission of packets might arrive after the jitter window so be considered lost anyway. Therefore most [[Voice over IP (VoIP)|VoIP]] applications use [[User Datagram Protocol (UDP)|UDP]] and just accept some packet loss - this lowers bandwidth usage as well.

There are 3 major techniques to handle packet loss in [[Voice over IP (VoIP)|VoIP]]

### Forward Error Correction

This transmits redundant data that can fill any gaps. This increases the bandwidth used but decreases packet loss. This can be done in a few different ways:
- Breaking the data into chunks that are overlapping - then we can use xor to reconstruct the data.
- Transmitting a lower quality stream along side the high quality stream.
The more redundant data you send the more bandwidth you use. Also some of these techniques require you to wait longer before playing out increasing end-to-end delay.

![[fec_example.png]]

### Interleaving

This technique does not require additional data to be transmitted instead it breaks up the chunks of data so that the data in one chunk does not contain consecutive bits. That way a lost packet generate many small gaps not noticeable by the human ear. The pay off is having to wait longer to receive consecutive chunks which increases end-to-end delay. 

![[interleaving.png]]

### Error concealment

This involves filling in the gaps using the packets around it. There are two basic forms of this:
- Simply replacing missing gaps with the chunk from before. This is easy to implement and is fairly good in most circumstances.
- Interpolating from the chunks on either side. This is computationally more expensive but normally provides better estimates.

## Live/on demand streaming

