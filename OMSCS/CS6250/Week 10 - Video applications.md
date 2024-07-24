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
# Week 10 - Video applications

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

